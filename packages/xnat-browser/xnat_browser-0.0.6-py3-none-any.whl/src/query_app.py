from __future__ import annotations

import json
import logging
from dataclasses import dataclass, astuple
from pathlib import Path
from typing import Any, cast, Final

import pandas as pd
import xnat
import xnat.search
from rich.text import Text
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widget import Widget
from textual.widgets import Input, Button, Header, DataTable, Footer, Select
from textual_fspicker import FileOpen, Filters, FileSave

from src.app_base import XnatBase

MAX_SEARCHES: Final[int] = 5

OPERATOR_OPTIONS = [('<', '<'),
                    ('<=', '<='),
                    ('=', '='),
                    ('>=', '>='),
                    ('>', '>'),
                    ('like', 'like')]


@dataclass(frozen=True)
class SearchField:
    name: str
    identifier: str

    @staticmethod
    def __convert(name: str) -> str:
        return name.replace('_', '').casefold()

    def __eq__(self, other: object) -> bool:
        return self.__convert(self.name) == self.__convert(cast(SearchField, other).name)

    def __hash__(self) -> int:
        return hash(self.__convert(self.name))


# noinspection PyPep8Naming
def get_search_terms(connection: xnat.XNATSession) -> dict[Any, list[str]]:
    classes = [connection.classes.SubjectData,
               connection.classes.MrScanData]

    search_fields = {}
    for xnat_type in classes:
        search_fields[xnat_type] = \
            [x for x in dir(xnat_type) if isinstance(getattr(xnat_type, x), xnat.search.BaseSearchField)]

    return search_fields


def get_select_fields(search_terms: dict[Any, list[str]]) -> list[tuple[str, str]]:
    fields: set[SearchField] = set()
    for xnat_type, search_fields in search_terms.items():
        # noinspection PyProtectedMember
        # pylint: disable=protected-access
        new_fields = {SearchField(name=x.casefold(), identifier=f'{xnat_type._XSI_TYPE}/{x}') for x in search_fields}
        fields.update(new_fields)
        # pylint: enable=protected-access
    return [cast(tuple[str, str], astuple(x)) for x in sorted(fields, key=lambda x: x.name.casefold())]


class SearchEntry(Widget):
    """Search entry widget. Consists of a search field, operator and value."""
    DEFAULT_CSS = """
    SearchEntry {
        height: 3;
    }
    SearchEntry Input {
        width: 1fr;
    }
    .search_field{
        min-width: 45;
        width: 1fr;
    }
    .search_operator {
        width: 15;
    }
    """

    def __init__(self, connection: xnat.XNATSession, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields = get_select_fields(get_search_terms(connection))

    def compose(self) -> ComposeResult:
        with Horizontal(id='horizontal'):
            yield Select(self.fields, id='field', classes='search_field')
            yield Select(OPERATOR_OPTIONS, id='operator', classes='search_operator')
            yield Input(id='value', placeholder='Value...')

    @property
    def constraint(self) -> None | xnat.search.Constraint:
        identifier = self.query_one('#field', Select).value
        operator = self.query_one('#operator', Select).value
        value = self.query_one('#value', Input).value
        if identifier is None or operator is None:
            return None

        return xnat.search.Constraint(identifier, operator, value)

    @constraint.setter
    def constraint(self, data: xnat.search.Constraint) -> None:
        search_entry = next((x for x in self.fields if x[0] == data.identifier), None)
        if search_entry is None:
            raise RuntimeError(f'Could not find search_entry: {data.identifier}')

        self.query_one('#field', Select).value = search_entry[1]
        self.query_one('#operator', Select).value = data.operator
        self.query_one('#value', Input).value = data.right_hand


class XnatQuery(XnatBase):
    CSS_PATH = 'query.tcss'
    BINDINGS = [
        Binding('ctrl+t', 'toggle_dark', show=False),
        Binding('s', 'save_result', 'Save Result'),
        Binding('ctrl+l', 'load_search', 'Load Search'),
        Binding('ctrl+s', 'save_search', 'Save Search'),
    ]

    def __init__(self, server: str, log_level: int = logging.INFO):
        super().__init__(server, log_level)
        self.query_result: pd.DataFrame | None = None

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal(id='horizontal'):
            with Vertical(id='query_input'):
                yield Button(label='Query', id='query_button')
                for index in range(MAX_SEARCHES):
                    yield SearchEntry(connection=self.session, id=f'search_{index}')
            yield DataTable(id='data_table')
        yield self._setup_logging()
        yield Footer()

    def _get_query_constraints(self) -> list[xnat.search.Constraint]:
        constraints = []
        for index in range(MAX_SEARCHES):
            constraint = self.query_one(f'#search_{index}', SearchEntry).constraint
            if constraint is None:
                continue
            constraints.append(constraint)
        return constraints

    def _set_query_constraints(self, constraints: list[xnat.search.Constraint]) -> None:
        for index, constraint in enumerate(constraints):
            self.query_one(f'#search_{index}', SearchEntry).constraint = constraint

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.control.id != 'query_button':
            return

        query = self.session.classes.MrScanData.query()
        for constraint in self._get_query_constraints():
            query = query.filter(constraint)

        self.query_result = (query.tabulate_pandas().dropna(axis='columns', how='all').
                             drop(columns=['project', 'quality', 'uid', 'quarantine_status'], errors='ignore'))

        if len(self.query_result) == 0:
            self.logger.info('Query returned 0 results.')

        data_table = self.query_one('#data_table', DataTable)
        data_table.clear()

        columns = self.query_result.columns.values.tolist()
        data_table.add_columns(*columns)
        for index, data in enumerate(self.query_result.itertuples(index=False, name=None), 1):
            label = Text(str(index), style='#B0FC38 italic')
            data_table.add_row(*data, label=label)

    def action_load_search(self) -> None:
        """Show the `FileOpen` dialog when the button is pushed."""
        self.push_screen(
            FileOpen('.', filters=Filters(('Searches', lambda p: p.suffix.lower() == '.json'))),
            callback=self.load_search)

    def action_save_search(self) -> None:
        self.push_screen(FileSave(filters=Filters(('Searches', lambda p: p.suffix.lower() == '.json'))),
                         callback=self.save_search)

    def action_save_result(self) -> None:
        self.push_screen(FileSave(), callback=self.save_result)

    def load_search(self, filename: Path | None) -> None:
        if filename is None:
            return

        with filename.open('r') as input_file:
            data = json.load(input_file)

        self._set_query_constraints([xnat.search.Constraint(*x) for x in data])

    def save_search(self, filename: Path | None) -> None:
        if filename is None:
            return

        fields = get_select_fields(get_search_terms(self.session))

        constraints = []
        for val in self._get_query_constraints():
            search_entry = next((x for x in fields if x[1] == val.identifier), None)
            if search_entry is None:
                continue
            constraints.append((search_entry[0], val.operator, val.right_hand))

        with filename.open('w') as output_file:
            output_file.write(json.dumps(constraints, indent=4, sort_keys=True))

    def save_result(self, filename: Path | None) -> None:
        if filename is None or self.query_result is None:
            return

        if filename.suffix == '.csv':
            self.query_result.to_csv(filename, index=False)
            return

        if filename.suffix == '.xlsx':
            self.query_result.to_excel(filename, index=False)
            return

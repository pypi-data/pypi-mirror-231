from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import ScrollableContainer, HorizontalScroll, VerticalScroll
from textual.widget import Widget
from textual.widgets import Header, Footer, Label, Input

from src.app_base import XnatBase
from src.quit_screen import QuitScreen
from src.xnat_tree import XnatTree


class XnatBrowser(XnatBase):
    CSS_PATH = 'browser.tcss'
    BINDINGS = [
        Binding('ctrl+t', 'toggle_dark', show=False),
        Binding('q', 'quit', 'Quit'),
        Binding('ctrl+f', 'filter_project', 'Filter Project'),
        Binding('escape', 'dismiss', show=False),
    ]

    def compose(self) -> ComposeResult:
        output = Label(id='dicom_info', expand=True)
        yield Header(show_clock=True)
        with HorizontalScroll(id='h_scroll'):
            with VerticalScroll(id='v_scroll'):
                yield Input(placeholder='Project', id='project_search', classes='remove')
                yield XnatTree(self._server, output, self.logger, id='xnat_tree')
            with ScrollableContainer(id='dicom_info_container'):
                yield output
        yield self._setup_logging()
        yield Footer()

    async def on_input_changed(self, message: Input.Changed) -> None:
        xnat_tree = self.query_one('#xnat_tree', XnatTree)
        await xnat_tree.select_projects(str(message.value))

    def action_filter_project(self) -> None:
        self.query_one('#project_search', Widget).toggle_class('remove')

    def action_dismiss(self) -> None:
        self.query_one('#dicom_info', Label).update('')

    async def action_quit(self) -> None:
        await self.push_screen(QuitScreen())

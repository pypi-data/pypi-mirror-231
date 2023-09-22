import http
import logging
import re
from typing import Any, Final, cast

import xnat
from rich.text import Text
from textual import work
from textual.binding import Binding
from textual.widgets import Tree, Label
from textual.widgets.tree import TreeNode
from xnat.core import XNATListing
from xnat.exceptions import XNATAuthError, XNATLoginFailedError, XNATExpiredCredentialsError, XNATNotConnectedError, \
    XNATResponseError
from xnat.mixin import ImageScanData, ProjectData, SubjectData, ImageSessionData
from xnat.prearchive import PrearchiveScan, PrearchiveSession

from src.create_markdown import create_markdown
from src.dicom_highlighter import DicomHighlighter


ARCHIVE_NODE_ID: Final[str] = 'archive'
PRE_ARCHIVE_NODE_ID: Final[str] = 'pre_archive'


class XnatTree(Tree):
    CSS_PATH = 'browser.tcss'
    BINDINGS = [
        ('d', 'dicom', 'DICOM info'),
        Binding('u', 'update_projects', 'Update projects', show=False),
        Binding('left', 'goto_parent', 'Goto Parent'),
    ]

    def __init__(self, server: str, output_pane: Label, logger: logging.Logger, **kwargs: Any) -> None:
        super().__init__(server, **kwargs)
        self.output = output_pane
        self.logger = logger
        self.show_root = False
        try:
            self.session = xnat.connect(server=server, default_timeout=300)
            self.logger.debug(f'Connected to: {server}')
        except (XNATAuthError, XNATLoginFailedError, XNATExpiredCredentialsError, XNATNotConnectedError):
            self.logger.error('Error connecting to XNAT server.')

    def on_mount(self) -> None:
        self.focus()

        archive_node = self.root.add('Archive', data=ARCHIVE_NODE_ID)

        # sort the projects using case-insensitive sorting.
        for project in sorted(self.session.projects.values(), key=lambda x: x.name.casefold()):  # type: ignore
            archive_node.add(project.name, project)
        archive_node.expand()
        archive_node.set_label(Text(f'[{len(archive_node.children):>2}] Archive'))

        prearchive_node = self.root.add('Pre-archive', data=PRE_ARCHIVE_NODE_ID)
        nodes: dict[str, TreeNode] = {}
        for project in sorted({x.project for x in self.session.prearchive.sessions()}):
            nodes[project] = prearchive_node.add(project)
        prearchive_node.set_label(Text(f'[{len(nodes):>2}] Pre-archive'))

        for prearchive_session in self.session.prearchive.sessions():
            if prearchive_session.status == 'ERROR':
                nodes[prearchive_session.project].add_leaf('Error', {})
                continue
            nodes[prearchive_session.project].add(prearchive_session.subject, prearchive_session)

        self.root.expand()

    def action_goto_parent(self) -> None:
        node = self.cursor_node
        if node is None or node.parent is None:
            return

        self.select_node(node.parent)
        self.scroll_to_node(node.parent)

    def action_dicom(self) -> None:
        self.logger.debug('DICOM action')
        node = self.cursor_node
        if node is None:
            return

        if isinstance(node.data, (ImageScanData, PrearchiveScan)):
            try:
                self.output.update(DicomHighlighter()(str(node.data.read_dicom())))
            except XNATResponseError as e:
                status = _get_http_status_code(e)
                if status == http.HTTPStatus.FORBIDDEN:
                    self.logger.error("you don't have permission to access this resource.")
                    return
                self.logger.error(f'Error downloading dicom file. {e}')
            except ValueError as e:
                self.logger.error(f'Error {e}')

    @work(thread=True)
    def action_update_projects(self) -> None:
        archive_node = self.get_archive_node()

        if archive_node is None:
            self.logger.error('Could not find "Archive" node.')
            return

        # make a copy of the children because the iterator becomes invalid on node removal.
        for project_node in list(archive_node.children):
            num_subjects = len(cast(ProjectData, project_node.data).subjects)
            if num_subjects == 0:
                project_node.remove()
                continue

            project_node.set_label(Text(f'[{num_subjects:>4} SUB] {project_node.label}'))
        archive_node.set_label(Text(f'[{len(archive_node.children):>2}] Archive'))

    def get_archive_node(self) -> TreeNode | None:
        for node in self.root.children:
            if node.data == ARCHIVE_NODE_ID:
                return node
        return None

    def on_tree_node_highlighted(self, event: Tree.NodeHighlighted) -> None:
        self.output.update('')

        if self.cursor_node is None:
            return

        self.output.update(create_markdown(event.node.data))

    def on_tree_node_expanded(self, event: Tree.NodeExpanded) -> None:
        self.output.update('')

        if not _is_archive(event.node):
            _process_pre_archive_node(event, self.logger)
            return

        _process_archive_node(event)

    async def select_projects(self, value: str) -> None:
        archive_node = self.get_archive_node()

        if archive_node is None:
            self.logger.error('Could not find "Archive" node.')
            return

        archive_node.remove_children()

        for project in sorted(self.session.projects.values(), key=lambda x: x.name.casefold()):  # type: ignore
            if not str(project.name).casefold().startswith(value.casefold()):
                continue
            archive_node.add(project.name, project)

        archive_node.expand()
        archive_node.set_label(Text(f'[{len(archive_node.children):>2}] Archive'))


def _add(node: TreeNode, data: XNATListing, suffix: str = "") -> None:
    node.set_label(Text(f'[{len(data):>4}{suffix}] {node.label}'))
    for key in sorted(x.label for x in data.values()):
        value = data[key]
        node.add(value.label, value)


def _process_archive_node(event: Tree.NodeExpanded) -> None:
    if len(event.node.children) > 0:
        return

    if isinstance(event.node.data, ProjectData):
        _add(event.node, event.node.data.subjects, ' SUB')
        return

    if isinstance(event.node.data, SubjectData):
        _add(event.node, event.node.data.experiments, ' EXP')  # type: ignore
        return

    if isinstance(event.node.data, ImageSessionData):
        data = event.node.data.scans  # type: ignore
        event.node.set_label(Text(f'[{len(data):>3} SCN] {event.node.label}'))
        for scan in data.values():  # type: ignore
            event.node.add_leaf(scan.type, scan)
        return


def _process_pre_archive_node(event: Tree.NodeExpanded, logger: logging.Logger) -> None:
    if not isinstance(event.node.data, PrearchiveSession) or len(event.node.children) > 0:
        return

    try:
        data = event.node.data.scans
        for scan in data:
            scan_node = event.node.add(scan.id, scan)
            for key, value in scan.data.items():
                scan_node.add(key, value)
    except XNATResponseError as e:
        status = _get_http_status_code(e)
        if status == http.HTTPStatus.NOT_FOUND:
            logger.error("Resource not found.")
        if status == http.HTTPStatus.FORBIDDEN:
            logger.error("You don't have permission to access this resource.")
            return
        raise XNATResponseError from e


def _is_archive(node: TreeNode) -> bool:
    while node.parent is not None:
        if str(node.data) == 'archive':
            return True
        return _is_archive(node.parent)

    return False


def _get_http_status_code(e: Exception) -> int:
    match = re.search(r'status (?P<status_code>\d{3})', str(e), flags=re.S)
    if not match:
        return -1

    return int(match.group("status_code"))

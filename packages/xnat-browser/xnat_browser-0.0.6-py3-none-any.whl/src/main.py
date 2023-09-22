""" CLI """
import logging

import typer
import rich.traceback
import rich.logging

from src.browse_app import XnatBrowser
from src.query_app import XnatQuery

app = typer.Typer(add_completion=False, no_args_is_help=True)


@app.command()
def browse(server: str, verbose: bool = typer.Option(False, '--verbose', '-v')) -> None:
    XnatBrowser(server, logging.DEBUG if verbose else logging.INFO).run()


@app.command()
def query(server: str, verbose: bool = typer.Option(False, '--verbose', '-v')) -> None:
    # from textual.app import App, ComposeResult
    # from src.query_app import SearchEntry
    # class SearchTest(App):
    #     def compose(self) -> ComposeResult:
    #         yield SearchEntry()
    #
    # SearchTest().run()
    XnatQuery(server, logging.DEBUG if verbose else logging.INFO).run()


if __name__ == "__main__":
    rich.traceback.install(width=None, word_wrap=True)
    app()

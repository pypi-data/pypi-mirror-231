"""
CLI entry points for Typer (https://typer.tiangolo.com/) made CLI.
"""

from datetime import datetime
from importlib.metadata import version as get_version
from pathlib import Path
from typing import Optional

import typer

from profitpulse.ui.cli_adapters import (
    close_account,
    deposit,
    import_file,
    migrate_database,
    open_account,
    report,
    reset,
    show_accounts,
)

app = typer.Typer(
    add_completion=False,
    help="Profitpulse helps you manage your personal finances.",
)

migrate_database()


@app.command(name="version", help="Shows current version")
def version():
    pass
    typer.echo(get_version("profitpulse"))


@app.command(name="import", help="Imports the transactions to feed the application")
def import_(file_path: Path):
    reset()
    migrate_database()
    import_file(file_path)


@app.command(name="report", help="Builds reports according to filters")
def report_(
    seller: Optional[str] = typer.Option(default="", help="Filters report by Seller"),
    since: Optional[datetime] = typer.Option(
        default=None, help="Show report since specified date"
    ),
    on: Optional[datetime] = typer.Option(
        default=None, help="Show report on specified date"
    ),
):
    migrate_database()
    report(seller, since, on)


@app.command(
    name="reset",
    help="Deletes all financial information from the application",
)
def reset_():
    delete_information = typer.confirm(
        "Are you sure you want to delete all financial information ?"
    )
    if not delete_information:
        raise typer.Abort()

    reset()


@app.command(name="deposit", help="Deposits money into an account")
def deposit_(
    cent_amount: int = typer.Argument(
        0, help="Amount to deposit in cents", metavar="AMOUNT"
    ),
    account_name: str = typer.Argument(
        "", help="Name of the account", metavar='"ACCOUNT NAME"'
    ),
):
    deposit(cent_amount, account_name)


accounts_app = typer.Typer()
app.add_typer(accounts_app, name="accounts", help="Handles accounts")


@accounts_app.command(name="show", help="Shows existing accounts")
def show():
    show_accounts(typer.echo)


@accounts_app.command(name="open", help="Opens a new account")
def open_(
    name: str = typer.Argument(
        "", help="Name of the account", metavar='"ACCOUNT NAME"'
    ),
):
    open_account(name)


@accounts_app.command(name="close", help="Closes an account")
def close_(
    name: str = typer.Argument(
        "", help="Name of the account", metavar='"ACCOUNT NAME"'
    ),
):
    close_account(name)

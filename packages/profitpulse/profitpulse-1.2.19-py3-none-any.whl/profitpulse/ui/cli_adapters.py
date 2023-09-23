"""
Cli adapters bridge the CLI with the application use cases.
"""

import site
from pathlib import Path

from toolcat.database import Database, Session

from profitpulse.account_name import AccountName
from profitpulse.application.close_account import CloseAccountService
from profitpulse.application.deposit_into_account import ServiceDepositIntoAccount
from profitpulse.application.import_transactions import ServiceImportTransactions
from profitpulse.application.open_account import OpenAccountService
from profitpulse.application.repositories.accounts import Accounts
from profitpulse.application.repositories.transactions import Transactions
from profitpulse.application.views.accounts import AccountsView
from profitpulse.application.views.transactions import ViewTransactions
from profitpulse.infrastructure.gateway_cgd_file import GatewayCGDFile
from profitpulse.money import Money

database_path = Path.home() / Path("Library/Application Support/Profitpulse")


def report(seller, since, on):
    with Session(Database(database_path).engine) as session:
        view = ViewTransactions(session, seller, since, on)

    transactions, total = view.data
    if not seller:
        if not transactions:
            print("Could not find any transactions!")
            return

        for t in transactions:
            print(f"Description: '{t['description']:>22}', Value: {t['value']:>10}")
        return

    print(f"Description: '{seller}', Value: {round(total, 2)}")


def migrate_database():
    try:
        site_packages_path = site.getsitepackages()[
            0
        ]  # .pyenv/versions/3.11.2/lib/python3.11/site-packages
        d = Database(
            database_path,
            Path(f"{site_packages_path}/profitpulse/migrations/0001 - Initial.sql"),
        )
        d.run_sql_file(
            Path(f"{site_packages_path}/profitpulse/migrations/0002 - accounts.sql")
        )
    except FileNotFoundError:
        # temporary hack for when running in dev mode
        d = Database(database_path, Path("migrations/0001 - Initial.sql"))
        d.run_sql_file(Path("migrations/0002 - accounts.sql"))


def reset():
    db = Database(database_path)
    db.remove()


def import_file(file_path: Path):
    with Session(Database(database_path).engine) as session:
        gateway_cgd = GatewayCGDFile(file_path)
        transactions = Transactions(session)
        ServiceImportTransactions(gateway_cgd, transactions).execute()
        session.commit()


class DepositRequest:
    def __init__(self, cent_amount, account_name):
        self._cent_amount = cent_amount
        self._account_name = account_name

    @property
    def amount(self) -> Money:
        return Money(self._cent_amount)

    @property
    def account_name(self) -> AccountName:
        return self._account_name


def deposit(cent_amount: int, account_name: str) -> None:
    with Session(Database(database_path).engine) as session:
        accounts = Accounts(session)
        request = DepositRequest(cent_amount, account_name)
        service = ServiceDepositIntoAccount(accounts)
        service.execute(request)

        session.commit()


def show_accounts(printer):
    with Session(Database(database_path).engine) as session:
        data = AccountsView(session).data
        if not data:
            print("No accounts found")
            return
        for i in data:
            printer(f"{i['name']}: {i['balance']} €")


class OpenAccountRequest:
    def __init__(self, name):
        self._name = AccountName(name)

    @property
    def account_name(self):
        return self._name


def open_account(name):
    with Session(Database(database_path).engine) as session:
        accounts = Accounts(session)
        request = OpenAccountRequest(name)
        OpenAccountService(accounts).execute(request)
        session.commit()


class CloseAccountRequest:
    def __init__(self, account_name):
        self._account_name = account_name

    @property
    def account_name(self) -> AccountName:
        return AccountName(self._account_name)


def close_account(name):
    with Session(Database(database_path).engine) as session:
        accounts = Accounts(session)
        request = CloseAccountRequest(name)
        CloseAccountService(accounts).execute(request)
        session.commit()

import typing

from profitpulse.account import Account
from profitpulse.account_name import AccountName
from profitpulse.money import Money


class AccountDoesNotExistError(Exception):
    def __str__(self) -> str:
        return "Account does not exist"


class Accounts(typing.Protocol):
    def __getitem__(self, account_name: AccountName) -> Account:
        ...

    def __setitem__(self, account_name: AccountName, account: Account):
        ...


class DepositIntoAccountRequest(typing.Protocol):
    @property
    def account_name(self) -> AccountName:
        ...

    @property
    def amount(self) -> Money:
        ...


class ServiceDepositIntoAccount:
    def __init__(self, accounts: Accounts):
        self._accounts = accounts

    def execute(self, request: DepositIntoAccountRequest):
        try:
            account = self._accounts[request.account_name]
        except KeyError:
            raise AccountDoesNotExistError()

        account.deposit(request.amount)

        self._accounts[request.account_name] = account

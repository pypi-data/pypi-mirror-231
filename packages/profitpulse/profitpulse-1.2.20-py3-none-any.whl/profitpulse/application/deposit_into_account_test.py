import pytest

from profitpulse.account import Account
from profitpulse.account_name import AccountName
from profitpulse.application.deposit_into_account import (
    AccountDoesNotExistError,
    ServiceDepositIntoAccount,
)
from profitpulse.money import Money


class AccountsNoAccount:
    def __getitem__(self, account_name):
        raise KeyError

    def __setitem__(self, account_name, account):
        pass


class DepositInAccountRequest:
    @property
    def account_name(self) -> AccountName:
        return AccountName("TheAccountName")

    @property
    def amount(self) -> Money:
        return Money(100)


def test_raise_error_if_account_does_not_exist():
    request = DepositInAccountRequest()
    accounts = AccountsNoAccount()

    service = ServiceDepositIntoAccount(accounts)
    with pytest.raises(AccountDoesNotExistError, match="Account does not exist"):
        service.execute(request)


class Accounts:
    def __init__(self, account: Account) -> None:
        self._account = account
        self.account_added = False

    def __getitem__(self, account_name) -> Account:
        return self._account

    def __setitem__(self, account_name, account: Account):
        self.account_added = True
        self._account = account


def test_save_deposit_into_account():
    request = DepositInAccountRequest()
    account = Account(AccountName("TheAccountName"))
    accounts = Accounts(account)

    service = ServiceDepositIntoAccount(accounts)

    service.execute(request)

    assert accounts.account_added  # nosec

import pytest

from profitpulse.account import Account
from profitpulse.account_name import AccountName
from profitpulse.application.repositories.accounts import Accounts
from profitpulse.money import Money
from testrig.scenario import DatabaseScenario


@pytest.mark.integration
def test_return_none_when_account_not_found(tmp_db_session):
    accounts = Accounts(tmp_db_session)
    assert accounts.get(AccountName("TheAccountName")) is None  # nosec


@pytest.mark.integration
def test_return_account_when_one_exists(tmp_db_session):
    DatabaseScenario(tmp_db_session).open_account(name="TheAccountName")
    accounts = Accounts(tmp_db_session)

    account = accounts.get(AccountName("TheAccountName"))

    assert isinstance(account, Account)  # nosec
    assert account._account_name == AccountName("TheAccountName")  # nosec


@pytest.mark.integration
def test_set_account(tmp_db_session):
    account = Account(AccountName("TheAccountName"))
    accounts = Accounts(tmp_db_session)

    accounts[account.name] = account


@pytest.mark.integration
def test_save_account_balance(tmp_db_session):
    balance = Money(10)
    account_name = AccountName("TheAccountName")
    account = Account(account_name=account_name, balance=balance)
    accounts = Accounts(tmp_db_session)

    accounts[account.name] = account

    account = accounts.get(account_name)
    assert account is not None  # nosec
    assert account.balance == balance  # nosec

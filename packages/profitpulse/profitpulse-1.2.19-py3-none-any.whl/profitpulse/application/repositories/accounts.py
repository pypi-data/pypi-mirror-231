from typing import Optional

from toolcat.database import text

from profitpulse.account import Account
from profitpulse.account_name import AccountName
from profitpulse.money import Money


class Accounts:
    """
    Accounts implement the AccountsRepository protocol.
    """

    def __init__(self, session):
        self._session = session

    def get(self, account_name: AccountName) -> Optional[Account]:
        try:
            return self[account_name]
        except KeyError:
            return None

    def __setitem__(self, account_name: AccountName, account: Account):
        sql_stmt = """
            INSERT OR REPLACE INTO account (name)
                 VALUES (:name)
        """
        prepared_statement = text(sql_stmt)
        prepared_statement = prepared_statement.bindparams(name=str(account.name))
        self._session.execute(prepared_statement)

        sql_stmt = """
            INSERT INTO balance (account_id, value)
                 VALUES ((SELECT id FROM account WHERE name = :name), :value)
        """
        prepared_statement = text(sql_stmt)
        prepared_statement = prepared_statement.bindparams(
            name=str(account.name), value=str(account.balance.cents)
        )
        self._session.execute(prepared_statement)

    def append(self, account: Account):
        self[account.name] = account

    def __getitem__(self, account_name: AccountName) -> Account:
        sql_stmt = """
            SELECT account.name as name,
                   COALESCE(balance.value, 0) as balance
              FROM account
         LEFT JOIN balance
                ON account.id = balance.account_id
             WHERE account.name = :name
        """
        prepared_statement = text(sql_stmt)
        prepared_statement = prepared_statement.bindparams(name=str(account_name))
        row = self._session.execute(prepared_statement).first()
        if not row:
            raise KeyError

        return Account(AccountName(row[0]), balance=Money(row[1]))

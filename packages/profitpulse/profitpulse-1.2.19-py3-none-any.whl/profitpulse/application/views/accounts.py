from toolcat.database import text

from profitpulse.application.views.views import View
from profitpulse.money import Money


class AccountsView(View):
    def __init__(self, session) -> None:
        self._session = session

    @property
    def data(self):
        sql_stmt = """
          SELECT account.name as name,
                 COALESCE(balance.value , 0) as balance
            FROM account
       LEFT JOIN balance
              ON account.id = balance.account_id
        """
        rows = self._session.execute(text(sql_stmt))

        return [{"name": row[0], "balance": Money(row[1])} for row in rows]

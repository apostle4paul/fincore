from app.models.account import account
from app.repositories.base_repository import BaseRepository


class AccountRepository(BaseRepository):

    def __init__(self, file_path="data/accounts.json"):

        super().__init__(file_path)

    # Get all accounts
    def get_all(self):

        data = self._read_data()

        accounts = []

        for item in data:

            account = Account.from_dict(item)

            accounts.append(account)

        return accounts

    # Get account by account number
    def get_by_number(self, account_number):

        accounts = self.get_all()

        for account in accounts:

            if account.account_number == account_number:

                return account

        return None

    # Save a new account
    def save(self, account):

        data = self._read_data()

        data.append(account.to_dict())

        self._write_data(data)

        return account

    # Update an existing account
    def update(self, account):

        data = self._read_data()

        for i in range(len(data)):

            if data[i]["account_number"] == account.account_number:

                data[i] = account.to_dict()

                self._write_data(data)

                return account

        return None
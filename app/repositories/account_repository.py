from app.models.account import Account
from app.repositories.base_repository import BaseRepository


class AccountRepository(BaseRepository):

    def __init__(
        self,
        file_path="data/accounts.json"
    ):
        super().__init__(file_path)

    def get_all(self):
        data = self._read_data()

        accounts = []

        for item in data:
            account = Account.from_dict(item)
            accounts.append(account)

        return accounts

    def get_by_number(self, account_number):

        accounts = self.get_all()

        for account in accounts:
            if account.account_number == account_number:
                return account

        return None

    def get_by_member_id(self, member_id):

        accounts = self.get_all()

        member_accounts = []

        for account in accounts:
            if account.member_id == member_id:
                member_accounts.append(account)

        return member_accounts

    def save(self, account):

        data = self._read_data()

        data.append(account.to_dict())

        self._write_data(data)

        return account

    def update(self, updated_account):

        data = self._read_data()

        for index, item in enumerate(data):

            if (
                item["account_number"]
                == updated_account.account_number
            ):
                data[index] = updated_account.to_dict()

                self._write_data(data)

                return updated_account

        return None
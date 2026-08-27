from app.models.transaction import Transaction
from app.repositories.base_repository import BaseRepository


class TransactionRepository(BaseRepository):

    def __init__(
        self,
        file_path="data/transactions.json"
    ):
        super().__init__(file_path)

    def get_all(self):

        data = self._read_data()

        return [
            Transaction.from_dict(item)
            for item in data
        ]

    def get_by_id(self, transaction_id):

        for transaction in self.get_all():

            if transaction.transaction_id == transaction_id:
                return transaction

        return None

    def get_by_account(self, account_number):

        return [
            transaction
            for transaction in self.get_all()
            if transaction.account_number == account_number
        ]

    def save(self, transaction):

        data = self._read_data()

        data.append(
            transaction.to_dict()
        )

        self._write_data(data)

        return transaction
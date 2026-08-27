from app.models.transaction import Transaction
from app.repositories.base_repository import BaseRepository


class TransactionRepository(BaseRepository):

    def __init__(self, file_path="data/transactions.json"):

        super().__init__(file_path)

    # Get all transactions
    def get_all(self):

        data = self._read_data()

        transactions = []

        for item in data:

            transaction = Transaction.from_dict(item)

            transactions.append(transaction)

        return transactions

    # Get transaction by ID
    def get_by_id(self, transaction_id):

        transactions = self.get_all()

        for transaction in transactions:

            if transaction.transaction_id == transaction_id:

                return transaction

        return None

    # Get transactions for an account
    def get_by_account(self, account_number):

        transactions = self.get_all()

        account_transactions = []

        for transaction in transactions:

            if transaction.account_number == account_number:

                account_transactions.append(transaction)

        return account_transactions

    # Save a new transaction
    def save(self, transaction):

        data = self._read_data()

        data.append(transaction.to_dict())

        self._write_data(data)

        return transaction
from app.exceptions import (
    AccountNotFoundError,
    InvalidTransactionError,
    TransactionNotFoundError,
    InsufficientBalanceError,
)

from app.models.transaction import Transaction
from app.repositories.account_repository import AccountRepository
from app.repositories.transaction_repository import TransactionRepository
from app.utils.id_generator import generate_id
from app.utils.money import validate_amount


class TransactionService:

    def __init__(self, transaction_repository=None, account_repository=None):
        self.transaction_repository = transaction_repository or TransactionRepository()
        self.account_repository = account_repository or AccountRepository()

    def _get_account(self, account_number: str):

        account = self.account_repository.get_by_number(account_number)

        if account is None:
            raise AccountNotFoundError(
                f"Account {account_number} was not found."
            )

        return account

    def _generate_transaction_id(self):

        transactions = self.transaction_repository.get_all()

        existing_ids = []

        for transaction in transactions:
            existing_ids.append(transaction.transaction_id)

        return generate_id("T", existing_ids)

    def deposit(
        self,
        account_number: str,
        amount: float,
        description: str = "Deposit",
    ) -> Transaction:

        account = self._get_account(account_number)

        if account.status != "ACTIVE":
            raise InvalidTransactionError(
                "Cannot deposit into an inactive account."
            )

        try:
            amount = validate_amount(amount)
        except ValueError as error:
            raise InvalidTransactionError(str(error))

        account.balance += amount

        self.account_repository.update(account)

        transaction = Transaction(
            transaction_id=self._generate_transaction_id(),
            account_number=account_number,
            transaction_type="DEPOSIT",
            amount=amount,
            balance_after=account.balance,
            description=description,
        )

        return self.transaction_repository.save(transaction)

    def withdraw(
        self,
        account_number: str,
        amount: float,
        description: str = "Withdrawal",
    ) -> Transaction:

        account = self._get_account(account_number)

        if account.status != "ACTIVE":
            raise InvalidTransactionError(
                "Cannot withdraw from an inactive account."
            )

        try:
            amount = validate_amount(amount)
        except ValueError as error:
            raise InvalidTransactionError(str(error))

        if amount > account.balance:
            raise InsufficientBalanceError("Insufficient balance.")

        account.balance -= amount

        self.account_repository.update(account)

        transaction = Transaction(
            transaction_id=self._generate_transaction_id(),
            account_number=account_number,
            transaction_type="WITHDRAWAL",
            amount=amount,
            balance_after=account.balance,
            description=description,
        )

        return self.transaction_repository.save(transaction)

    def get_transaction(self, transaction_id: str) -> Transaction:

        transaction = self.transaction_repository.get_by_id(transaction_id)

        if transaction is None:
            raise TransactionNotFoundError(
                f"Transaction {transaction_id} was not found."
            )

        return transaction

    def get_account_transactions(self, account_number: str) -> list[Transaction]:

        self._get_account(account_number)

        return self.transaction_repository.get_by_account(account_number)

    def list_transactions(self) -> list[Transaction]:

        return self.transaction_repository.get_all()

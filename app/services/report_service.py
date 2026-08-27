from app.repositories.member_repository import MemberRepository
from app.repositories.transaction_repository import TransactionRepository
from app.repositories.account_repository import AccountRepository


class ReportService:

    def __init__(
        self,
        member_repository=None,
        transaction_repository=None,
        account_repository=None,
    ):

        self.member_repository = (
            member_repository or MemberRepository()
        )

        self.transaction_repository = (
            transaction_repository or TransactionRepository()
        )

        self.account_repository = (
            account_repository or AccountRepository()
        )

    def member_report(self):

        members = self.member_repository.get_all()

        total_members = len(members)

        active_members = 0
        inactive_members = 0

        for member in members:

            if member.status == "ACTIVE":
                active_members += 1

            elif member.status == "INACTIVE":
                inactive_members += 1

        return {
            "total_members": total_members,
            "active_members": active_members,
            "inactive_members": inactive_members,
        }

    def transaction_report(self):

        transactions = (
            self.transaction_repository.get_all()
        )

        total_transactions = len(transactions)

        total_deposits = 0
        total_withdrawals = 0

        deposit_count = 0
        withdrawal_count = 0

        for transaction in transactions:

            if transaction.transaction_type == "DEPOSIT":

                total_deposits += transaction.amount
                deposit_count += 1

            elif transaction.transaction_type == "WITHDRAWAL":

                total_withdrawals += transaction.amount
                withdrawal_count += 1

        return {
            "total_transactions": total_transactions,
            "total_deposits": total_deposits,
            "total_withdrawals": total_withdrawals,
            "deposit_count": deposit_count,
            "withdrawal_count": withdrawal_count,
        }

    def account_report(self):

        accounts = self.account_repository.get_all()

        total_accounts = len(accounts)

        active_accounts = 0
        inactive_accounts = 0

        total_balance = 0

        for account in accounts:

            total_balance += account.balance

            if account.status == "ACTIVE":
                active_accounts += 1

            elif account.status == "INACTIVE":
                inactive_accounts += 1

        return {
            "total_accounts": total_accounts,
            "active_accounts": active_accounts,
            "inactive_accounts": inactive_accounts,
            "total_balance": total_balance,
        }



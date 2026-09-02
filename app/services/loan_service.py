from app.models.loan import PersonalLoan, BusinessLoan
from app.repositories.loan_repository import LoanRepository
from app.repositories.account_repository import AccountRepository
from app.repositories.member_repository import MemberRepository
from app.services.transaction_service import TransactionService
from app.utils.id_generator import generate_id


class LoanService:

    def __init__(
        self,
        loan_repository=None,
        account_repository=None,
        member_repository=None
    ):
        self.loan_repository = (
            loan_repository or LoanRepository()
        )

        self.account_repository = (
            account_repository or AccountRepository()
        )

        self.member_repository = (
            member_repository or MemberRepository()
        )

        self.transaction_service = TransactionService(
            account_repository=self.account_repository
        )

    # 1. Apply for loan + 2. Check eligibility
    def apply_loan(
        self,
        member_id,
        account_number,
        loan_type,
        amount,
        duration
    ):

        member = self.member_repository.get_by_id(
            member_id.upper()
        )

        if member is None:
            raise ValueError("Member does not exist.")

        account = self.account_repository.get_by_number(
            account_number.upper()
        )

        if account is None:
            raise ValueError("Account does not exist.")

        if account.balance < 5000:
            raise ValueError(
                "You need at least 5,000 ETB to apply for a loan."
            )

        if amount <= 0:
            raise ValueError("Loan amount must be positive.")

        if duration <= 0:
            raise ValueError("Duration must be greater than zero.")

        loan_type = loan_type.upper()

        loans = self.loan_repository.get_all()

        loan_ids = [loan.loan_id for loan in loans]

        loan_id = generate_id("L", loan_ids)

        if loan_type == "PERSONAL":
            loan = PersonalLoan(
                loan_id,
                member_id,
                account.account_number,
                amount,
                duration
            )

        elif loan_type == "BUSINESS":
            loan = BusinessLoan(
                loan_id,
                member_id,
                account.account_number,
                amount,
                duration
            )

        else:
            raise ValueError(
                "Loan type must be PERSONAL or BUSINESS."
            )

        return self.loan_repository.save(loan)

    
    def approve_loan(self, loan_id):

        loan = self.loan_repository.get_by_id(
            loan_id.upper()
        )

        if loan is None:
            raise ValueError("Loan not found.")

        if loan.status != "PENDING":
            raise ValueError("Loan is no longer pending.")

        self.transaction_service.deposit(
            loan.account_number,
            loan.amount,
            "Loan approved"
        )

        loan.status = "APPROVED"

        return self.loan_repository.update(loan)

    
    def reject_loan(self, loan_id):

        loan = self.loan_repository.get_by_id(
            loan_id.upper()
        )

        if loan is None:
            raise ValueError("Loan not found.")

        if loan.status != "PENDING":
            raise ValueError("Loan is no longer pending.")

        loan.status = "REJECTED"

        return self.loan_repository.update(loan)

    
    def get_loan(self, loan_id):

        loan = self.loan_repository.get_by_id(
            loan_id.upper()
        )

        if loan is None:
            raise ValueError("Loan not found.")

        return loan

    
    def make_payment(self, loan_id, amount):

        loan = self.get_loan(loan_id)

        if loan.status != "APPROVED":
            raise ValueError("Loan is not active.")

        if amount <= 0:
            raise ValueError("Payment must be positive.")

        remaining = loan.remaining_balance()

        if amount > remaining:
            amount = remaining

        self.transaction_service.withdraw(
            loan.account_number,
            amount,
            "Loan payment"
        )

        loan.amount_paid += amount

        if loan.amount_paid >= loan.total_repayment():
            loan.amount_paid = loan.total_repayment()
            loan.status = "PAID"

        return self.loan_repository.update(loan)

    # 6. View loans
    def list_loans(self):
        return self.loan_repository.get_all()

    def get_account_loans(self, account_number):
        return self.loan_repository.get_by_account(
            account_number.upper()
        )
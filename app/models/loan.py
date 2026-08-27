class Loan:

    def __init__(
        self,
        loan_id,
        borrower,
        account_number,
        loan_type,
        amount,
        interest_rate,
        duration,
        status="PENDING",
        amount_paid=0.0
    ):
        self.loan_id = loan_id
        self.borrower = borrower
        self.account_number = account_number
        self.loan_type = loan_type
        self.amount = float(amount)
        self.interest_rate = interest_rate
        self.duration = duration
        self.status = status
        self.amount_paid = float(amount_paid)

    def calculate_interest(self):
        return self.amount * self.interest_rate

    def total_repayment(self):
        return self.amount + self.calculate_interest()

    def monthly_payment(self):
        return self.total_repayment() / self.duration

    def remaining_balance(self):
        return self.total_repayment() - self.amount_paid

    def to_dict(self):
        return {
            "loan_id": self.loan_id,
            "borrower": self.borrower,
            "account_number": self.account_number,
            "loan_type": self.loan_type,
            "amount": self.amount,
            "interest_rate": self.interest_rate,
            "duration": self.duration,
            "status": self.status,
            "amount_paid": self.amount_paid
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            loan_id=data["loan_id"],
            borrower=data["borrower"],
            account_number=data["account_number"],
            loan_type=data["loan_type"],
            amount=data["amount"],
            interest_rate=data["interest_rate"],
            duration=data["duration"],
            status=data.get("status", "PENDING"),
            amount_paid=data.get("amount_paid", 0.0)
        )


class PersonalLoan(Loan):

    def __init__(
        self,
        loan_id,
        borrower,
        account_number,
        amount,
        duration
    ):
        super().__init__(
            loan_id,
            borrower,
            account_number,
            "PERSONAL",
            amount,
            0.10,
            duration
        )


class BusinessLoan(Loan):

    def __init__(
        self,
        loan_id,
        borrower,
        account_number,
        amount,
        duration
    ):
        super().__init__(
            loan_id,
            borrower,
            account_number,
            "BUSINESS",
            amount,
            0.08,
            duration
        )
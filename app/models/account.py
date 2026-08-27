from datetime import date


class Account:

    def __init__(
        self,
        account_number,
        member_id,
        account_type="SAVINGS",
        balance=0.0,
        status="ACTIVE",
        date_opened=None
    ):
        self.account_number = account_number
        self.member_id = member_id
        self.account_type = account_type
        self.balance = float(balance)
        self.status = status
        self.date_opened = (
            date_opened
            if date_opened
            else date.today().isoformat()
        )

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "member_id": self.member_id,
            "account_type": self.account_type,
            "balance": self.balance,
            "status": self.status,
            "date_opened": self.date_opened
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            account_number=data["account_number"],
            member_id=data["member_id"],
            account_type=data.get(
                "account_type",
                "SAVINGS"
            ),
            balance=data.get(
                "balance",
                0.0
            ),
            status=data.get(
                "status",
                "ACTIVE"
            ),
            date_opened=data.get(
                "date_opened"
            )
        )

    def __str__(self):
        return (
            f"Account Number: {self.account_number}\n"
            f"Member ID: {self.member_id}\n"
            f"Account Type: {self.account_type}\n"
            f"Balance: {self.balance:.2f}\n"
            f"Status: {self.status}\n"
            f"Date Opened: {self.date_opened}"
        )
from datetime import datetime

class Transaction:

    def __init__(

            self,
            transaction_id:str,
            account_number:str,
            transaction_type:str,
            amount:float,
            balance_after:float,
            desciption: str= "",
            timestamp: str | None=None,
            status:str = "COMPLETED",
    ):
        self.transaction_id=transaction_id
        self.account_number=account_number
        self.transaction_type=transaction_type
        self.amount=amount
        self.balance_after=balance_after
        self.description=desciption
        self.timestamp=(
            timestamp
            or datetime.now().isoformat(
                timespec="seconds"
            )
        )
        self.status=status

    def to_dict(self) -> dict:
        return {
            "transaction_id": self.transaction_id,
            "account_number": self.account_number,
            "transaction_type": self.transaction_type,
            "amount": self.amount,
            "balance_after": self.balance_after,
            "description": self.description,
            "timestamp": self.timestamp,
            "status": self.status,
        }
    @classmethod

    def from_dict(cls, data:dict):
        return cls(
            transaction_id=data["transaction_id"],
            account_number=data["account_number"],
            transaction_type=data["transaction_type"],
            amount=data["amount"],
            balance_after=data["balance_after"],
            description=data.get(
                "description",
                ""
            ),
            timestamp=data.get("timestamp"),
            status=data.get(
                "status",
                "COMPLETED"
            ),
        )
    def __str__(self):
        return (
            f"Transaction ID: {self.transaction_id}\n"
            f"Account Number: {self.account_number}\n"
            f"Type: {self.transaction_type}\n"
            f"Amount: {self.amount:.2f}\n"
            f"Balance After: {self.balance_after:.2f}\n"
            f"Description: {self.description}\n"
            f"Timestamp: {self.timestamp}\n"
            f"Status: {self.status}"
        )
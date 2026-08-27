from app.models.loan import Loan
from app.repositories.base_repository import BaseRepository


class LoanRepository(BaseRepository):

    def __init__(self, file_path="data/loans.json"):
        super().__init__(file_path)

    def get_all(self):
        return [
            Loan.from_dict(item)
            for item in self._read_data()
        ]

    def get_by_id(self, loan_id):
        for loan in self.get_all():
            if loan.loan_id == loan_id:
                return loan

        return None

    def get_by_account(self, account_number):
        return [
            loan
            for loan in self.get_all()
            if loan.account_number == account_number
        ]

    def save(self, loan):
        data = self._read_data()
        data.append(loan.to_dict())
        self._write_data(data)
        return loan

    def update(self, loan):
        data = self._read_data()

        for i, item in enumerate(data):
            if item["loan_id"] == loan.loan_id:
                data[i] = loan.to_dict()
                self._write_data(data)
                return loan

        return None
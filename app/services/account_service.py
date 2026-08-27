from app.models.account import Account

from app.repositories.account_repository import (
    AccountRepository
)

from app.repositories.member_repository import (
    MemberRepository
)

from app.utils.id_generator import generate_id

from app.exceptions import (
    AccountNotFoundError,
    InvalidAccountDataError,
    MemberNotFoundForAccountError
)


class AccountService:

    def __init__(
        self,
        account_repository=None,
        member_repository=None
    ):

        self.account_repository = (
            account_repository
            or AccountRepository()
        )

        self.member_repository = (
            member_repository
            or MemberRepository()
        )

    def open_account(
        self,
        member_id,
        account_type="SAVINGS"
    ):

        member_id = member_id.strip().upper()

        member = self.member_repository.get_by_id(
            member_id
        )

        if member is None:
            raise MemberNotFoundForAccountError(
                f"Member {member_id} does not exist."
            )

        account_type = account_type.upper()

        if account_type != "SAVINGS":
            raise InvalidAccountDataError(
                "Only SAVINGS accounts are supported."
            )

        accounts = self.account_repository.get_all()

        existing_ids = [
            account.account_number
            for account in accounts
        ]

        account_number = generate_id(
            "A",
            existing_ids
        )

        account = Account(
            account_number=account_number,
            member_id=member_id,
            account_type=account_type
        )

        return self.account_repository.save(
            account
        )

    def get_account(
        self,
        account_number
    ):

        account_number = account_number.strip().upper()

        account = self.account_repository.get_by_number(
            account_number
        )

        if account is None:
            raise AccountNotFoundError(
                f"Account {account_number} was not found."
            )

        return account

    def get_member_accounts(
        self,
        member_id
    ):

        member_id = member_id.strip().upper()

        member = self.member_repository.get_by_id(
            member_id
        )

        if member is None:
            raise MemberNotFoundForAccountError(
                f"Member {member_id} does not exist."
            )

        return self.account_repository.get_by_member_id(
            member_id
        )

    def close_account(
        self,
        account_number
    ):

        account = self.get_account(
            account_number
        )

        if account.status != "ACTIVE":
            raise InvalidAccountDataError(
                "Account is already inactive."
            )

        if account.balance != 0:
            raise InvalidAccountDataError(
                "Account balance must be zero "
                "before closing the account."
            )

        account.status = "INACTIVE"

        return self.account_repository.update(
            account
        )

    def list_accounts(self):

        return self.account_repository.get_all()
class FinCoreError(Exception):
    """Base exception for FinCore."""

class MemberNotFoundError(FinCoreError):
    """Raised when a membeer cannot be found."""

class DuplicateMemberError(FinCoreError):
    """Raised when a number already exists."""

class InvalidMemberDataError(FinCoreError):
    """Raised when member data is invalid."""

class TransactionNotFoundError(FinCoreError):
    """Raised when a transaction cannot be found."""


class InvalidTransactionError(FinCoreError):
    """Raised when transaction data is invalid."""

class AccountNotFoundError(FinCoreError):
    pass

class DuplicateAccountError(FinCoreError):
    """Raised when an account number already exists."""
    pass

class InvalidAccountDataError(FinCoreError):
    pass


class InsufficientBalanceError(FinCoreError):
    pass


class MemberNotFoundForAccountError(FinCoreError):
    pass
class FinCoreError(Exception):
    """Base exception for FinCore."""

class MemberNotFoundError(FinCoreError):
    """Raised when a membeer cannot be found."""

class DuplicateMemberError(FinCoreError):
    """Raised when a number already exists."""

class InvalidMemberDataError(FinCoreError):
    """Raised when member data is invalid."""
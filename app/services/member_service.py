from app.exceptions import (
    DuplicateMemberError,
    InvalidMemberDataError,
    MemberNotFoundError
)

from app.models.member import Member
from app.repositories.member_repository import MemberRepository
from app.utils.id_generator import generate_id


from app.utils.validators import (
    validate_email,
    validate_name,
    validate_phone
)
class MemberService:

    def __init__(self, repository=None):
        self.repository = repository or MemberRepository()

    def register_member(self, full_name, phone, email):

        # Validate the information
        full_name = validate_name(full_name)
        phone = validate_phone(phone)
        email = validate_email(email)

        # Check if phone already exists
        if self.repository.get_by_phone(phone):
            raise DuplicateMemberError(
                "member with this phone number already exists."
            )

        # Get existing IDs
        members = self.repository.get_all()
        existing_ids = []

        for member in members:
            existing_ids.append(member.member_id)

        # Create new ID
        member_id = generate_id("M", existing_ids)

        # Create member
        member = Member(
            member_id,
            full_name,
            phone,
            email
        )

        # Save member
        return self.repository.save(member)

    def get_member(self, member_id):

        member = self.repository.get_by_id(member_id)

        if member is None:
            raise MemberNotFoundError(
                "Member was not found."
            )

        return member

    def search_member(self, search_term):

        search_term = search_term.strip().lower()

        if search_term == "":
            raise InvalidMemberDataError(
                "Search term cannot be empty."
            )

        members = self.repository.get_all()
        results = []

        for member in members:
            if (
                search_term in member.member_id.lower()
                or search_term in member.full_name.lower()
                or search_term in member.phone
                or search_term in member.email.lower()
            ):
                results.append(member)

        return results

    def update_member(self, member_id, full_name, phone, email):

        # first check if the  member exists
        member = self.get_member(member_id)

        # Validate the new information
        full_name = validate_name(full_name)
        phone = validate_phone(phone)
        email = validate_email(email)

        # Check phone belongs to another member
        existing_member = self.repository.get_by_phone(phone)

        if existing_member and existing_member.member_id != member_id:
            raise DuplicateMemberError(
                "This phone number is already registered."
            )

        # Update member
        member.full_name = full_name
        member.phone = phone
        member.email = email

        return self.repository.update(member)

    def deactivate_member(self, member_id):

        member = self.get_member(member_id)

        if member.status == "INACTIVE":
            raise InvalidMemberDataError(
                "Member is already inactive."
            )

        member.status = "INACTIVE"

        return self.repository.update(member)

    def list_members(self):
        return self.repository.get_all()
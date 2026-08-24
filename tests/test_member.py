import pytest

from app.exceptions import (
    DuplicateMemberError,
    MemberNotFoundError,
)

from app.repositories.member_repository import (
    MemberRepository
)

from app.services.member_service import (
    MemberService
)


@pytest.fixture
def member_service(tmp_path):

    file_path = tmp_path / "members.json"

    repository = MemberRepository(
        str(file_path)
    )

    return MemberService(repository)


def test_register_member(member_service):

    member = member_service.register_member(
        full_name="Abebe Kebede",
        phone="0912345678",
        email="abebe@example.com",
    )

    assert member.member_id == "M001"
    assert member.full_name == "Abebe Kebede"
    assert member.status == "ACTIVE"


def test_register_duplicate_phone(
    member_service
):

    member_service.register_member(
        full_name="Abebe Kebede",
        phone="0912345678",
        email="abebe@example.com",
    )

    with pytest.raises(
        DuplicateMemberError
    ):

        member_service.register_member(
            full_name="Another Person",
            phone="0912345678",
            email="another@example.com",
        )


def test_get_member(member_service):

    created = member_service.register_member(
        full_name="Abebe Kebede",
        phone="0912345678",
        email="abebe@example.com",
    )

    found = member_service.get_member(
        created.member_id
    )

    assert found.member_id == created.member_id
    assert found.full_name == "Abebe Kebede"


def test_get_nonexistent_member(
    member_service
):

    with pytest.raises(
        MemberNotFoundError
    ):

        member_service.get_member("M999")


def test_search_member(member_service):

    member_service.register_member(
        full_name="Abebe Kebede",
        phone="0912345678",
        email="abebe@example.com",
    )

    member_service.register_member(
        full_name="Hana Tesfaye",
        phone="0923456789",
        email="hana@example.com",
    )

    results = member_service.search_member(
        "Hana"
    )

    assert len(results) == 1
    assert results[0].full_name == "Hana Tesfaye"


def test_update_member(member_service):

    member = member_service.register_member(
        full_name="Abebe Kebede",
        phone="0912345678",
        email="abebe@example.com",
    )

    updated = member_service.update_member(
        member_id=member.member_id,
        full_name="Abebe Gebre",
        phone="0911111111",
        email="new@example.com",
    )

    assert updated.full_name == "Abebe Gebre"
    assert updated.phone == "0911111111"
    assert updated.email == "new@example.com"


def test_deactivate_member(
    member_service
):

    member = member_service.register_member(
        full_name="Abebe Kebede",
        phone="0912345678",
        email="abebe@example.com",
    )

    deactivated = (
        member_service.deactivate_member(
            member.member_id
        )
    )

    assert deactivated.status == "INACTIVE"
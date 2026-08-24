from app.models.member import Member

from app.repositories.member_repository import (
    MemberRepository
)


def test_repository_save_and_get(
    tmp_path
):

    file_path = tmp_path / "members.json"

    repository = MemberRepository(
        str(file_path)
    )

    member = Member(
        member_id="M001",
        full_name="Abebe Kebede",
        phone="0912345678",
        email="abebe@example.com",
    )

    repository.save(member)

    found = repository.get_by_id("M001")

    assert found is not None
    assert found.member_id == "M001"
    assert found.full_name == "Abebe Kebede"


def test_repository_get_all(
    tmp_path
):

    file_path = tmp_path / "members.json"

    repository = MemberRepository(
        str(file_path)
    )

    member1 = Member(
        member_id="M001",
        full_name="Abebe Kebede",
        phone="0912345678",
        email="abebe@example.com",
    )

    member2 = Member(
        member_id="M002",
        full_name="Hana Tesfaye",
        phone="0923456789",
        email="hana@example.com",
    )

    repository.save(member1)
    repository.save(member2)

    members = repository.get_all()

    assert len(members) == 2
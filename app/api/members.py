from fastapi import APIRouter
from app.services.member_service import MemberService

router = APIRouter()
service = MemberService()


@router.get("/members")
def list_members():
    return [member.to_dict() for member in service.list_members()]


@router.get("/members/{member_id}")
def get_member(member_id: str):
    return service.get_member(member_id).to_dict()


@router.post("/members")
def register_member(data: dict):
    member = service.register_member(
        data["full_name"],
        data["phone"],
        data["email"]
    )

    return member.to_dict()


@router.put("/members/{member_id}")
def update_member(member_id: str, data: dict):
    member = service.update_member(
        member_id,
        data["full_name"],
        data["phone"],
        data["email"]
    )

    return member.to_dict()


@router.put("/members/{member_id}/deactivate")
def deactivate_member(member_id: str):
    member = service.deactivate_member(member_id)

    return member.to_dict()
from fastapi import APIRouter, HTTPException

from app.services.account_service import AccountService


router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)

service = AccountService()


@router.get("")
def get_accounts():

    accounts = service.list_accounts()

    return [
        account.to_dict()
        for account in accounts
    ]


@router.get("/{account_number}")
def get_account(
    account_number: str
):

    try:

        account = service.get_account(
            account_number
        )

        return account.to_dict()

    except Exception as error:

        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.post("")
def open_account(
    data: dict
):

    try:

        member_id = data["member_id"]

        account = service.open_account(
            member_id
        )

        return account.to_dict()

    except KeyError:

        raise HTTPException(
            status_code=400,
            detail="member_id is required."
        )

    except Exception as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.post("/{account_number}/close")
def close_account(
    account_number: str
):

    try:

        account = service.close_account(
            account_number
        )

        return account.to_dict()

    except Exception as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )
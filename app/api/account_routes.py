from fastapi import APIRouter, HTTPException

from app.services.account_service import AccountService


router = APIRouter()
service = AccountService()


@router.get("/accounts")
def get_accounts():
    accounts = service.list_accounts()
    return [account.to_dict() for account in accounts]


@router.get("/accounts/{account_number}")
def get_account(account_number: str):
    try:
        account = service.get_account(account_number)
        return account.to_dict()
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))


@router.post("/accounts")
def open_account(data: dict):
    try:
        account = service.open_account(data["member_id"])
        return account.to_dict()
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.post("/accounts/{account_number}/deposit")
def deposit(account_number: str, data: dict):
    try:
        account = service.deposit(
            account_number,
            float(data["amount"])
        )
        return account.to_dict()
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.post("/accounts/{account_number}/withdraw")
def withdraw(account_number: str, data: dict):
    try:
        account = service.withdraw(
            account_number,
            float(data["amount"])
        )
        return account.to_dict()
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.post("/accounts/{account_number}/close")
def close_account(account_number: str):
    try:
        account = service.close_account(account_number)
        return account.to_dict()
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))
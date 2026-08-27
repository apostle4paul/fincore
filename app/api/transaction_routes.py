from fastapi import APIRouter, HTTPException

from app.services.transaction_service import TransactionService


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

service = TransactionService()


@router.get("")
def list_transactions():

    return [
        transaction.to_dict()
        for transaction in service.list_transactions()
    ]


@router.get("/{transaction_id}")
def get_transaction(transaction_id: str):

    try:
        transaction = service.get_transaction(
            transaction_id.upper()
        )

        return transaction.to_dict()

    except Exception as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.get("/account/{account_number}")
def get_account_transactions(account_number: str):

    try:
        transactions = service.get_account_transactions(
            account_number.upper()
        )

        return [
            transaction.to_dict()
            for transaction in transactions
        ]

    except Exception as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.post("/deposit")
def deposit(data: dict):

    try:

        transaction = service.deposit(
            data["account_number"],
            float(data["amount"]),
            data.get("description", "Deposit")
        )

        return transaction.to_dict()

    except Exception as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.post("/withdraw")
def withdraw(data: dict):

    try:

        transaction = service.withdraw(
            data["account_number"],
            float(data["amount"]),
            data.get("description", "Withdrawal")
        )

        return transaction.to_dict()

    except Exception as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )
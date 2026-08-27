from fastapi import APIRouter, HTTPException

from app.services.loan_service import LoanService


router = APIRouter(
    prefix="/loans",
    tags=["Loans"]
)

service = LoanService()


@router.get("")
def list_loans():

    loans = service.list_loans()

    return [
        loan.to_dict()
        for loan in loans
    ]


@router.get("/{loan_id}")
def get_loan(loan_id: str):

    try:
        loan = service.get_loan(loan_id)

        return loan.to_dict()

    except Exception as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.post("")
def apply_loan(data: dict):

    try:
        loan = service.apply_loan(
            data["member_id"],
            data["account_number"],
            data["loan_type"],
            float(data["amount"]),
            int(data["duration"])
        )

        return loan.to_dict()

    except KeyError as error:
        raise HTTPException(
            status_code=400,
            detail=f"{error.args[0]} is required."
        )

    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.post("/{loan_id}/approve")
def approve_loan(loan_id: str):

    try:
        loan = service.approve_loan(loan_id)

        return loan.to_dict()

    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.post("/{loan_id}/reject")
def reject_loan(loan_id: str):

    try:
        loan = service.reject_loan(loan_id)

        return loan.to_dict()

    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.post("/{loan_id}/payment")
def make_payment(
    loan_id: str,
    data: dict
):

    try:
        amount = float(data["amount"])

        loan = service.make_payment(
            loan_id,
            amount
        )

        return loan.to_dict()

    except KeyError:
        raise HTTPException(
            status_code=400,
            detail="amount is required."
        )

    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )
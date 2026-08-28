from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.members import router as member_router
from app.api.account_routes import router as account_router
from app.api.transaction_routes import router as transaction_router
from app.api.loan_routes import router as loan_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(member_router, prefix="/members")
app.include_router(account_router)
app.include_router(transaction_router)
app.include_router(loan_router)


@app.get("/")
def home():
    return {"message": "FinCore API is running"}


@app.get("/test-loans")
def test_loans():
    return {"message": "Loan route is reachable"}
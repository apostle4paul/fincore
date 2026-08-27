from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.members import router as members_router
from app.api.account_routes import router as accounts_router
from app.api.transaction_routes import router as transactions_router


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(members_router)
app.include_router(accounts_router)
app.include_router(transactions_router)


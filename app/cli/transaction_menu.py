from app.exceptions import FinCoreError
from app.services.transaction_service import TransactionService


transaction_service = TransactionService()


def display_transaction(transaction):
    print("\n" + "-" * 50)
    print(transaction)
    print("-" * 50)


def transaction_menu():

    while True:

        print("\n" + "=" * 50)
        print("            TRANSACTION MANAGEMENT")
        print("=" * 50)

        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. View Transaction")
        print("4. Account Transaction History")
        print("5. List All Transactions")
        print("6. Back")

        choice = input("\nChoose: ").strip()

        try:

            if choice == "1":
                deposit()

            elif choice == "2":
                withdraw()

            elif choice == "3":
                view_transaction()

            elif choice == "4":
                account_history()

            elif choice == "5":
                list_transactions()

            elif choice == "6":
                break

            else:
                print("\nInvalid option.")

        except FinCoreError as error:
            print(f"\nError: {error}")

        except ValueError:
            print("\nError: Please enter a valid number.")


def deposit():

    print("\n========== DEPOSIT ==========")

    account_number = input("Account Number: ").strip().upper()
    amount = float(input("Amount: "))
    description = input("Description: ").strip()

    transaction = transaction_service.deposit(
        account_number=account_number,
        amount=amount,
        description=description or "Deposit"
    )

    print("\nDeposit successful.")
    display_transaction(transaction)


def withdraw():

    print("\n========== WITHDRAW ==========")

    account_number = input("Account Number: ").strip().upper()
    amount = float(input("Amount: "))
    description = input("Description: ").strip()

    transaction = transaction_service.withdraw(
        account_number=account_number,
        amount=amount,
        description=description or "Withdrawal"
    )

    print("\nWithdrawal successful.")
    display_transaction(transaction)


def view_transaction():

    print("\n========== VIEW TRANSACTION ==========")

    transaction_id = input("Transaction ID: ").strip().upper()

    transaction = transaction_service.get_transaction(transaction_id)

    display_transaction(transaction)


def account_history():

    print("\n========== ACCOUNT HISTORY ==========")

    account_number = input("Account Number: ").strip().upper()

    transactions = transaction_service.get_account_transactions(
        account_number
    )

    if not transactions:
        print("\nNo transactions found.")
        return

    for transaction in transactions:
        display_transaction(transaction)


def list_transactions():

    print("\n========== ALL TRANSACTIONS ==========")

    transactions = transaction_service.list_transactions()

    if not transactions:
        print("\nNo transactions found.")
        return

    print(f"\nTotal transactions: {len(transactions)}")

    for transaction in transactions:
        display_transaction(transaction)


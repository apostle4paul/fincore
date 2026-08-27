from app.exceptions import FinCoreError
from app.services.account_service import AccountService


account_service = AccountService()


def display_account(account):

    print("\n" + "-" * 45)
    print(account)
    print("-" * 45)


def account_menu():

    while True:

        print("\n" + "=" * 45)
        print("           SAVINGS ACCOUNT MANAGEMENT")
        print("=" * 45)

        print("1. Open Account")
        print("2. View Account")
        print("3. View Member Accounts")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Close Account")
        print("7. List All Accounts")
        print("8. Back")

        choice = input("\nChoose: ").strip()

        try:

            if choice == "1":
                open_account()

            elif choice == "2":
                view_account()

            elif choice == "3":
                view_member_accounts()

            elif choice == "4":
                deposit()

            elif choice == "5":
                withdraw()

            elif choice == "6":
                close_account()

            elif choice == "7":
                list_accounts()

            elif choice == "8":
                break

            else:
                print("\nInvalid option.")

        except FinCoreError as error:

            print(f"\nError: {error}")

        except ValueError:

            print("\nError: Please enter a valid amount.")


def open_account():

    print("\n========== OPEN SAVINGS ACCOUNT ==========")

    member_id = input(
        "Member ID: "
    ).strip().upper()

    account = account_service.open_account(
        member_id
    )

    print("\nAccount opened successfully.")

    display_account(account)


def view_account():

    print("\n========== VIEW ACCOUNT ==========")

    account_number = input(
        "Account Number: "
    ).strip().upper()

    account = account_service.get_account(
        account_number
    )

    display_account(account)


def view_member_accounts():

    print("\n========== MEMBER ACCOUNTS ==========")

    member_id = input(
        "Member ID: "
    ).strip().upper()

    accounts = account_service.get_member_accounts(
        member_id
    )

    if not accounts:
        print("\nThis member has no accounts.")
        return

    for account in accounts:
        display_account(account)


def deposit():

    print("\n========== DEPOSIT ==========")

    account_number = input(
        "Account Number: "
    ).strip().upper()

    amount = float(
        input("Amount: ")
    )

    account = account_service.deposit(
        account_number,
        amount
    )

    print("\nDeposit successful.")

    display_account(account)


def withdraw():

    print("\n========== WITHDRAW ==========")

    account_number = input(
        "Account Number: "
    ).strip().upper()

    amount = float(
        input("Amount: ")
    )

    account = account_service.withdraw(
        account_number,
        amount
    )

    print("\nWithdrawal successful.")

    display_account(account)


def close_account():

    print("\n========== CLOSE ACCOUNT ==========")

    account_number = input(
        "Account Number: "
    ).strip().upper()

    account = account_service.get_account(
        account_number
    )

    display_account(account)

    confirmation = input(
        "\nClose this account? (y/n): "
    ).strip().lower()

    if confirmation != "y":
        print("\nOperation cancelled.")
        return

    account = account_service.close_account(
        account_number
    )

    print("\nAccount closed successfully.")

    display_account(account)


def list_accounts():

    print("\n========== ALL SAVINGS ACCOUNTS ==========")

    accounts = account_service.list_accounts()

    if not accounts:
        print("\nNo accounts found.")
        return

    print(f"\nTotal accounts: {len(accounts)}")

    for account in accounts:
        display_account(account)
from app.cli.member_menu import member_menu
from app.cli.transaction_menu import transaction_menu
from app.cli.account_menu import account_menu


def main_menu():

    while True:

        print("\n" + "=" * 45)
        print("                 FINCORE")
        print(
            "     Financial Operations & Loan System"
        )
        print("=" * 45)

        print("\n1. Member Management")
        print("2. Savings Accounts")
        print("3. Transactions")
        print("4. Loan Management")
        print("5. Risk Assessment")
        print("6. Reports")
        print("7. Exit")

        choice = input(
            "\nChoose an option: "
        ).strip()

        if choice == "1":

            member_menu()

        elif choice == "2":
          account_menu()

        elif choice == "3":
            transaction_menu()

        elif choice == "4":

            print(
                "\nLoan Management "
            )

        elif choice == "5":

            print(
                "\nRisk Assessment "
            )

        elif choice == "6":

            print(
                "\nReports"
            )

        elif choice == "7":

            print(
                "\nThank you for using FinCore."
            )

            break

        else:

            print(
                "\nInvalid option. "
                "Please try again."
            )
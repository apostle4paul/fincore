class loan:
    def __init__(
            self,
            borrower,
            amount,
            interest_rate,
            duration,
            Account
    ):
        self.borrower = borrower
        self.amount = amount
        self.interest_rate = interest_rate
        self.duration = duration
        self.account = Account
        self.status = "PENDING"
        self.remaining_balance = amount + self.calculate_interest()
    def calculate_interest(self):
        return self.amount * self.interest_rate
    def total_repayment(self):
        return self.amount + self.calculate_interest()
    def monthly_payment(self):
        return self.total_repayment() / self.duration
    def approve(self):
        if self.status != "PENDING":
            print("This loan is no longer pending.")
            return
        self.status = "APPROVED"
        self.account.deposit(self.amount)
        print("\nLoan approved successfully!")
        print(f"Loan amount: {self.amount:.2f} ETB")
    def reject(self):
        if self.status != "PENDING":
            print("This loan is no longer pending.")
            return
        self.status = "REJECTED"
        print("\nLoan rejected.")
    def make_payment(self, amount):
        if self.status != "APPROVED":
            print("Loan is not active.")
            return
        if amount <= 0:
            print("Payment must be positive.")
            return
        if amount > self.remaining_balance:
            amount = self.remaining_balance

        success = self.acount.withdraw(amount)
        if not success:
            print("Payment failed because of insufficient balance.")
            return
        self.remaining_balance -= amount
        print(f"\nPayment of {amount:.2f} ETB made.")
        print(
            f"Remaining loan balance: "
            f"{self.remaining_balance:.2f} ETB"
        )
        if self.remaining_balance == 0:
            self.status = "PAID"
            print("Congratulations! Loan has been fully paid.")
    def display_loan(self):
        print("\n========== LOAN ==========")
        print(f"Borrower: {self.borrower}")
        print(f"Loan Amount: {self.amount:.2f} ETB")
        print(f"Interrest Rate: {self.interest_rate * 100:.2f}%")
        print(f"Duration: {self.duration} months")
        print(
            f"Total Repayment: "
            f"{self.total_repayment():.2f} ETB"
        )
        print(
            f"Monthly Payment: "
            f"{self.monthly_payment():.2f} ETB"
        )
        print(
            f"Remaining Balance: "
            f"{self.remaining_balance:.2f} ETB"
        )
        print(f"Status: {self.status}")
        print("===========================")
# ===========================================
# PERSONAL LOAN
# ===========================================
class PersonalLoan(loan):
    def __init__(
            self,
            borrower,
            amount,
            duration,
            account
    ):
        #Personal loans have 10% interest
        super().__init__(
            borrower,
            amount,
            0.10,
            duration,
            account
        )
# ===========================================
# BUSINESS LOAN
# ===========================================
class BusinessLoan(loan):
    def __init__(
            self,
            borrower,
            amount,
            duration,
            account
    ):
        # Business loans have 8% interest
        super().__init__(
            borrower,
            amount,
            0.08,
            duration,
            account
        )
# ==========================================
# LOAN MANAGER
# ==========================================
class LoanManager:
    def __init__(self):
        self.loans = []
    def add_loan(self, loan):
        self.loans.append(loan)
        print("\nLoan application submitted successfully.")
    def show_loans(self):
        if len(self.loans) == 0:
            print("\nThere are no loans.")
            return
        print("\n========== ALL LOANS ==========")
        for number, loan in enumerate(self.loans, start=1):
            print(
                f"{number}. "
                f"{loan.borrower} - "
                f"{loan.amount:.2f} ETB - "
                f"{loan.status}"
            )
        print("==============================")
    def find_loan(self, borrower):
        for loan in self.loans:
            if loan.borrower.lower() == borrower.lower():
                return loan
        return None
# ============================================
# MAIN FINCORE PROGRAM
# ============================================
def main():
    print("==============================")
    print("        WELCOME TO FINCORE")
    print("==============================")
    # Create customer
    owner = input("Enter your name: ")
    account_number = input(
        "Enter your account number: "
    )
    # Create account
    account = Account(
        owner,
        account_number
    )
    # Create loan manager
    loan_manager = LoanManager()
    while True:
        print("\n")
        print("========== FINCORE ==========")
        print("1. View Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Apply for Personal Loan")
        print("5. Apply for Business Loan")
        print("6. View My Loan")
        print("7. Approve Loan")
        print("8. Reject Loan")
        print("9. Make Loan Payment")
        print("10. View All Loans")
        print("11. Exit")
        print("=============================")

        choice = input("Choose an option: ")
        # ==============================================
        # VIEW ACCOUNT
        # ==============================================
        if choice == "1":
            account.display_account()
        # ==============================================
        # DEPOSIT
        # ==============================================
        elif choice == "2":
            try:
                amount = float(
                    input("Enter amount to deposit: ")
                )
                account.deposit(amount)
            except ValueError:
                print("Please enter a valid number.")
        # ==============================================
        # WITHDRAW
        # ==============================================
        elif choice == "3":
            try:
                amount = float(
                    input("Enter amount to withdraw: ")
                )
                account.withdraw(amount)
            except ValueError:
                print("Please enter a valid number.")
        # ==============================================
        # PERSONAL LOAN
        # ==============================================
        elif choice == "4":
            try:
                amount = float(
                    input("Enter loan amount: ")
                )
                duration = int(
                    input(
                        "Enter duration in months: "
                    )
                )
                # Simple eligibility rule
                if account.balance < 5000:
                    print(
                        "\nYou are not eligible for a loan."
                    )
                    print(
                        "You need at least "
                        "5,000 ETB in your account."
                    )
                else:
                    loan = PersonalLoan(
                        owner,
                        amount,
                        duration,
                        account
                    )
                    loan_manager.add_loan(loan)
                    loan.display_loan()
            except ValueError:
                print(
                    "Please enter valid numbers."
                )
        # =============================================
        # BUSINESS LOAN
        # =============================================
        elif choice == "5":
            try:
                amount = float(
                    input("Enter loan amount: ")
                )
                duration = int(
                    input(
                        "Enter duration in months: "
                    )
                )
                if account.balance < 5000:
                    print(
                        "\nYou are not eligible for a loan."
                    )
                    print(
                        "You need at least"
                        "5,000 ETB in your account."
                    )
                else:
                    loan = BusinessLoan(
                        owner,
                        amount,
                        duration,
                        account
                    )
                    loan_manager.add_loan(loan)
                    loan.display_loan()
            except ValueError:
                print(
                    "Please enter valid numbers."
                )
        # ==============================================
        # VIEW LOAN
        # ==============================================
        elif choice == "6":
            loan = loan_manager.find_loan(owner)
            if loan is None:
                print("\nYou don't have a loan.")
            else:
                loan.display_loan()
        # ==============================================
        # APPROVE LOAN
        # ==============================================
        elif choice == "7":
            loan = loan_manager.find_loan(owner)
            if loan is None:
                print("\nYou don't have a loan.")
            else:
                loan.approve()
        # ==============================================
        # REJECT LOAN
        # ==============================================
        elif choice == "8":
            loan = loan_manager.find_loan(owner)
            if loan is None:
                print("\nYou don't have a loan.")
            else:
                loan.reject()
        # ==============================================
        # MAKE PAYMENT
        # ==============================================
        elif choice == "9":
            loan = loan_manager.find_loan(owner)
            if loan is None:
                print("\nYou don't have a loan.")
            else:
                try:
                    amount = float(
                        input(
                            "Enter payment amount: "
                        )
                    )
                    loan.make_payment(amount)
                except ValueError:
                    print(
                        "Please enter a valid number."
                    )
        # ===============================================
        # SHOW ALL LOANS
        # ===============================================
        elif choice == "10":
            loan_manager.show_loans()
        # ===============================================
        # EXIT
        # ===============================================
        elif choice == "11":
            print(
                "\nThank you for using FINCORE!"
            )
            break
        else:
            print(
                "\nInvalid choice."
                "Please choose 1-11."
            )
# =========================================
# RUN PROGRAM
# =========================================

if __name__ == "__main__":
    main()



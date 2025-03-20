from models.loans import Loan

class LoanService:
    def create_loan(self, account_number, amount, loan_type, interest_rate):
        try:
            loan = Loan(account_number, amount, loan_type, interest_rate)
            loan.save()
        except Exception as e:
            print(f"Error creating loan: {e}")

    def get_loan(self, loan_id):
        try:
            loan = Loan.get(loan_id)
            return loan
        except Exception as e:
            print(f"Error fetching loan: {e}")
            return None

    def list_loans(self, account_number):
        try:
            loans = Loan.filter(account_number=account_number)
            return loans
        except Exception as e:
            print(f"Error listing loans: {e}")
            return []

    def delete_loan(self, loan_id):
        try:
            loan = Loan.get(loan_id)
            if loan:
                loan.delete()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error deleting loan: {e}")
            return False
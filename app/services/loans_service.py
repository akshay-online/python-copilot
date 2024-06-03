from models.loans import Loan

class LoanService:
    # existing methods...

    def create_loan(self, account_number, amount, loan_type, interest_rate):
        # Create a new loan transaction
        loan = Loan(account_number, amount, loan_type, interest_rate)
        # Save the loan to the database
        loan.save()

    def get_loan(self, loan_id):
        # Get the loan details from the database
        loan = Loan.get(loan_id)
        return loan

    def list_loans(self, account_number):
        # Get all loans for the specified account from the database
        loans = Loan.filter(account_number=account_number)
        return loans
    
    def delete_loan(self, loan_id):
        # Delete the loan from the database
        loan = Loan.get(loan_id)
        if loan:
            loan.delete()
            return True
        else:
            return False
# app/services/loan_service.py
class LoanService:
    def __init__(self):
        self.loans = []

    def create_loan(self, loan_id, account_number, amount, loan_type):
        loan = {
            "loan_id": loan_id,
            "account_number": account_number,
            "amount": amount,
            "loan_type": loan_type
        }
        self.loans.append(loan)
        return loan

    def get_loan_details(self, loan_id):
        for loan in self.loans:
            if loan["loan_id"] == loan_id:
                return loan
        return None

    def update_loan_amount(self, loan_id, amount):
        for loan in self.loans:
            if loan["loan_id"] == loan_id:
                loan["amount"] = amount
                return loan
        return None

    def delete_loan(self, loan_id):
        for loan in self.loans:
            if loan["loan_id"] == loan_id:
                self.loans.remove(loan)
                return loan
        return None

    def list_loans(self):
        return self.loans
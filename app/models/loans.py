class Loan:
    def __init__(self, transaction_id, account_number, amount, timestamp, loan_type, interest_rate):
        self.loan_type = loan_type
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.amount * self.interest_rate / 100
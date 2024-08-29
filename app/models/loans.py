class Loan:
    def __init__(self, transaction_id, account_number, amount, timestamp, loan_type, interest_rate, loan_date, status):
        self.loan_type = loan_type
        self.interest_rate = interest_rate
        self.amount = amount
        self.account_number = account_number


    def calculate_interest(self):
        return self.amount * self.interest_rate / 100
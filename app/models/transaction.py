class Transaction:
    def __init__(self, transaction_id, account_number, amount, timestamp):
        self.transaction_id = transaction_id
        self.account_number = account_number
        self.amount = amount
        self.timestamp = timestamp

class Withdrawal(Transaction):
    def __init__(self, transaction_id, account_number, amount, timestamp, atm_id):
        super().__init__(transaction_id, account_number, amount, timestamp)
        self.atm_id = atm_id

class Deposit(Transaction):
    def __init__(self, transaction_id, account_number, amount, timestamp, deposit_method):
        super().__init__(transaction_id, account_number, amount, timestamp)
        self.deposit_method = deposit_method
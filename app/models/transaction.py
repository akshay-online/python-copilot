class Transaction:
    def __init__(self, transaction_id, account_number, amount, timestamp):
        self.transaction_id = transaction_id
        self.account_number = account_number
        self.amount = amount
        self.timestamp = timestamp

        self.transactions = [
            {"id": 1, "account_number": "1234567890", "amount": 100.0},
            {"id": 2, "account_number": "0987654321", "amount": 200.0},
        ]

    def create_transaction(self, account_number, amount):
        transaction = {"id": len(self.transactions) + 1, "account_number": account_number, "amount": amount}
        self.transactions.append(transaction)
        return transaction

    def get_transaction(self, transaction_id):
        for transaction in self.transactions:
            if transaction["id"] == transaction_id:
                return transaction
        return None

    def list_transactions(self, account_number):
        return [transaction for transaction in self.transactions if transaction["account_number"] == account_number]
    

class Withdrawal(Transaction):   

        def __init__(self) :
                self.withdrawals = [
                        {"id": 1, "account_number": "1234567890", "amount": 100.0},
                        {"id": 2, "account_number": "0987654321", "amount": 200.0},
                ]

        def create_withdrawal(self, account_number, amount):
                # use the self.withdrawals list to create a new withdrawal transaction
                withdrawal = {"id": len(self.withdrawals) + 1, "account_number": account_number, "amount": amount}
                self.withdrawals.append(withdrawal)

        def get_withdrawal(self, transaction_id):
                # use the self.withdrawals list to get the withdrawal transaction details
                for withdrawal in self.withdrawals:
                        if withdrawal["id"] == transaction_id:
                                return withdrawal
        
        def list_withdrawals(self, account_number):
                # use the self.withdrawals list to get all withdrawal transactions for the specified account
                return [withdrawal for withdrawal in self.withdrawals if withdrawal["account_number"] == account_number]
        


class Deposit(Transaction):
    def __init__(self) -> None:
        self.deposits = [
            {"id": 1, "account_number": "1234567890", "amount": 100.0},
            {"id": 2, "account_number": "0987654321", "amount": 200.0},
        ]

    def create_deposit(self, account_number, amount):
        # use the self.deposits list to create a new deposit transaction
        deposit = {"id": len(self.deposits) + 1, "account_number": account_number, "amount": amount}
        self.deposits.append(deposit)
    
    def get_deposit(self, transaction_id):
        # use the self.deposits list to get the deposit transaction details
        for deposit in self.deposits:
            if deposit["id"] == transaction_id:
                return deposit

    
    def list_deposits(self, account_number):
        # use the self.deposits list to get all deposit transactions for the specified account
        return [deposit for deposit in self.deposits if deposit["account_number"] == account_number]

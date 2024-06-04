from models.transaction import Transaction

class TransactionService:
    def __init__(self):
        # Mock data
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
    
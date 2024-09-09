# app/services/transaction_service.py
class TransactionService:
    def __init__(self):
        self.transactions = []

    def create_transaction(self, transaction_id, account_number, amount):
        transaction = {
            "transaction_id": transaction_id,
            "account_number": account_number,
            "amount": amount
        }
        self.transactions.append(transaction)
        return transaction

    def get_transaction_details(self, transaction_id):
        for transaction in self.transactions:
            if transaction["transaction_id"] == transaction_id:
                return transaction
        return None

    def update_transaction_amount(self, transaction_id, amount):
        for transaction in self.transactions:
            if transaction["transaction_id"] == transaction_id:
                transaction["amount"] = amount
                return transaction
        return None

    def delete_transaction(self, transaction_id):
        for transaction in self.transactions:
            if transaction["transaction_id"] == transaction_id:
                self.transactions.remove(transaction)
                return transaction
        return None

    def list_transactions(self):
        return self.transactions
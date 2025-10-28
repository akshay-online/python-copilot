from models.transaction import Transaction
from datetime import datetime

class TransactionService:
    def __init__(self):
        self.transactions = [
            {"id": 1, "account_number": "1234567890", "amount": 100.0, "timestamp": "2025-01-15T10:30:00"},
            {"id": 2, "account_number": "0987654321", "amount": 200.0, "timestamp": "2025-02-20T14:45:00"},
        ]

    def create_transaction(self, account_number, amount):
        try:
            transaction = {
                "id": len(self.transactions) + 1, 
                "account_number": account_number, 
                "amount": amount,
                "timestamp": datetime.now().isoformat()
            }
            self.transactions.append(transaction)
            return transaction
        except Exception as e:
            print(f"Error creating transaction: {e}")
            return None

    def get_transaction(self, transaction_id):
        try:
            for transaction in self.transactions:
                if transaction["id"] == transaction_id:
                    return transaction
            return None
        except Exception as e:
            print(f"Error fetching transaction: {e}")
            return None

    def list_transactions(self, account_number):
        try:
            return [transaction for transaction in self.transactions if transaction["account_number"] == account_number]
        except Exception as e:
            print(f"Error listing transactions: {e}")
            return []
    
    def get_transactions_by_month(self, year, month, account_number=None):
        """
        Get all transactions for a specific month and year.
        
        Args:
            year: The year to filter by (e.g., 2025)
            month: The month to filter by (1-12)
            account_number: Optional account number to filter by
            
        Returns:
            List of transactions for the specified month
        """
        try:
            filtered_transactions = []
            for transaction in self.transactions:
                if "timestamp" in transaction:
                    # Parse the timestamp
                    tx_date = datetime.fromisoformat(transaction["timestamp"])
                    
                    # Check if the transaction is in the specified month/year
                    if tx_date.year == year and tx_date.month == month:
                        # Apply account filter if provided
                        if account_number is None or transaction["account_number"] == account_number:
                            filtered_transactions.append(transaction)
            
            return filtered_transactions
        except Exception as e:
            print(f"Error getting monthly transactions: {e}")
            return []

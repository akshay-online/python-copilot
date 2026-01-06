from models.transaction import UPITransaction
from datetime import date

class UPIService:
    def __init__(self):
        self.upi_transaction = UPITransaction()

    def create_upi_transaction(self, account_number, amount, upi_id, recipient_upi):
        """Create a new UPI transaction and update daily count"""
        return self.upi_transaction.create_upi_transaction(account_number, amount, upi_id, recipient_upi)

    def get_upi_transaction(self, transaction_id):
        """Get UPI transaction by ID"""
        return self.upi_transaction.get_upi_transaction(transaction_id)

    def list_upi_transactions(self, account_number):
        """List all UPI transactions for an account"""
        return self.upi_transaction.list_upi_transactions(account_number)

    def get_daily_upi_count(self, account_number, date_str=None):
        """Get UPI transaction count for an account on a specific date"""
        return self.upi_transaction.get_daily_upi_count(account_number, date_str)

    def get_upi_transactions_by_date(self, account_number, date_str):
        """Get all UPI transactions for an account on a specific date"""
        return self.upi_transaction.get_upi_transactions_by_date(account_number, date_str)

    def get_account_daily_summary(self, account_number, date_str=None):
        """Get daily UPI transaction summary for an account"""
        if date_str is None:
            date_str = date.today().isoformat()
        
        count = self.get_daily_upi_count(account_number, date_str)
        transactions = self.get_upi_transactions_by_date(account_number, date_str)
        total_amount = sum(txn["amount"] for txn in transactions)
        
        return {
            "account_number": account_number,
            "date": date_str,
            "transaction_count": count,
            "total_amount": total_amount,
            "transactions": transactions
        }
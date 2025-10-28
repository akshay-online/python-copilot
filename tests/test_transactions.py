import unittest
from app.models.transaction import Transaction
from app.services.transaction_service import TransactionService
from datetime import datetime

class TestTransactionService(unittest.TestCase):
    def setUp(self):
        self.transaction_service = TransactionService()

    def test_create_transaction(self):
        transaction_data = {
            "account_number": "1234567890",
            "amount": 100.0
        }
        transaction_id = self.transaction_service.create_transaction(transaction_data)
        transaction = self.transaction_service.get_transaction(transaction_id)
        self.assertEqual(transaction.account_number, transaction_data["account_number"])
        self.assertEqual(transaction.amount, transaction_data["amount"])

    def test_get_transaction(self):
        transaction_data = {
            "account_number": "1234567890",
            "amount": 100.0
        }
        transaction_id = self.transaction_service.create_transaction(transaction_data)
        transaction = self.transaction_service.get_transaction(transaction_id)
        self.assertEqual(transaction.account_number, transaction_data["account_number"])
        self.assertEqual(transaction.amount, transaction_data["amount"])

    def test_list_transactions(self):
        transaction_data = {
            "account_number": "1234567890",
            "amount": 100.0
        }
        self.transaction_service.create_transaction(transaction_data)
        transactions = self.transaction_service.list_transactions(transaction_data["account_number"])
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0].account_number, transaction_data["account_number"])
        self.assertEqual(transactions[0].amount, transaction_data["amount"])
    
    def test_get_transactions_by_month(self):
        """Test getting transactions for a specific month and year"""
        # The service has predefined transactions with timestamps
        # Transaction 1: 2025-01-15
        # Transaction 2: 2025-02-20
        
        # Get transactions for January 2025
        jan_transactions = self.transaction_service.get_transactions_by_month(2025, 1)
        self.assertEqual(len(jan_transactions), 1)
        self.assertEqual(jan_transactions[0]["id"], 1)
        self.assertEqual(jan_transactions[0]["account_number"], "1234567890")
        
        # Get transactions for February 2025
        feb_transactions = self.transaction_service.get_transactions_by_month(2025, 2)
        self.assertEqual(len(feb_transactions), 1)
        self.assertEqual(feb_transactions[0]["id"], 2)
        self.assertEqual(feb_transactions[0]["account_number"], "0987654321")
        
        # Get transactions for March 2025 (should be empty)
        mar_transactions = self.transaction_service.get_transactions_by_month(2025, 3)
        self.assertEqual(len(mar_transactions), 0)
    
    def test_get_transactions_by_month_with_account_filter(self):
        """Test getting transactions for a specific month with account number filter"""
        # Get transactions for January 2025 for account 1234567890
        transactions = self.transaction_service.get_transactions_by_month(
            2025, 1, account_number="1234567890"
        )
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["account_number"], "1234567890")
        
        # Get transactions for January 2025 for different account (should be empty)
        transactions = self.transaction_service.get_transactions_by_month(
            2025, 1, account_number="9999999999"
        )
        self.assertEqual(len(transactions), 0)
    
    def test_get_transactions_by_month_with_new_transaction(self):
        """Test that newly created transactions can be filtered by month"""
        # Create a new transaction (will have current timestamp)
        new_tx = self.transaction_service.create_transaction("1111111111", 500.0)
        
        # Get current year and month
        now = datetime.now()
        current_year = now.year
        current_month = now.month
        
        # Get transactions for current month
        transactions = self.transaction_service.get_transactions_by_month(
            current_year, current_month
        )
        
        # Should find at least the newly created transaction
        self.assertGreaterEqual(len(transactions), 1)
        
        # Verify the new transaction is in the results
        tx_ids = [tx["id"] for tx in transactions]
        self.assertIn(new_tx["id"], tx_ids)

if __name__ == "__main__":
    unittest.main()
import unittest
import sys
import os
from datetime import date

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from services.upi_service import UPIService

class TestUPITransactions(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.upi_service = UPIService()
        
    def test_create_upi_transaction(self):
        """Test creating a UPI transaction"""
        account_number = "1234567890"
        amount = 500.0
        upi_id = "test@paytm"
        recipient_upi = "merchant@gpay"
        
        transaction = self.upi_service.create_upi_transaction(
            account_number, amount, upi_id, recipient_upi
        )
        
        self.assertIsNotNone(transaction)
        self.assertEqual(transaction['account_number'], account_number)
        self.assertEqual(transaction['amount'], amount)
        self.assertEqual(transaction['upi_id'], upi_id)
        self.assertEqual(transaction['recipient_upi'], recipient_upi)
        self.assertIn('id', transaction)
        self.assertIn('timestamp', transaction)
        self.assertIn('date', transaction)
        
    def test_daily_upi_count_tracking(self):
        """Test that daily UPI transaction count is tracked correctly"""
        account_number = "9876543210"
        today = date.today().isoformat()
        
        # Initially should be 0
        initial_count = self.upi_service.get_daily_upi_count(account_number)
        
        # Create a UPI transaction
        self.upi_service.create_upi_transaction(
            account_number, 100.0, "user@paytm", "shop@gpay"
        )
        
        # Count should increase by 1
        updated_count = self.upi_service.get_daily_upi_count(account_number)
        self.assertEqual(updated_count, initial_count + 1)
        
        # Create another UPI transaction
        self.upi_service.create_upi_transaction(
            account_number, 200.0, "user@paytm", "store@phonepe"
        )
        
        # Count should increase by 1 more
        final_count = self.upi_service.get_daily_upi_count(account_number)
        self.assertEqual(final_count, initial_count + 2)
        
    def test_get_upi_transaction_by_id(self):
        """Test retrieving UPI transaction by ID"""
        account_number = "1111111111"
        amount = 750.0
        upi_id = "test@phonepe"
        recipient_upi = "shop@paytm"
        
        # Create transaction
        created_txn = self.upi_service.create_upi_transaction(
            account_number, amount, upi_id, recipient_upi
        )
        
        # Retrieve by ID
        retrieved_txn = self.upi_service.get_upi_transaction(created_txn['id'])
        
        self.assertIsNotNone(retrieved_txn)
        self.assertEqual(retrieved_txn['id'], created_txn['id'])
        self.assertEqual(retrieved_txn['account_number'], account_number)
        self.assertEqual(retrieved_txn['amount'], amount)
        
    def test_list_upi_transactions_by_account(self):
        """Test listing UPI transactions for a specific account"""
        account_number = "2222222222"
        
        # Create multiple transactions
        self.upi_service.create_upi_transaction(
            account_number, 100.0, "user@paytm", "merchant1@gpay"
        )
        self.upi_service.create_upi_transaction(
            account_number, 200.0, "user@paytm", "merchant2@phonepe"
        )
        
        # List transactions for the account
        transactions = self.upi_service.list_upi_transactions(account_number)
        
        # Should include the transactions we just created
        account_txns = [txn for txn in transactions if txn['account_number'] == account_number]
        self.assertGreaterEqual(len(account_txns), 2)
        
    def test_daily_summary(self):
        """Test getting daily UPI transaction summary"""
        account_number = "3333333333"
        today = date.today().isoformat()
        
        # Create transactions
        self.upi_service.create_upi_transaction(
            account_number, 100.0, "user@paytm", "shop1@gpay"
        )
        self.upi_service.create_upi_transaction(
            account_number, 250.0, "user@paytm", "shop2@phonepe"
        )
        
        # Get summary
        summary = self.upi_service.get_account_daily_summary(account_number, today)
        
        self.assertEqual(summary['account_number'], account_number)
        self.assertEqual(summary['date'], today)
        self.assertGreaterEqual(summary['transaction_count'], 2)
        self.assertGreaterEqual(summary['total_amount'], 350.0)
        self.assertIsInstance(summary['transactions'], list)

if __name__ == '__main__':
    unittest.main()
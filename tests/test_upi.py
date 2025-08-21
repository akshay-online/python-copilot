import unittest
import sys
import os

# Add the app directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))

from services.upi_service import UPIService

class TestUPIService(unittest.TestCase):
    def setUp(self):
        self.upi_service = UPIService()

    def test_list_all_upi_payments(self):
        """Test listing all UPI payments without account filter"""
        upi_payments = self.upi_service.list_upi_payments()
        self.assertEqual(len(upi_payments), 5)  # Should return all 5 default payments
        
        # Check if all payments have required fields
        for payment in upi_payments:
            self.assertIn('id', payment)
            self.assertIn('account_number', payment)
            self.assertIn('amount', payment)
            self.assertIn('upi_id', payment)
            self.assertIn('type', payment)
            self.assertEqual(payment['type'], 'upi')

    def test_list_upi_payments_by_account(self):
        """Test listing UPI payments filtered by account number"""
        account_number = "1234567890"
        upi_payments = self.upi_service.list_upi_payments(account_number)
        
        # Should return only payments for this account
        for payment in upi_payments:
            self.assertEqual(payment['account_number'], account_number)

    def test_get_upi_payment_by_id(self):
        """Test getting a specific UPI payment by ID"""
        payment_id = 1
        upi_payment = self.upi_service.get_upi_payment(payment_id)
        
        self.assertIsNotNone(upi_payment)
        self.assertEqual(upi_payment['id'], payment_id)
        self.assertEqual(upi_payment['type'], 'upi')

    def test_get_nonexistent_upi_payment(self):
        """Test getting a UPI payment that doesn't exist"""
        payment_id = 999
        upi_payment = self.upi_service.get_upi_payment(payment_id)
        
        self.assertIsNone(upi_payment)

    def test_create_upi_payment(self):
        """Test creating a new UPI payment"""
        initial_count = len(self.upi_service.upi_payments)
        
        new_payment = self.upi_service.create_upi_payment(
            account_number="5555666677",
            amount=100.0,
            upi_id="newuser@upi"
        )
        
        self.assertIsNotNone(new_payment)
        self.assertEqual(new_payment['account_number'], "5555666677")
        self.assertEqual(new_payment['amount'], 100.0)
        self.assertEqual(new_payment['upi_id'], "newuser@upi")
        self.assertEqual(new_payment['type'], 'upi')
        
        # Check that the payment was added to the list
        self.assertEqual(len(self.upi_service.upi_payments), initial_count + 1)

    def test_list_all_p2p_upi_payments(self):
        """Test listing all P2P UPI payments without account filter"""
        p2p_payments = self.upi_service.list_p2p_upi_payments()
        
        # Should return only P2P payments
        for payment in p2p_payments:
            self.assertEqual(payment['upi_category'], 'p2p')
            self.assertIn('recipient_upi', payment)
            self.assertIn('description', payment)

    def test_list_p2p_upi_payments_by_account(self):
        """Test listing P2P UPI payments filtered by account number"""
        account_number = "1234567890"
        p2p_payments = self.upi_service.list_p2p_upi_payments(account_number)
        
        # Should return only P2P payments for this account
        for payment in p2p_payments:
            self.assertEqual(payment['account_number'], account_number)
            self.assertEqual(payment['upi_category'], 'p2p')

if __name__ == "__main__":
    unittest.main()
import unittest
from app.models.transaction import Transaction
from app.services.transaction_service import TransactionService

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

if __name__ == "__main__":
    unittest.main()
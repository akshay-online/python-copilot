# tests/test_transactions.py
import unittest
from app.services.transaction_service import TransactionService

class TestTransactionService(unittest.TestCase):
    def setUp(self):
        self.transaction_service = TransactionService()

    def test_create_transaction(self):
        transaction_data = {
            "transaction_id": "txn123",
            "account_number": "acc456",
            "amount": 100.0
        }
        transaction = self.transaction_service.create_transaction(
            transaction_data["transaction_id"],
            transaction_data["account_number"],
            transaction_data["amount"]
        )
        self.assertEqual(transaction["transaction_id"], "txn123")
        self.assertEqual(transaction["account_number"], "acc456")
        self.assertEqual(transaction["amount"], 100.0)

    def test_list_transactions(self):
        transaction_data1 = {
            "transaction_id": "txn123",
            "account_number": "acc456",
            "amount": 100.0
        }
        transaction_data2 = {
            "transaction_id": "txn124",
            "account_number": "acc457",
            "amount": 200.0
        }
        self.transaction_service.create_transaction(
            transaction_data1["transaction_id"],
            transaction_data1["account_number"],
            transaction_data1["amount"]
        )
        self.transaction_service.create_transaction(
            transaction_data2["transaction_id"],
            transaction_data2["account_number"],
            transaction_data2["amount"]
        )
        transactions = self.transaction_service.list_transactions()
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0]["transaction_id"], "txn123")
        self.assertEqual(transactions[1]["transaction_id"], "txn124")

if __name__ == '__main__':
    unittest.main()
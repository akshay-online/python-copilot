# tests/test_account_service.py
import unittest
from app.services.account_service import AccountService

class TestAccountService(unittest.TestCase):
    def setUp(self):
        self.account_service = AccountService()

    def test_create_account(self):
        account_data = {
            "account_number": "123456",
            "account_name": "John Doe",
            "balance": 1000.0
        }
        account = self.account_service.create_account(
            account_data["account_number"],
            account_data["account_name"],
            account_data["balance"]
        )
        self.assertEqual(account["account_number"], "123456")
        self.assertEqual(account["account_name"], "John Doe")
        self.assertEqual(account["balance"], 1000.0)

    def test_get_account_details(self):
        account_data = {
            "account_number": "123456",
            "account_name": "John Doe",
            "balance": 1000.0
        }
        self.account_service.create_account(
            account_data["account_number"],
            account_data["account_name"],
            account_data["balance"]
        )
        account = self.account_service.get_account_details("123456")
        self.assertIsNotNone(account)
        self.assertEqual(account["account_number"], "123456")
        self.assertEqual(account["account_name"], "John Doe")
        self.assertEqual(account["balance"], 1000.0)

    def test_update_account_balance(self):
        account_data = {
            "account_number": "123456",
            "account_name": "John Doe",
            "balance": 1000.0
        }
        self.account_service.create_account(
            account_data["account_number"],
            account_data["account_name"],
            account_data["balance"]
        )
        updated_account = self.account_service.update_account_balance("123456", 1500.0)
        self.assertIsNotNone(updated_account)
        self.assertEqual(updated_account["account_number"], "123456")
        self.assertEqual(updated_account["balance"], 1500.0)

    def test_delete_account(self):
        account_data = {
            "account_number": "123456",
            "account_name": "John Doe",
            "balance": 1000.0
        }
        self.account_service.create_account(
            account_data["account_number"],
            account_data["account_name"],
            account_data["balance"]
        )
        deleted_account = self.account_service.delete_account("123456")
        self.assertIsNotNone(deleted_account)
        self.assertEqual(deleted_account["account_number"], "123456")
        self.assertEqual(deleted_account["balance"], 1000.0)
        self.assertIsNone(self.account_service.get_account_details("123456"))

if __name__ == '__main__':
    unittest.main()
import unittest
from account import Account
from app.services.account_service import AccountService

class TestAccountAPI(unittest.TestCase):
    def setUp(self):
        self.account_service = AccountService()

    def test_create_account(self):
        account_data = {
            "account_number": "1234567890",
            "balance": 1000
        }
        account = self.account_service.create_account(account_data)
        self.assertIsInstance(account, Account)
        self.assertEqual(account.account_number, "1234567890")
        self.assertEqual(account.balance, 1000)

    def test_get_account_details(self):
        account_data = {
            "account_number": "1234567890",
            "balance": 1000
        }
        self.account_service.create_account(account_data)
        account = self.account_service.get_account_details("1234567890")
        self.assertIsInstance(account, Account)
        self.assertEqual(account.account_number, "1234567890")
        self.assertEqual(account.balance, 1000)

    def test_update_account_balance(self):
        account_data = {
            "account_number": "1234567890",
            "balance": 1000
        }
        self.account_service.create_account(account_data)
        updated_account = self.account_service.update_account_balance("1234567890", 500)
        self.assertIsInstance(updated_account, Account)
        self.assertEqual(updated_account.account_number, "1234567890")
        self.assertEqual(updated_account.balance, 1500)

if __name__ == '__main__':
    unittest.main()
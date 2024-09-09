# tests/test_loans_service.py
import unittest
from app.services.loans_service import LoanService

class TestLoanService(unittest.TestCase):
    def setUp(self):
        self.loan_service = LoanService()

    def test_create_loan(self):
        loan_data = {
            "loan_id": "loan123",
            "account_number": "acc456",
            "amount": 1000.0,
            "loan_type": "personal"
        }
        loan = self.loan_service.create_loan(
            loan_data["loan_id"],
            loan_data["account_number"],
            loan_data["amount"],
            loan_data["loan_type"]
        )
        self.assertEqual(loan["loan_id"], "loan123")
        self.assertEqual(loan["account_number"], "acc456")
        self.assertEqual(loan["amount"], 1000.0)
        self.assertEqual(loan["loan_type"], "personal")

    def test_get_loan_details(self):
        loan_data = {
            "loan_id": "loan123",
            "account_number": "acc456",
            "amount": 1000.0,
            "loan_type": "personal"
        }
        self.loan_service.create_loan(
            loan_data["loan_id"],
            loan_data["account_number"],
            loan_data["amount"],
            loan_data["loan_type"]
        )
        loan = self.loan_service.get_loan_details("loan123")
        self.assertIsNotNone(loan)
        self.assertEqual(loan["loan_id"], "loan123")
        self.assertEqual(loan["account_number"], "acc456")
        self.assertEqual(loan["amount"], 1000.0)
        self.assertEqual(loan["loan_type"], "personal")

    def test_update_loan_amount(self):
        loan_data = {
            "loan_id": "loan123",
            "account_number": "acc456",
            "amount": 1000.0,
            "loan_type": "personal"
        }
        self.loan_service.create_loan(
            loan_data["loan_id"],
            loan_data["account_number"],
            loan_data["amount"],
            loan_data["loan_type"]
        )
        updated_loan = self.loan_service.update_loan_amount("loan123", 1500.0)
        self.assertIsNotNone(updated_loan)
        self.assertEqual(updated_loan["loan_id"], "loan123")
        self.assertEqual(updated_loan["amount"], 1500.0)

    def test_delete_loan(self):
        loan_data = {
            "loan_id": "loan123",
            "account_number": "acc456",
            "amount": 1000.0,
            "loan_type": "personal"
        }
        self.loan_service.create_loan(
            loan_data["loan_id"],
            loan_data["account_number"],
            loan_data["amount"],
            loan_data["loan_type"]
        )
        deleted_loan = self.loan_service.delete_loan("loan123")
        self.assertIsNotNone(deleted_loan)
        self.assertEqual(deleted_loan["loan_id"], "loan123")
        self.assertEqual(deleted_loan["amount"], 1000.0)
        self.assertEqual(deleted_loan["loan_type"], "personal")
        self.assertIsNone(self.loan_service.get_loan_details("loan123"))

    def test_list_loans(self):
        loan_data1 = {
            "loan_id": "loan123",
            "account_number": "acc456",
            "amount": 1000.0,
            "loan_type": "personal"
        }
        loan_data2 = {
            "loan_id": "loan124",
            "account_number": "acc457",
            "amount": 2000.0,
            "loan_type": "home"
        }
        self.loan_service.create_loan(
            loan_data1["loan_id"],
            loan_data1["account_number"],
            loan_data1["amount"],
            loan_data1["loan_type"]
        )
        self.loan_service.create_loan(
            loan_data2["loan_id"],
            loan_data2["account_number"],
            loan_data2["amount"],
            loan_data2["loan_type"]
        )
        loans = self.loan_service.list_loans()
        self.assertEqual(len(loans), 2)
        self.assertEqual(loans[0]["loan_id"], "loan123")
        self.assertEqual(loans[1]["loan_id"], "loan124")

if __name__ == '__main__':
    unittest.main()
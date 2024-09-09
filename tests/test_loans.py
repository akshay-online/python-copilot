import unittest
from app.services.loans_service import LoanService
from loans import Loan

class TestLoanService(unittest.TestCase):
    def setUp(self):
        self.loan_service = LoanService()

    def test_create_loan(self):
        loan_data = {
            "account_number": "1234567890",
            "amount": 1000.0,
            "loan_type": "Personal",
            "interest_rate": 5.0
        }
        self.loan_service.create_loan(**loan_data)
        loan = Loan.filter(account_number=loan_data["account_number"]).first()
        self.assertEqual(loan.account_number, loan_data["account_number"])
        self.assertEqual(loan.amount, loan_data["amount"])
        self.assertEqual(loan.loan_type, loan_data["loan_type"])
        self.assertEqual(loan.interest_rate, loan_data["interest_rate"])

    def test_get_loan(self):
        loan_data = {
            "account_number": "1234567890",
            "amount": 1000.0,
            "loan_type": "Personal",
            "interest_rate": 5.0
        }
        self.loan_service.create_loan(**loan_data)
        loan = Loan.filter(account_number=loan_data["account_number"]).first()
        fetched_loan = self.loan_service.get_loan(loan.id)
        self.assertEqual(fetched_loan.id, loan.id)

    def test_list_loans(self):
        loan_data = {
            "account_number": "1234567890",
            "amount": 1000.0,
            "loan_type": "Personal",
            "interest_rate": 5.0
        }
        self.loan_service.create_loan(**loan_data)
        loans = self.loan_service.list_loans(loan_data["account_number"])
        self.assertEqual(len(loans), 1)
        self.assertEqual(loans[0].account_number, loan_data["account_number"])

    def test_delete_loan(self):
        loan_data = {
            "account_number": "1234567890",
            "amount": 1000.0,
            "loan_type": "Personal",
            "interest_rate": 5.0
        }
        self.loan_service.create_loan(**loan_data)
        loan = Loan.filter(account_number=loan_data["account_number"]).first()
        result = self.loan_service.delete_loan(loan.id)
        self.assertTrue(result)
        deleted_loan = self.loan_service.get_loan(loan.id)
        self.assertIsNone(deleted_loan)

if __name__ == "__main__":
    unittest.main()
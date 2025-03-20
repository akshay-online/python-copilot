from models.transaction import Withdrawal

class WithdrawalService:
    def __init__(self):
        self.withdrawals = [
            {"id": 1, "account_number": "1234567890", "amount": 100.0, "type": "withdraw", "date": "2021-10-01"},
            {"id": 2, "account_number": "0987654321", "amount": 200.0, "type": "withdraw", "date": "2021-10-01"},
        ]

    def create_withdrawal(self, account_number, amount):
        try:
            withdrawal = {"id": len(self.withdrawals) + 1, "account_number": account_number, "amount": amount, "type": "withdraw", "date": "2021-10-01"}
            self.withdrawals.append(withdrawal)
        except Exception as e:
            print(f"Error creating withdrawal: {e}")

    def get_withdrawal(self, transaction_id):
        try:
            for withdrawal in self.withdrawals:
                if withdrawal["id"] == transaction_id:
                    return withdrawal
        except Exception as e:
            print(f"Error fetching withdrawal: {e}")
            return None

    def list_withdrawals(self, account_number):
        try:
            return [withdrawal for withdrawal in self.withdrawals if withdrawal["account_number"] == account_number]
        except Exception as e:
            print(f"Error listing withdrawals: {e}")
            return []


from models.transaction import Withdrawal

class WithdrawalService:
    
        def __init__(self) :
                self.withdrawals = [
                        {"id": 1, "account_number": "1234567890", "amount": 100.0, "type": "withdraw", "date": "2021-10-01"},
                        {"id": 2, "account_number": "0987654321", "amount": 200.0, "type": "withdraw", "date": "2021-10-01"},
                ]

        def create_withdrawal(self, account_number, amount):
                # use the self.withdrawals list to create a new withdrawal transaction
                withdrawal = {"id": len(self.withdrawals) + 1, "account_number": account_number, "amount": amount, "type": "withdraw", "date": "2021-10-01"}
                self.withdrawals.append(withdrawal)

        def get_withdrawal(self, transaction_id):
                # use the self.withdrawals list to get the withdrawal transaction details
                for withdrawal in self.withdrawals:
                        if withdrawal["id"] == transaction_id:
                                return withdrawal
        
        def list_withdrawals(self, account_number):
                # use the self.withdrawals list to get all withdrawal transactions for the specified account
                return [withdrawal for withdrawal in self.withdrawals if withdrawal["account_number"] == account_number]
        

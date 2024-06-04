from models.transaction import Deposit

class DepositService:
    def __init__(self) -> None:
        self.deposits = [
            {"id": 1, "account_number": "1234567890", "amount": 100.0},
            {"id": 2, "account_number": "0987654321", "amount": 200.0},
        ]

    def create_deposit(self, account_number, amount):
        # use the self.deposits list to create a new deposit transaction
        deposit = {"id": len(self.deposits) + 1, "account_number": account_number, "amount": amount}
        self.deposits.append(deposit)
    
    def get_deposit(self, transaction_id):
        # use the self.deposits list to get the deposit transaction details
        for deposit in self.deposits:
            if deposit["id"] == transaction_id:
                return deposit

    
    def list_deposits(self, account_number):
        # use the self.deposits list to get all deposit transactions for the specified account
        return [deposit for deposit in self.deposits if deposit["account_number"] == account_number]

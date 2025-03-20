from models.transaction import Deposit

class DepositService:
    def __init__(self) -> None:
        self.deposits = [
            {"id": 1, "account_number": "1234567890", "amount": 100.0},
            {"id": 2, "account_number": "0987654321", "amount": 200.0},
        ]

    def create_deposit(self, account_number, amount):
        try:
            deposit = {"id": len(self.deposits) + 1, "account_number": account_number, "amount": amount}
            self.deposits.append(deposit)
        except Exception as e:
            print(f"Error creating deposit: {e}")

    def get_deposit(self, transaction_id):
        try:
            for deposit in self.deposits:
                if deposit["id"] == transaction_id:
                    return deposit
        except Exception as e:
            print(f"Error fetching deposit: {e}")
            return None

    def list_deposits(self, account_number):
        try:
            return [deposit for deposit in self.deposits if deposit["account_number"] == account_number]
        except Exception as e:
            print(f"Error listing deposits: {e}")
            return []

# app/services/account_service.py
class AccountService:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, account_name, balance):
        account = {
            "account_number": account_number,
            "account_name": account_name,
            "balance": balance
        }
        self.accounts.append(account)
        return account

    def get_account_details(self, account_number):
        for account in self.accounts:
            if account["account_number"] == account_number:
                return account
        return None

    def update_account_balance(self, account_number, balance):
        for account in self.accounts:
            if account["account_number"] == account_number:
                account["balance"] = balance
                return account
        return None

    def delete_account(self, account_number):
        for account in self.accounts:
            if account["account_number"] == account_number:
                self.accounts.remove(account)
                return account
        return None
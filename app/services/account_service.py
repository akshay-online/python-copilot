from account import Account

class AccountService:
    def create_account(self, account_number, balance):
        """
        Create a new bank account with the given account number and initial balance.
        """
        account = Account(account_number, balance)
        # Save the account to the database or perform any other necessary operations
        return account

    def get_account_details(self, account_number):
        """
        Get the details of a bank account with the given account number.
        """
        # Retrieve the account from the database or perform any other necessary operations
        account = Account(account_number, balance)
        return account

    def update_account_balance(self, account_number, amount):
        """
        Update the balance of a bank account with the given account number by the specified amount.
        """
        # Retrieve the account from the database or perform any other necessary operations
        account = Account(account_number, balance)
        account.deposit(amount)  # or account.withdraw(amount)
        # Save the updated account to the database or perform any other necessary operations
        return account
    
    # delete account
    def delete_account(self, account_number):
        """
        Delete the account with the given account number.
        """
        # Retrieve the account from the database or perform any other necessary operations
        account = Account(account_number, balance)
        # Delete the account from the database or perform any other necessary operations
        return account
    

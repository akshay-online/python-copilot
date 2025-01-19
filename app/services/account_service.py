import pyodbc
from models.account import Account

class AccountService:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def _get_connection(self):
        return pyodbc.connect(self.connection_string)

    def create_account(self, account_number, balance):
        """ 
        Create a new bank account with the given account number and initial balance.
        """
        account = Account(account_number, balance)
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO accounts (account_number, balance) VALUES (?, ?)", (account_number, balance))
            conn.commit()
        return account

    def get_account_details(self, account_number):
        """
        Get the details of a bank account with the given account number.
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT account_number, balance FROM accounts WHERE account_number = ?", (account_number,))
            row = cursor.fetchone()
            if row:
                account = Account(row[0], row[1])
                return account
            else:
                return None

    def update_account_balance(self, account_number, amount):
        """
        Update the balance of a bank account with the given account number by the specified amount.
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
            row = cursor.fetchone()
            if row:
                new_balance = row[0] + amount
                cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (new_balance, account_number))
                conn.commit()
                account = Account(account_number, new_balance)
                return account
            else:
                return None

    def delete_account(self, account_number):
        """
        Delete the account with the given account number.
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM accounts WHERE account_number = ?", (account_number,))
            conn.commit()
            return True


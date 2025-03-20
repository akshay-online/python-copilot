import pyodbc
from models.account import Account

class AccountService:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def _get_connection(self):
        return pyodbc.connect(self.connection_string)

    def create_account(self, account_number, balance):
        try:
            account = Account(account_number, balance)
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO accounts (account_number, balance) VALUES (?, ?)", (account_number, balance))
                conn.commit()
            return account
        except Exception as e:
            print(f"Error creating account: {e}")
            return None

    def get_account_details(self, account_number):
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT account_number, balance FROM accounts WHERE account_number = ?", (account_number,))
                row = cursor.fetchone()
                if row:
                    account = Account(row[0], row[1])
                    return account
                else:
                    return None
        except Exception as e:
            print(f"Error fetching account details: {e}")
            return None

    def update_account_balance(self, account_number, amount):
        try:
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
        except Exception as e:
            print(f"Error updating account balance: {e}")
            return None

    def delete_account(self, account_number):
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM accounts WHERE account_number = ?", (account_number,))
                conn.commit()
                return True
        except Exception as e:
            print(f"Error deleting account: {e}")
            return False


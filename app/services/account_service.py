import pyodbc
import logging
from models.account import Account

logger = logging.getLogger(__name__)

class AccountService:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def _get_connection(self):
        # Ensure compatibility with pyodbc context manager support
        conn = pyodbc.connect(self.connection_string)
        return conn

    def create_account(self, account_number, balance):
        """
        Create a new account if the account number does not already exist.

        Parameters:
            account_number (str): The account number to create.
            balance (float): The initial balance for the account.

        Returns:
            Account: The created Account object, or None if creation failed.
        """
        if not isinstance(account_number, str) or not account_number.strip():
            logger.warning("Invalid account number.")
            return None
        if not isinstance(balance, (int, float)) or balance < 0:
            logger.warning("Invalid balance. Must be a non-negative number.")
            return None
        if len(account_number) > 32 or not account_number.isalnum():
            logger.warning("Account number must be alphanumeric and <= 32 characters.")
            return None
        try:
            account = Account(account_number, balance)
            conn = self._get_connection()
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT 1 FROM accounts WHERE account_number = ?", (account_number,))
                if cursor.fetchone():
                    logger.warning("Account number already exists.")
                    return None
                cursor.execute("INSERT INTO accounts (account_number, balance) VALUES (?, ?)", (account_number, balance))
                conn.commit()
                return account
            finally:
                conn.close()
        except Exception as e:
            logger.error(f"Error creating account: {e}")
            return None

    def get_account_details(self, account_number):
        """
        Retrieve account details by account number.

        Parameters:
            account_number (str): The account number to look up.

        Returns:
            Account: The Account object if found, else None.
        """
        if not isinstance(account_number, str) or not account_number.strip():
            logger.warning("Invalid account number.")
            return None
        if len(account_number) > 32 or not account_number.isalnum():
            logger.warning("Account number must be alphanumeric and <= 32 characters.")
            return None
        try:
            conn = self._get_connection()
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT account_number, balance FROM accounts WHERE account_number = ?", (account_number,))
                row = cursor.fetchone()
                if row:
                    account = Account(row[0], row[1])
                    return account
                else:
                    logger.info("Account not found.")
                    return None
            finally:
                conn.close()
        except Exception as e:
            logger.error(f"Error fetching account details: {e}")
            return None

    def update_account_balance(self, account_number, amount):
        """
        Atomically update the account balance by a given amount.

        Parameters:
            account_number (str): The account number to update.
            amount (float): The amount to add (or subtract) from the balance.

        Returns:
            Account: The updated Account object, or None if update failed.
        """
        if not isinstance(account_number, str) or not account_number.strip():
            logger.warning("Invalid account number.")
            return None
        if not isinstance(amount, (int, float)):
            logger.warning("Invalid amount. Must be a number.")
            return None
        if len(account_number) > 32 or not account_number.isalnum():
            logger.warning("Account number must be alphanumeric and <= 32 characters.")
            return None
        try:
            conn = self._get_connection()
            try:
                cursor = conn.cursor()
                # Atomic update: only update if sufficient funds
                cursor.execute(
                    "UPDATE accounts SET balance = balance + ? WHERE account_number = ? AND balance + ? >= 0",
                    (amount, account_number, amount)
                )
                if cursor.rowcount == 0:
                    # Check if account exists
                    cursor.execute("SELECT 1 FROM accounts WHERE account_number = ?", (account_number,))
                    if cursor.fetchone():
                        logger.warning("Insufficient funds.")
                    else:
                        logger.info("Account not found.")
                    conn.rollback()
                    return None
                conn.commit()
                cursor.execute("SELECT account_number, balance FROM accounts WHERE account_number = ?", (account_number,))
                row = cursor.fetchone()
                if row:
                    return Account(row[0], row[1])
                else:
                    logger.error("Account updated but not found.")
                    return None
            finally:
                conn.close()
        except Exception as e:
            logger.error(f"Error updating account balance: {e}")
            return None

    def delete_account(self, account_number):
        """
        Delete an account by account number.

        Parameters:
            account_number (str): The account number to delete.

        Returns:
            bool: True if deleted, False otherwise.
        """
        if not isinstance(account_number, str) or not account_number.strip():
            logger.warning("Invalid account number.")
            return False
        if len(account_number) > 32 or not account_number.isalnum():
            logger.warning("Account number must be alphanumeric and <= 32 characters.")
            return False
        try:
            conn = self._get_connection()
            try:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM accounts WHERE account_number = ?", (account_number,))
                if cursor.rowcount == 0:
                    logger.info("Account not found.")
                    conn.rollback()
                    return False
                conn.commit()
                return True
            finally:
                conn.close()
        except Exception as e:
            logger.error(f"Error deleting account: {e}")
            return False


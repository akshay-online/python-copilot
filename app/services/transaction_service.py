from models.transaction import Deposit, Transaction, Withdrawal

class TransactionService:
    def create_transaction(self, account_number, amount):
        # Create a new transaction
        transaction = Transaction(account_number, amount)
        # Save the transaction to the database
        transaction.save()

    def get_transaction(self, transaction_id):
        # Get the transaction details from the database
        transaction = Transaction.get(transaction_id)
        return transaction

    def list_transactions(self, account_number):
        # Get all transactions for the specified account from the database
        transactions = Transaction.filter(account_number=account_number)
        return transactions

    def create_withdrawal(self, account_number, amount):
        # Create a new withdrawal transaction
        transaction = Withdrawal(account_number, amount)
        # Save the transaction to the database
        transaction.save()

    def create_deposit(self, account_number, amount):
        # Create a new deposit transaction
        transaction = Transaction.Deposit(account_number, amount)
        # Save the transaction to the database
        transaction.save()

    def get_withdrawal(self, transaction_id):
        # Get the withdrawal transaction details from the database
        transaction = Transaction.Withdrawal.get(transaction_id)
        return transaction

    def get_deposit(self, transaction_id):
        # Get the deposit transaction details from the database
        transaction = Deposit.get(transaction_id)
        return transaction

    def list_withdrawals(self, account_number):
        # Get all withdrawal transactions for the specified account from the database
        transactions = Withdrawal.filter(account_number=account_number)
        return transactions

    def list_deposits(self, account_number):
        # Get all deposit transactions for the specified account from the database
        transactions = Deposit.filter(account_number=account_number)
        return transactions

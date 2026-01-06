class Transaction:
    def __init__(self, transaction_id, account_number, amount, timestamp):
        self.transaction_id = transaction_id
        self.account_number = account_number
        self.amount = amount
        self.timestamp = timestamp

        self.transactions = [
            {"id": 1, "account_number": "1234567890", "amount": 100.0},
            {"id": 2, "account_number": "0987654321", "amount": 200.0},
        ]

    def create_transaction(self, account_number, amount):
        transaction = {"id": len(self.transactions) + 1, "account_number": account_number, "amount": amount}
        self.transactions.append(transaction)
        return transaction

    def get_transaction(self, transaction_id):
        for transaction in self.transactions:
            if transaction["id"] == transaction_id:
                return transaction
        return None

    def list_transactions(self, account_number):
        return [transaction for transaction in self.transactions if transaction["account_number"] == account_number]
    

class Withdrawal(Transaction):   

        def __init__(self) :
                self.withdrawals = [
                        {"id": 1, "account_number": "1234567890", "amount": 100.0},
                        {"id": 2, "account_number": "0987654321", "amount": 200.0},
                ]

        def create_withdrawal(self, account_number, amount):
                # use the self.withdrawals list to create a new withdrawal transaction
                withdrawal = {"id": len(self.withdrawals) + 1, "account_number": account_number, "amount": amount}
                self.withdrawals.append(withdrawal)

        def get_withdrawal(self, transaction_id):
                # use the self.withdrawals list to get the withdrawal transaction details
                for withdrawal in self.withdrawals:
                        if withdrawal["id"] == transaction_id:
                                return withdrawal
        
        def list_withdrawals(self, account_number):
                # use the self.withdrawals list to get all withdrawal transactions for the specified account
                return [withdrawal for withdrawal in self.withdrawals if withdrawal["account_number"] == account_number]
        


class Deposit(Transaction):
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


class UPITransaction(Transaction):
    def __init__(self) -> None:
        from datetime import datetime, date
        self.upi_transactions = [
            {
                "id": 1, 
                "account_number": "1234567890", 
                "amount": 500.0,
                "upi_id": "user1@paytm",
                "recipient_upi": "merchant@gpay",
                "timestamp": datetime.now(),
                "date": date.today().isoformat()
            },
            {
                "id": 2, 
                "account_number": "0987654321", 
                "amount": 1000.0,
                "upi_id": "user2@phonepe",
                "recipient_upi": "shop@paytm",
                "timestamp": datetime.now(),
                "date": date.today().isoformat()
            }
        ]
        # Track daily UPI transaction counts per account
        self.daily_upi_counts = {}

    def create_upi_transaction(self, account_number, amount, upi_id, recipient_upi):
        from datetime import datetime, date
        
        current_date = date.today().isoformat()
        
        # Create UPI transaction
        upi_transaction = {
            "id": len(self.upi_transactions) + 1,
            "account_number": account_number,
            "amount": amount,
            "upi_id": upi_id,
            "recipient_upi": recipient_upi,
            "timestamp": datetime.now(),
            "date": current_date
        }
        self.upi_transactions.append(upi_transaction)
        
        # Update daily count
        key = f"{account_number}:{current_date}"
        self.daily_upi_counts[key] = self.daily_upi_counts.get(key, 0) + 1
        
        return upi_transaction

    def get_upi_transaction(self, transaction_id):
        for upi_transaction in self.upi_transactions:
            if upi_transaction["id"] == transaction_id:
                return upi_transaction
        return None

    def list_upi_transactions(self, account_number):
        return [upi for upi in self.upi_transactions if upi["account_number"] == account_number]

    def get_daily_upi_count(self, account_number, date_str=None):
        from datetime import date
        if date_str is None:
            date_str = date.today().isoformat()
        
        key = f"{account_number}:{date_str}"
        return self.daily_upi_counts.get(key, 0)

    def get_upi_transactions_by_date(self, account_number, date_str):
        return [
            upi for upi in self.upi_transactions 
            if upi["account_number"] == account_number and upi["date"] == date_str
        ]

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


class UPI(Transaction):
    def __init__(self) -> None:
        self.upi_payments = [
            {"id": 1, "account_number": "1234567890", "amount": 150.0, "upi_id": "user1@paytm", "type": "upi", "upi_category": "p2p", "recipient_upi": "friend1@paytm", "description": "Money transfer to friend"},
            {"id": 2, "account_number": "0987654321", "amount": 250.0, "upi_id": "user2@gpay", "type": "upi", "upi_category": "merchant", "recipient_upi": "shop@merchant", "description": "Online shopping payment"},
            {"id": 3, "account_number": "1122334455", "amount": 75.0, "upi_id": "user3@phonepe", "type": "upi", "upi_category": "p2p", "recipient_upi": "family@phonepe", "description": "Family money transfer"},
            {"id": 4, "account_number": "1234567890", "amount": 300.0, "upi_id": "user1@paytm", "type": "upi", "upi_category": "p2p", "recipient_upi": "colleague@gpay", "description": "Lunch money split"},
            {"id": 5, "account_number": "0987654321", "amount": 500.0, "upi_id": "user2@gpay", "type": "upi", "upi_category": "bill_payment", "recipient_upi": "electricity@bill", "description": "Electricity bill payment"},
        ]

    def create_upi_payment(self, account_number, amount, upi_id, upi_category="p2p", recipient_upi=None, description=""):
        # use the self.upi_payments list to create a new UPI payment transaction
        upi_payment = {
            "id": len(self.upi_payments) + 1, 
            "account_number": account_number, 
            "amount": amount,
            "upi_id": upi_id,
            "type": "upi",
            "upi_category": upi_category,
            "recipient_upi": recipient_upi,
            "description": description
        }
        self.upi_payments.append(upi_payment)
        return upi_payment
    
    def get_upi_payment(self, transaction_id):
        # use the self.upi_payments list to get the UPI payment transaction details
        for upi_payment in self.upi_payments:
            if upi_payment["id"] == transaction_id:
                return upi_payment
        return None

    def list_upi_payments(self, account_number=None):
        # use the self.upi_payments list to get all UPI payment transactions
        if account_number:
            return [upi_payment for upi_payment in self.upi_payments if upi_payment["account_number"] == account_number]
        return self.upi_payments

    def list_p2p_upi_payments(self, account_number=None):
        # use the self.upi_payments list to get all P2P UPI payment transactions
        p2p_payments = [upi_payment for upi_payment in self.upi_payments if upi_payment.get("upi_category") == "p2p"]
        if account_number:
            return [upi_payment for upi_payment in p2p_payments if upi_payment["account_number"] == account_number]
        return p2p_payments

from models.transaction import UPI

class UPIService:
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
from dataclasses import dataclass
from typing import List, Dict
from enum import Enum
import smtplib
from email.message import EmailMessage

class OrderStatus(Enum):
    PENDING = "PENDING"
    INVALID = "INVALID"
    OUT_OF_STOCK = "OUT_OF_STOCK"
    PAYMENT_FAILED = "PAYMENT_FAILED"
    COMPLETED = "COMPLETED"
    ERROR = "ERROR"

@dataclass
class OrderItem:
    product_id: str
    quantity: int
    price: float

@dataclass
class Order:
    order_id: str
    customer_email: str
    items: List[OrderItem]
    payment_method: str
    total_amount: float = 0
    status: OrderStatus = OrderStatus.PENDING

class OrderProcessor:
    def __init__(self):
        self.inventory: Dict[str, int] = {}
        
    def calculate_total(self, items: List[OrderItem]) -> float:
        return sum(item.price * item.quantity for item in items)
    
    def validate_order(self, order: Order) -> bool:
        if not order or not order.items or not order.customer_email:
            return False
        order.total_amount = self.calculate_total(order.items)
        return order.total_amount > 0
    
    def check_inventory(self, order: Order) -> bool:
        for item in order.items:
            if self.inventory.get(item.product_id, 0) < item.quantity:
                return False
        return True
    
    def process_payment(self, order: Order) -> bool:
        # Simplified payment processing
        return order.total_amount > 0 and order.payment_method is not None
    
    def update_inventory(self, order: Order) -> None:
        for item in order.items:
            current_stock = self.inventory.get(item.product_id, 0)
            self.inventory[item.product_id] = current_stock - item.quantity
    
    def send_confirmation_email(self, order: Order) -> None:
        # Simplified email sending logic
        print(f"Order confirmation sent to: {order.customer_email}")
    
    def process_order(self, order: Order) -> bool:
        try:
            # Validate order
            if not self.validate_order(order):
                order.status = OrderStatus.INVALID
                return False
            
            # Check inventory
            if not self.check_inventory(order):
                order.status = OrderStatus.OUT_OF_STOCK
                return False
            
            # Process payment
            if not self.process_payment(order):
                order.status = OrderStatus.PAYMENT_FAILED
                return False
            
            # Update inventory
            self.update_inventory(order)
            
            # Send confirmation
            self.send_confirmation_email(order)
            
            order.status = OrderStatus.COMPLETED
            return True
            
        except Exception as e:
            print(f"Error processing order: {str(e)}")
            order.status = OrderStatus.ERROR
            return False

# Usage Example
if __name__ == "__main__":
    processor = OrderProcessor()
    
    # Initialize some inventory
    processor.inventory = {
        "PROD1": 10,
        "PROD2": 5
    }
    
    # Create sample order
    order = Order(
        order_id="ORD123",
        customer_email="customer@example.com",
        items=[
            OrderItem(product_id="PROD1", quantity=2, price=10.0),
            OrderItem(product_id="PROD2", quantity=1, price=20.0)
        ],
        payment_method="CREDIT_CARD"
    )
    
    # Process the order
    success = processor.process_order(order)
    print(f"Order processing {'successful' if success else 'failed'}")
    print(f"Order status: {order.status}")
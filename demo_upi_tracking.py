#!/usr/bin/env python3
"""
UPI Transaction Count Tracking Demo

This script demonstrates the UPI transaction count tracking feature
that tracks daily UPI transactions per account.
"""

import sys
import os
from datetime import date, datetime

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from services.upi_service import UPIService

def main():
    print("🏦 Banking API - UPI Transaction Count Tracking Demo")
    print("=" * 60)
    
    # Initialize UPI service
    upi_service = UPIService()
    
    # Demo account
    account_number = "1234567890"
    today = date.today().isoformat()
    
    print(f"📅 Today's Date: {today}")
    print(f"💳 Account Number: {account_number}")
    print()
    
    # Check initial count
    initial_count = upi_service.get_daily_upi_count(account_number)
    print(f"📊 Initial UPI transaction count for today: {initial_count}")
    print()
    
    # Create some UPI transactions
    print("🔄 Creating UPI transactions...")
    
    transactions = [
        {"amount": 500.0, "upi_id": "user@paytm", "recipient_upi": "coffee@gpay", "description": "Coffee purchase"},
        {"amount": 1200.0, "upi_id": "user@paytm", "recipient_upi": "grocery@phonepe", "description": "Grocery shopping"},
        {"amount": 250.0, "upi_id": "user@paytm", "recipient_upi": "fuel@paytm", "description": "Fuel payment"},
        {"amount": 800.0, "upi_id": "user@paytm", "recipient_upi": "restaurant@gpay", "description": "Dinner"},
    ]
    
    created_transactions = []
    for i, txn in enumerate(transactions, 1):
        print(f"  {i}. Creating transaction: ₹{txn['amount']} to {txn['recipient_upi']} ({txn['description']})")
        
        created_txn = upi_service.create_upi_transaction(
            account_number, 
            txn['amount'], 
            txn['upi_id'], 
            txn['recipient_upi']
        )
        created_transactions.append(created_txn)
        
        # Show updated count after each transaction
        current_count = upi_service.get_daily_upi_count(account_number)
        print(f"     ✅ Transaction created (ID: {created_txn['id']}) - Daily count: {current_count}")
        print()
    
    # Show final daily summary
    print("📈 Daily UPI Transaction Summary:")
    print("-" * 40)
    
    summary = upi_service.get_account_daily_summary(account_number, today)
    
    print(f"Account Number: {summary['account_number']}")
    print(f"Date: {summary['date']}")
    print(f"Total Transactions: {summary['transaction_count']}")
    print(f"Total Amount: ₹{summary['total_amount']}")
    print()
    
    print("📋 Transaction Details:")
    for txn in summary['transactions']:
        timestamp = txn['timestamp'].strftime('%H:%M:%S') if isinstance(txn['timestamp'], datetime) else str(txn['timestamp'])
        print(f"  • ID {txn['id']}: ₹{txn['amount']} from {txn['upi_id']} to {txn['recipient_upi']} at {timestamp}")
    
    print()
    print("🎯 Key Features Demonstrated:")
    print("  ✓ UPI transaction creation with detailed metadata")
    print("  ✓ Daily transaction count tracking per account")
    print("  ✓ Date-specific transaction counting")
    print("  ✓ Daily summary with total count and amount")
    print("  ✓ Transaction history retrieval")
    print()
    
    # Show API endpoints that would be available
    print("🌐 Available API Endpoints:")
    print("  POST /transactions/upi - Create UPI transaction")
    print("  GET  /transactions/upi/<id> - Get UPI transaction by ID")
    print("  GET  /transactions/upi?account_number=<num> - List UPI transactions")
    print("  GET  /transactions/upi/count/<account_number> - Get daily count")
    print("  GET  /transactions/upi/summary/<account_number> - Get daily summary")
    print()
    print("✨ Demo completed successfully!")

if __name__ == "__main__":
    main()
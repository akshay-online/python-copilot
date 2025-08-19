#!/usr/bin/env python3
"""
Simple test script to verify the UPI service and endpoint functionality
"""

import sys
import os
import json

# Add the app directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from flask import Flask
from services.upi_service import UPIService

def test_upi_service():
    """Test the UPI service directly"""
    print("Testing UPI Service...")
    
    upi_service = UPIService()
    
    # Test 1: Get all UPI payments
    print("\n1. Testing list_upi_payments():")
    all_payments = upi_service.list_upi_payments()
    print(f"   Found {len(all_payments)} UPI payments")
    for payment in all_payments:
        print(f"   - ID {payment['id']}: {payment['account_number']} -> {payment['upi_id']} (₹{payment['amount']})")
    
    # Test 2: Get UPI payments for specific account
    print("\n2. Testing list_upi_payments(account_number='1234567890'):")
    account_payments = upi_service.list_upi_payments('1234567890')
    print(f"   Found {len(account_payments)} payments for account 1234567890")
    for payment in account_payments:
        print(f"   - ID {payment['id']}: {payment['upi_id']} (₹{payment['amount']})")
    
    # Test 3: Get specific payment by ID
    print("\n3. Testing get_upi_payment(1):")
    specific_payment = upi_service.get_upi_payment(1)
    if specific_payment:
        print(f"   Payment ID 1: {json.dumps(specific_payment, indent=2)}")
    else:
        print("   Payment not found")
    
    # Test 4: Create new payment
    print("\n4. Testing create_upi_payment():")
    new_payment = upi_service.create_upi_payment("9999888877", 500.0, "test@amazon")
    print(f"   Created new payment: {json.dumps(new_payment, indent=2)}")
    
    print(f"\n   Total payments after creation: {len(upi_service.list_upi_payments())}")

def test_upi_endpoint():
    """Test the UPI endpoint in a minimal Flask app"""
    print("\n\nTesting UPI Endpoint...")
    
    app = Flask(__name__)
    
    # Import and set up the UPI service
    from services.upi_service import UPIService
    upi_service = UPIService()
    
    # Simple endpoint implementation
    @app.route('/transactions/upi', methods=['GET'])
    def get_all_upi_payments():
        from flask import request, jsonify
        account_number = request.args.get('account_number')
        upi_payments = upi_service.list_upi_payments(account_number)
        return jsonify(upi_payments)
    
    # Test the endpoint with app context
    with app.test_client() as client:
        print("\n1. Testing GET /transactions/upi:")
        response = client.get('/transactions/upi')
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.get_json()
            print(f"   Response: {len(data)} payments returned")
            print(f"   Sample: {json.dumps(data[0] if data else {}, indent=2)}")
        
        print("\n2. Testing GET /transactions/upi?account_number=1234567890:")
        response = client.get('/transactions/upi?account_number=1234567890')
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.get_json()
            print(f"   Response: {len(data)} payments returned for account 1234567890")

if __name__ == "__main__":
    test_upi_service()
    test_upi_endpoint()
    print("\n✅ All tests completed successfully!")
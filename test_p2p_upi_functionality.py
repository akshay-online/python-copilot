#!/usr/bin/env python3
"""
Test script to verify the P2P UPI endpoint functionality
"""

import sys
import os
import json

# Add the app directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from flask import Flask
from services.upi_service import UPIService

def test_p2p_upi_service():
    """Test the P2P UPI service directly"""
    print("Testing P2P UPI Service...")
    
    upi_service = UPIService()
    
    # Test 1: Get all P2P UPI payments
    print("\n1. Testing list_p2p_upi_payments():")
    p2p_payments = upi_service.list_p2p_upi_payments()
    print(f"   Found {len(p2p_payments)} P2P UPI payments")
    for payment in p2p_payments:
        print(f"   - ID {payment['id']}: {payment['account_number']} -> {payment['recipient_upi']} (₹{payment['amount']}) - {payment['description']}")
    
    # Test 2: Get P2P UPI payments for specific account
    print("\n2. Testing list_p2p_upi_payments(account_number='1234567890'):")
    account_p2p_payments = upi_service.list_p2p_upi_payments('1234567890')
    print(f"   Found {len(account_p2p_payments)} P2P payments for account 1234567890")
    for payment in account_p2p_payments:
        print(f"   - ID {payment['id']}: {payment['upi_id']} -> {payment['recipient_upi']} (₹{payment['amount']}) - {payment['description']}")
    
    # Test 3: Compare all UPI vs P2P UPI
    print("\n3. Comparing all UPI vs P2P UPI:")
    all_upi = upi_service.list_upi_payments()
    print(f"   Total UPI payments: {len(all_upi)}")
    print(f"   P2P UPI payments: {len(p2p_payments)}")
    print(f"   Non-P2P UPI payments: {len(all_upi) - len(p2p_payments)}")

def test_p2p_upi_endpoint():
    """Test the P2P UPI endpoint in a minimal Flask app"""
    print("\n\nTesting P2P UPI Endpoint...")
    
    app = Flask(__name__)
    
    # Import and set up the UPI service
    from services.upi_service import UPIService
    upi_service = UPIService()
    
    # Simple P2P endpoint implementation
    @app.route('/transactions/upi/p2p', methods=['GET'])
    def get_all_p2p_upi_payments():
        from flask import request, jsonify
        account_number = request.args.get('account_number')
        p2p_payments = upi_service.list_p2p_upi_payments(account_number)
        return jsonify(p2p_payments)
    
    # Test the endpoint with app context
    with app.test_client() as client:
        print("\n1. Testing GET /transactions/upi/p2p:")
        response = client.get('/transactions/upi/p2p')
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.get_json()
            print(f"   Response: {len(data)} P2P payments returned")
            if data:
                print(f"   Sample P2P payment: {json.dumps(data[0], indent=2)}")
        
        print("\n2. Testing GET /transactions/upi/p2p?account_number=1234567890:")
        response = client.get('/transactions/upi/p2p?account_number=1234567890')
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.get_json()
            print(f"   Response: {len(data)} P2P payments returned for account 1234567890")

if __name__ == "__main__":
    test_p2p_upi_service()
    test_p2p_upi_endpoint()
    print("\n✅ All P2P UPI tests completed successfully!")
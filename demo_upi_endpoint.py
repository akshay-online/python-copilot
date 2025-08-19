#!/usr/bin/env python3
"""
Demonstration of the UPI Payment Details Endpoint
Shows the API response format and functionality
"""

import sys
import os
import json

# Add the app directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from flask import Flask, request, jsonify
from services.upi_service import UPIService

def create_demo_app():
    """Create a minimal Flask app with just the UPI endpoint"""
    app = Flask(__name__)
    upi_service = UPIService()
    
    @app.route('/transactions/upi', methods=['GET'])
    def get_all_upi_payments():
        """
        Get all UPI payment details.
        Query parameter: account_number (optional) - Filter by account number
        """
        account_number = request.args.get('account_number')
        upi_payments = upi_service.list_upi_payments(account_number)
        return jsonify(upi_payments)
    
    return app

def demonstrate_endpoint():
    """Demonstrate the UPI endpoint functionality"""
    print("=" * 60)
    print("UPI PAYMENT DETAILS ENDPOINT DEMONSTRATION")
    print("=" * 60)
    
    app = create_demo_app()
    
    with app.test_client() as client:
        print("\n1. GET /transactions/upi")
        print("   Description: Get all UPI payment details")
        print("   " + "-" * 45)
        
        response = client.get('/transactions/upi')
        data = response.get_json()
        
        print(f"   Status Code: {response.status_code}")
        print(f"   Content-Type: {response.content_type}")
        print(f"   Response Body:")
        print("   " + json.dumps(data, indent=4))
        
        print("\n2. GET /transactions/upi?account_number=1234567890")
        print("   Description: Get UPI payments filtered by account number")
        print("   " + "-" * 55)
        
        response = client.get('/transactions/upi?account_number=1234567890')
        data = response.get_json()
        
        print(f"   Status Code: {response.status_code}")
        print(f"   Content-Type: {response.content_type}")
        print(f"   Response Body:")
        print("   " + json.dumps(data, indent=4))
        
        print("\n3. GET /transactions/upi?account_number=9999999999")
        print("   Description: Get UPI payments for non-existent account")
        print("   " + "-" * 54)
        
        response = client.get('/transactions/upi?account_number=9999999999')
        data = response.get_json()
        
        print(f"   Status Code: {response.status_code}")
        print(f"   Content-Type: {response.content_type}")
        print(f"   Response Body:")
        print("   " + json.dumps(data, indent=4))
    
    print("\n" + "=" * 60)
    print("ENDPOINT SUMMARY")
    print("=" * 60)
    print("Endpoint: GET /transactions/upi")
    print("Query Parameters:")
    print("  - account_number (optional): Filter UPI payments by account number")
    print("\nResponse Format:")
    print("  - Array of UPI payment objects")
    print("  - Each object contains: id, account_number, amount, upi_id, type")
    print("\nFunctionality:")
    print("  ✅ Returns all UPI payment details when no filter applied")
    print("  ✅ Filters by account number when parameter provided")
    print("  ✅ Returns empty array for non-existent accounts")
    print("  ✅ Consistent with existing transaction endpoints")
    print("=" * 60)

if __name__ == "__main__":
    demonstrate_endpoint()
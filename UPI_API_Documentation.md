# UPI Payment Details API Endpoint

## Overview
This document describes the UPI payment details endpoint that was added to the Banking API.

## Endpoint Details

### GET /transactions/upi

Retrieves all UPI payment details from the system.

**URL:** `GET /transactions/upi`

**Query Parameters:**
- `account_number` (optional, string): Filter UPI payments by specific account number

**Response Format:**
```json
[
    {
        "id": 1,
        "account_number": "1234567890",
        "amount": 150.0,
        "upi_id": "user1@paytm",
        "type": "upi"
    },
    {
        "id": 2,
        "account_number": "0987654321",
        "amount": 250.0,
        "upi_id": "user2@gpay",
        "type": "upi"
    }
]
```

## Usage Examples

### 1. Get All UPI Payments
```bash
curl -X GET "http://localhost:5000/transactions/upi"
```

### 2. Get UPI Payments for Specific Account
```bash
curl -X GET "http://localhost:5000/transactions/upi?account_number=1234567890"
```

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Unique identifier for the UPI payment |
| `account_number` | string | Bank account number associated with the payment |
| `amount` | number | Payment amount in currency units |
| `upi_id` | string | UPI ID used for the transaction (e.g., user@paytm) |
| `type` | string | Transaction type, always "upi" for UPI payments |

## HTTP Status Codes

- `200 OK`: Request successful, returns array of UPI payments
- `400 Bad Request`: Invalid query parameters (if implemented)
- `500 Internal Server Error`: Server error occurred

## Implementation Details

The UPI payment endpoint follows the same architectural patterns as existing transaction endpoints:

- **Model**: `UPI` class in `app/models/transaction.py`
- **Service**: `UPIService` class in `app/services/upi_service.py`
- **Route**: Defined in `app/routes/transaction_routes.py`
- **Tests**: Comprehensive test suite in `tests/test_upi.py`

## Sample Data

The system includes sample UPI payment data for testing:

```json
[
    {
        "id": 1,
        "account_number": "1234567890",
        "amount": 150.0,
        "upi_id": "user1@paytm",
        "type": "upi"
    },
    {
        "id": 2,
        "account_number": "0987654321",
        "amount": 250.0,
        "upi_id": "user2@gpay",
        "type": "upi"
    },
    {
        "id": 3,
        "account_number": "1122334455",
        "amount": 75.0,
        "upi_id": "user3@phonepe",
        "type": "upi"
    }
]
```

## Integration with Swagger

The endpoint is documented with Swagger/OpenAPI specifications and will appear in the API documentation under the "Transactions" tag.

## Testing

Run the UPI-specific tests:
```bash
python -m unittest tests.test_upi -v
```

Or run all tests:
```bash
python -m unittest discover tests -v
```
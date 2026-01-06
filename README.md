# Banking API

This project is a Python API for banking transactions. It provides endpoints for managing bank accounts, loans, offers, and performing transactions, **including UPI transaction tracking with daily count monitoring**.

## New Feature: UPI Transaction Count Tracking 📱💰

The API now supports UPI (Unified Payments Interface) transactions with comprehensive daily tracking:

### Features
- **Create UPI transactions** with sender and recipient UPI IDs
- **Track daily transaction count** per account automatically  
- **Get real-time count** of UPI transactions for any account on any date
- **Daily summary** with transaction count, total amount, and transaction details
- **Historical tracking** with date-specific queries

### UPI API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/transactions/upi` | Create a new UPI transaction |
| `GET` | `/transactions/upi/<id>` | Get UPI transaction by ID |
| `GET` | `/transactions/upi?account_number=<num>` | List UPI transactions for account |
| `GET` | `/transactions/upi/count/<account_number>` | Get daily UPI transaction count |
| `GET` | `/transactions/upi/summary/<account_number>` | Get daily summary with count and total amount |

### Example Usage

**Create UPI Transaction:**
```bash
POST /transactions/upi
{
  "account_number": "1234567890",
  "amount": 500.0,
  "upi_id": "user@paytm",
  "recipient_upi": "merchant@gpay"
}
```

**Get Daily Count:**
```bash
GET /transactions/upi/count/1234567890?date=2026-01-06
# Response: {"account_number": "1234567890", "date": "2026-01-06", "upi_transaction_count": 5}
```

**Get Daily Summary:**
```bash
GET /transactions/upi/summary/1234567890
# Response includes: transaction_count, total_amount, and list of transactions
```

### Demo Script
Run the demo to see UPI tracking in action:
```bash
python demo_upi_tracking.py
```

## Project Structure
```plaintext
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── account.py
│   │   ├── loans.py
│   │   ├── offer.py
│   │   └── transaction.py          # 🆕 Now includes UPITransaction class
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── account_routes.py
│   │   ├── loans_routes.py
│   │   ├── offer_routes.py
│   │   └── transaction_routes.py   # 🆕 Now includes UPI endpoints
│   └── services/
│       ├── __init__.py
│       ├── account_service.py
│       ├── loans_service.py
│       ├── offer_service.py
│       ├── transaction_service.py
│       └── upi_service.py          # 🆕 New UPI service for tracking
├── tests/
│   ├── __init__.py
│   ├── test_accounts.py
│   ├── test_transactions.py
│   └── test_upi_transactions.py    # 🆕 Comprehensive UPI tests
├── demo_upi_tracking.py            # 🆕 Interactive demo script
├── config.py
├── requirements.txt
├── .gitignore
└── README.md
```

The project has the following files and directories:

- `app/`: Contains the main application code.
  - `__init__.py`: Marks the `app` directory as a Python package.
  - `main.py`: Entry point of the application. Sets up the Flask app and routes.
  - `models/`: Contains the data models for accounts, loans, offers, and transactions.
    - `__init__.py`: Marks the `models` directory as a Python package.
    - `account.py`: Defines the `Account` class for bank accounts.
    - `loans.py`: Defines the `Loans` class for bank loans.
    - `offer.py`: Defines the `Offer` class for bank offers.
    - `transaction.py`: Defines the `Transaction` class for bank transactions.
  - `routes/`: Contains the API routes for accounts, loans, offers, and transactions.
    - `__init__.py`: Marks the `routes` directory as a Python package.
    - `account_routes.py`: Defines the routes for account-related APIs.
    - `loans_routes.py`: Defines the routes for loans-related APIs.
    - `offer_routes.py`: Defines the routes for offer-related APIs.
    - `transaction_routes.py`: Defines the routes for transaction-related APIs.
  - `services/`: Contains the service classes for accounts, loans, offers, and transactions.
    - `__init__.py`: Marks the `services` directory as a Python package.
    - `account_service.py`: Provides methods for interacting with the `Account` model.
    - `loans_service.py`: Provides methods for interacting with the `Loans` model.
    - `offer_service.py`: Provides methods for interacting with the `Offer` model.
    - `transaction_service.py`: Provides methods for interacting with the `Transaction` model.
- `tests/`: Contains the test cases for the APIs.
  - `__init__.py`: Marks the `tests` directory as a Python package.
  - `test_accounts.py`: Contains test cases for the account-related APIs.
  - `test_transactions.py`: Contains test cases for the transaction-related APIs.
- `config.py`: Contains configuration settings for the application.
- `requirements.txt`: Lists the dependencies required for the project.
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `README.md`: Provides an overview of the project and instructions for setup and usage.

## Getting Started

To set up and run the banking API, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/banking-api.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Configure the database connection in `config.py`.
4. Run the application: `python app/main.py`

## API Documentation

The API documentation can be found in the individual route files in the `app/routes` directory. Each route file contains the endpoint URLs and the request/response formats.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Authors

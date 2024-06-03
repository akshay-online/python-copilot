from flask import Blueprint, request, jsonify
from models.transaction import Transaction
from services.transaction_service import TransactionService
from models.transaction import Transaction

transaction_routes = Blueprint('transaction_routes', __name__)
transaction_service = TransactionService()


@transaction_routes.route('/transactions', methods=['POST'])
def create_transaction():
    """
    Create a new transaction.

    Returns:
        A JSON response with a success message.
    """
    data = request.get_json()
    transaction = Transaction(data['account_number'], data['amount'])
    transaction_service.create_transaction(transaction)
    return jsonify({'message': 'Transaction created successfully'})

@transaction_routes.route('/transactions/<transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    """
    Get a transaction by its ID.

    Args:
        transaction_id: The ID of the transaction.

    Returns:
        A JSON response with the transaction details if found, or a message if not found.
    """
    transaction = transaction_service.get_transaction(transaction_id)
    if transaction:
        return jsonify(transaction.__dict__)
    else:
        return jsonify({'message': 'Transaction not found'})

# Mock data for testing purposes
mock_transactions = [
    {
        'id': 1,
        'account_number': '1234567890',
        'amount': 100.0,
        'type': 'deposit'
    },
    {
        'id': 2,
        'account_number': '0987654321',
        'amount': 50.0,
        'type': 'withdrawal'
    }
]

@transaction_routes.route('/transactions/mock', methods=['GET'])
def get_mock_transactions():
    """
    Get mock transactions for testing purposes.

    Returns:
        A JSON response with a list of mock transaction details.
    """
    return jsonify(mock_transactions)

@transaction_routes.route('/transactions', methods=['GET'])
def list_transactions():
    """
    List all transactions.

    Returns:
        A JSON response with a list of transaction details.
    """
    account_number = request.args.get('account_number')
    transactions = transaction_service.list_transactions(account_number)
    return jsonify([transaction.__dict__ for transaction in transactions])

# add withdrawal and deposit routes
@transaction_routes.route('/transactions/withdrawal', methods=['POST'])
def create_withdrawal():
    """
    Create a new withdrawal transaction.

    Returns:
        A JSON response with a success message.
    """
    data = request.get_json()
    transaction = Transaction(data['account_number'], data['amount'])
    transaction_service.create_withdrawal(transaction)
    return jsonify({'message': 'Withdrawal created successfully'})

@transaction_routes.route('/transactions/deposit', methods=['POST'])
def create_deposit():
    """
    Create a new deposit transaction.

    Returns:
        A JSON response with a success message.
    """
    data = request.get_json()
    transaction = Transaction(data['account_number'], data['amount'])
    transaction_service.create_deposit(transaction)
    return jsonify({'message': 'Deposit created successfully'})

@transaction_routes.route('/transactions/withdrawal/<transaction_id>', methods=['GET'])
def get_withdrawal(transaction_id):
    """
    Get a withdrawal transaction by its ID.

    Args:
        transaction_id: The ID of the withdrawal transaction.

    Returns:
        A JSON response with the withdrawal transaction details if found, or a message if not found.
    """
    transaction = transaction_service.get_withdrawal(transaction_id)
    if transaction:
        return jsonify(transaction.__dict__)
    else:
        return jsonify({'message': 'Withdrawal not found'})
    
@transaction_routes.route('/transactions/deposit/<transaction_id>', methods=['GET'])
def get_deposit(transaction_id):
    """
    Get a deposit transaction by its ID.

    Args:
        transaction_id: The ID of the deposit transaction.

    Returns:
        A JSON response with the deposit transaction details if found, or a message if not found.
    """
    transaction = transaction_service.get_deposit(transaction_id)
    if transaction:
        return jsonify(transaction.__dict__)
    else:
        return jsonify({'message': 'Deposit not found'})

@transaction_routes.route('/transactions/withdrawal', methods=['GET'])
def list_withdrawals():
    """
    List all withdrawal transactions.

    Returns:
        A JSON response with a list of withdrawal transaction details.
    """
    account_number = request.args.get('account_number')
    transactions = transaction_service.list_withdrawals(account_number)
    return jsonify([transaction.__dict__ for transaction in transactions])

# List all deposit transactions
@transaction_routes.route('/transactions/deposit', methods=['GET'])
def list_deposits():
    """
    List all deposit transactions.

    Returns:
        A JSON response with a list of deposit transaction details.
    """
    account_number = request.args.get('account_number')
    transactions = transaction_service.list_deposits(account_number)
    return jsonify([transaction.__dict__ for transaction in transactions])
from flask import Blueprint, request, jsonify
from models.transaction import Transaction
from services.deposit_service import DepositService
from services.transaction_service import TransactionService
from services.withdrawal_service import WithdrawalService
from services.upi_service import UPIService
from flask import Blueprint, request, jsonify
from models.transaction import Transaction

from flasgger import swag_from


transaction_routes = Blueprint('transaction_routes', __name__)
transaction_service = TransactionService()
withdrawal_service = WithdrawalService()
deposit_service = DepositService()
upi_service = UPIService()

@transaction_routes.route('/transactions', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'type': 'object',
                'properties': {
                    'account_number': {
                        'type': 'string',
                        'description': 'The account number'
                    },
                    'amount': {
                        'type': 'number',
                        'description': 'The transaction amount'
                    }
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Transaction created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'description': 'Success message'
                    }
                }
            }
        }
    }
})
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
@swag_from({
    'tags': ['Transactions'],
    'description': 'Get a transaction by its ID',
    'parameters': [
        {
            'name': 'transaction_id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'The ID of the transaction'
        }
    ],
    'responses': {
        '200': {
            'description': 'Transaction details',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {
                        'type': 'integer',
                        'description': 'Transaction ID'
                    },
                    'account_number': {
                        'type': 'string',
                        'description': 'The account number'
                    },
                    'amount': {
                        'type': 'number',
                        'description': 'The transaction amount'
                    },
                    'type': {
                        'type': 'string',
                        'description': 'The transaction type'
                    }
                }
            }
        },
        '404': {
            'description': 'Transaction not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'description': 'Error message'
                    }
                }
            }
        }
    }
})
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

@transaction_routes.route('/transactions', methods=['GET'])
@swag_from({
    'tags': ['Transactions'],
    'description': 'List all transactions',
    'parameters': [
        {
            'name': 'account_number',
            'in': 'query',
            'required': False,
            'type': 'string',
            'description': 'Filter transactions by account number'
        }
    ],
    'responses': {
        '200': {
            'description': 'List of transaction details',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {
                            'type': 'integer',
                            'description': 'Transaction ID'
                        },
                        'account_number': {
                            'type': 'string',
                            'description': 'The account number'
                        },
                        'amount': {
                            'type': 'number',
                            'description': 'The transaction amount'
                        },
                        'type': {
                            'type': 'string',
                            'description': 'The transaction type'
                        }
                    }
                }
            }
        }
    }
})
def list_transactions():
    account_number = request.args.get('account_number')
    transactions = transaction_service.list_transactions(account_number)
    return jsonify([transaction.__dict__ for transaction in transactions])

# add withdrawal and deposit routes
@transaction_routes.route('/transactions/withdrawal', methods=['POST'])
@swag_from({
    'tags': ['Transactions'],
    'description': 'Create a new withdrawal transaction',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'account_number': {
                        'type': 'string',
                        'description': 'The account number'
                    },
                    'amount': {
                        'type': 'number',
                        'description': 'The transaction amount'
                    }
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Withdrawal created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'description': 'Success message'
                    }
                }
            }
        }
    }
})
def create_withdrawal():
    """
    Create a new withdrawal transaction.

    Returns:
        A JSON response with a success message.
    """
    data = request.get_json()
    transaction = Transaction(data['account_number'], data['amount'])
    withdrawal_service.create_withdrawal(transaction)
    return jsonify({'message': 'Withdrawal created successfully'})

@transaction_routes.route('/transactions/deposit', methods=['POST'])
@swag_from({
    'tags': ['Transactions'],
    'description': 'Create a new deposit transaction',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'account_number': {
                        'type': 'string',
                        'description': 'The account number'
                    },
                    'amount': {
                        'type': 'number',
                        'description': 'The transaction amount'
                    }
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Deposit created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'description': 'Success message'
                    }
                }
            }
        }
    }
})
def create_deposit():
    """
    Create a new deposit transaction.

    Returns:
        A JSON response with a success message.
    """
    data = request.get_json()
    transaction = Transaction(data['account_number'], data['amount'])
    deposit_service.create_deposit(transaction)
    return jsonify({'message': 'Deposit created successfully'})

@transaction_routes.route('/transactions/withdrawal/<transaction_id>', methods=['GET'])
@swag_from({
    'tags': ['Transactions'],
    'description': 'Get a withdrawal transaction by its ID',
    'parameters': [
        {
            'name': 'transaction_id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'The ID of the withdrawal transaction'
        }
    ],
    'responses': {
        '200': {
            'description': 'Withdrawal transaction details',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {
                        'type': 'integer',
                        'description': 'Transaction ID'
                    },
                    'account_number': {
                        'type': 'string',
                        'description': 'The account number'
                    },
                    'amount': {
                        'type': 'number',
                        'description': 'The transaction amount'
                    },
                    'type': {
                        'type': 'string',
                        'description': 'The transaction type'
                    }
                }
            }
        },
        '404': {
            'description': 'Withdrawal not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'description': 'Error message'
                    }
                }
            }
        }
    }
})
def get_withdrawal(transaction_id):
    """
    Get a withdrawal transaction by its ID.

    Args:
        transaction_id: The ID of the withdrawal transaction.

    Returns:
        A JSON response with the withdrawal transaction details if found, or a message if not found.
    """
    transaction = withdrawal_service.get_withdrawal(transaction_id)
    if transaction:
        return jsonify(transaction.__dict__)
    else:
        return jsonify({'message': 'Withdrawal not found'})

@transaction_routes.route('/transactions/deposit/<transaction_id>', methods=['GET'])
@swag_from({
    'tags': ['Transactions'],
    'description': 'Get a deposit transaction by its ID',
    'parameters': [
        {
            'name': 'transaction_id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'The ID of the deposit transaction'
        }
    ],
    'responses': {
        '200': {
            'description': 'Deposit transaction details',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {
                        'type': 'integer',
                        'description': 'Transaction ID'
                    },
                    'account_number': {
                        'type': 'string',
                        'description': 'The account number'
                    },
                    'amount': {
                        'type': 'number',
                        'description': 'The transaction amount'
                    },
                    'type': {
                        'type': 'string',
                        'description': 'The transaction type'
                    }
                }
            }
        },
        '404': {
            'description': 'Deposit not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'description': 'Error message'
                    }
                }
            }
        }
    }
})
def get_deposit(transaction_id):
    """
    Get a deposit transaction by its ID.

    Args:
        transaction_id: The ID of the deposit transaction.

    Returns:
        A JSON response with the deposit transaction details if found, or a message if not found.
    """
    transaction = deposit_service.get_deposit(transaction_id)
    if transaction:
        return jsonify(transaction.__dict__)
    else:
        return jsonify({'message': 'Deposit not found'})

@transaction_routes.route('/transactions/withdrawal', methods=['GET'])
@swag_from({
    'tags': ['Transactions'],
    'description': 'List all withdrawal transactions',
    'parameters': [
        {
            'name': 'account_number',
            'in': 'query',
            'required': False,
            'type': 'string',
            'description': 'Filter withdrawal transactions by account number'
        }
    ],
    'responses': {
        '200': {
            'description': 'List of withdrawal transaction details',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {
                            'type': 'integer',
                            'description': 'Transaction ID'
                        },
                        'account_number': {
                            'type': 'string',
                            'description': 'The account number'
                        },
                        'amount': {
                            'type': 'number',
                            'description': 'The transaction amount'
                        },
                        'type': {
                            'type': 'string',
                            'description': 'The transaction type'
                        }
                    }
                }
            }
        }
    }
})
def list_withdrawals():
    """
    List all withdrawal transactions.

    Returns:
        A JSON response with a list of withdrawal transaction details.
    """
    account_number = request.args.get('account_number')
    transactions = withdrawal_service.list_withdrawals(account_number)
    return jsonify([transaction.__dict__ for transaction in transactions])

@transaction_routes.route('/transactions/deposit', methods=['GET'])
@swag_from({
    'tags': ['Transactions'],
    'description': 'List all deposit transactions',
    'parameters': [
        {
            'name': 'account_number',
            'in': 'query',
            'required': False,
            'type': 'string',
            'description': 'Filter deposit transactions by account number'
        }
    ],
    'responses': {
        '200': {
            'description': 'List of deposit transaction details',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {
                            'type': 'integer',
                            'description': 'Transaction ID'
                        },
                        'account_number': {
                            'type': 'string',
                            'description': 'The account number'
                        },
                        'amount': {
                            'type': 'number',
                            'description': 'The transaction amount'
                        },
                        'type': {
                            'type': 'string',
                            'description': 'The transaction type'
                        }
                    }
                }
            }
        }
    }
})
def list_deposits():
    """
    List all deposit transactions.

    Returns:
        A JSON response with a list of deposit transaction details.
    """
    account_number = request.args.get('account_number')
    transactions = deposit_service.list_deposits(account_number)
    return jsonify([transaction.__dict__ for transaction in transactions])


# UPI Transaction Routes
@transaction_routes.route('/transactions/upi', methods=['POST'])
@swag_from({
    'tags': ['UPI Transactions'],
    'description': 'Create a new UPI transaction',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'account_number': {
                        'type': 'string',
                        'description': 'The account number'
                    },
                    'amount': {
                        'type': 'number',
                        'description': 'The transaction amount'
                    },
                    'upi_id': {
                        'type': 'string',
                        'description': 'The sender UPI ID'
                    },
                    'recipient_upi': {
                        'type': 'string',
                        'description': 'The recipient UPI ID'
                    }
                },
                'required': ['account_number', 'amount', 'upi_id', 'recipient_upi']
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'UPI transaction created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'},
                    'transaction': {'type': 'object'},
                    'daily_count': {'type': 'integer'}
                }
            }
        }
    }
})
def create_upi_transaction():
    """Create a new UPI transaction and track daily count"""
    data = request.get_json()
    transaction = upi_service.create_upi_transaction(
        data['account_number'], 
        data['amount'], 
        data['upi_id'], 
        data['recipient_upi']
    )
    daily_count = upi_service.get_daily_upi_count(data['account_number'])
    
    return jsonify({
        'message': 'UPI transaction created successfully',
        'transaction': transaction,
        'daily_count': daily_count
    })


@transaction_routes.route('/transactions/upi/<int:transaction_id>', methods=['GET'])
@swag_from({
    'tags': ['UPI Transactions'],
    'description': 'Get a UPI transaction by ID',
    'parameters': [
        {
            'name': 'transaction_id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'The UPI transaction ID'
        }
    ],
    'responses': {
        '200': {'description': 'UPI transaction details'},
        '404': {'description': 'UPI transaction not found'}
    }
})
def get_upi_transaction(transaction_id):
    """Get UPI transaction by ID"""
    transaction = upi_service.get_upi_transaction(transaction_id)
    if transaction:
        return jsonify(transaction)
    return jsonify({'message': 'UPI transaction not found'}), 404


@transaction_routes.route('/transactions/upi', methods=['GET'])
@swag_from({
    'tags': ['UPI Transactions'],
    'description': 'List UPI transactions for an account',
    'parameters': [
        {
            'name': 'account_number',
            'in': 'query',
            'required': True,
            'type': 'string',
            'description': 'The account number'
        }
    ],
    'responses': {
        '200': {'description': 'List of UPI transactions'}
    }
})
def list_upi_transactions():
    """List UPI transactions for an account"""
    account_number = request.args.get('account_number')
    if not account_number:
        return jsonify({'message': 'account_number is required'}), 400
    
    transactions = upi_service.list_upi_transactions(account_number)
    return jsonify(transactions)


@transaction_routes.route('/transactions/upi/count/<account_number>', methods=['GET'])
@swag_from({
    'tags': ['UPI Transactions'],
    'description': 'Get daily UPI transaction count for an account',
    'parameters': [
        {
            'name': 'account_number',
            'in': 'path',
            'required': True,
            'type': 'string',
            'description': 'The account number'
        },
        {
            'name': 'date',
            'in': 'query',
            'required': False,
            'type': 'string',
            'description': 'Date in YYYY-MM-DD format (defaults to today)'
        }
    ],
    'responses': {
        '200': {
            'description': 'UPI transaction count',
            'schema': {
                'type': 'object',
                'properties': {
                    'account_number': {'type': 'string'},
                    'date': {'type': 'string'},
                    'upi_transaction_count': {'type': 'integer'}
                }
            }
        }
    }
})
def get_upi_transaction_count(account_number):
    """Get daily UPI transaction count for an account"""
    date_str = request.args.get('date')
    count = upi_service.get_daily_upi_count(account_number, date_str)
    
    from datetime import date
    target_date = date_str if date_str else date.today().isoformat()
    
    return jsonify({
        'account_number': account_number,
        'date': target_date,
        'upi_transaction_count': count
    })


@transaction_routes.route('/transactions/upi/summary/<account_number>', methods=['GET'])
@swag_from({
    'tags': ['UPI Transactions'],
    'description': 'Get daily UPI transaction summary for an account',
    'parameters': [
        {
            'name': 'account_number',
            'in': 'path',
            'required': True,
            'type': 'string',
            'description': 'The account number'
        },
        {
            'name': 'date',
            'in': 'query',
            'required': False,
            'type': 'string',
            'description': 'Date in YYYY-MM-DD format (defaults to today)'
        }
    ],
    'responses': {
        '200': {
            'description': 'Daily UPI transaction summary',
            'schema': {
                'type': 'object',
                'properties': {
                    'account_number': {'type': 'string'},
                    'date': {'type': 'string'},
                    'transaction_count': {'type': 'integer'},
                    'total_amount': {'type': 'number'},
                    'transactions': {'type': 'array'}
                }
            }
        }
    }
})
def get_upi_daily_summary(account_number):
    """Get daily UPI transaction summary for an account"""
    date_str = request.args.get('date')
    summary = upi_service.get_account_daily_summary(account_number, date_str)
    return jsonify(summary)
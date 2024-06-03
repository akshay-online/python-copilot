from flask import Blueprint, request, jsonify
from models.transaction import Transaction
from services.transaction_service import TransactionService
from models.transaction import Transaction
from flask import Blueprint, request, jsonify
from models.transaction import Transaction
from services.transaction_service import TransactionService
from models.transaction import Transaction
from flasgger import swag_from


transaction_routes = Blueprint('transaction_routes', __name__)
transaction_service = TransactionService()

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
@swag_from({
    'tags': ['Transactions'],
    'description': 'Get mock transactions for testing purposes',
    'responses': {
        '200': {
            'description': 'List of mock transaction details',
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
def get_mock_transactions():
    """
    Get mock transactions for testing purposes.

    Returns:
        A JSON response with a list of mock transaction details.
    """
    return jsonify(mock_transactions)

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
    transaction_service.create_withdrawal(transaction)
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
    transaction_service.create_deposit(transaction)
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
    transaction = transaction_service.get_withdrawal(transaction_id)
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
    transaction = transaction_service.get_deposit(transaction_id)
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
    transactions = transaction_service.list_withdrawals(account_number)
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
    transactions = transaction_service.list_deposits(account_number)
    return jsonify([transaction.__dict__ for transaction in transactions])
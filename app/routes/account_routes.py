from flask import Blueprint, request, jsonify
from models.account import Account
from services.account_service import AccountService
from flasgger import swag_from

account_routes = Blueprint('account_routes', __name__)
account_service = AccountService()


@account_routes.route('/accounts', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'id': 'Account',
                'properties': {
                    'account_number': {
                        'type': 'string',
                        'description': 'Account number for the new account'
                    },
                    'balance': {
                        'type': 'number',
                        'description': 'Initial balance for the new account'
                    }
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Account created successfully',
            'schema': {
                'id': 'Response',
                'properties': {
                    'message': {
                        'type': 'string',
                        'description': 'Success message'
                    }
                }
            }
        },
        '400': {
            'description': 'Invalid request payload'
        }
    }
})
def create_account():
    data = request.get_json()
    account_number = data.get('account_number')
    balance = data.get('balance')
    account = Account(account_number, balance)
    account_service.create_account(account)
    return jsonify({'message': 'Account created successfully'})

@account_routes.route('/accounts/<account_number>', methods=['GET'])

@swag_from({
    'parameters': [
        {
            'name': 'account_number',
            'in': 'path',
            'required': 'true',
            'type': 'string',
            'description': 'Account number'
        }
    ],
    'responses': {
        '200': {
            'description': 'Account details',
            'schema': {
                'id': 'Account',
                'properties': {
                    'account_number': {
                        'type': 'string',
                        'description': 'Account number'
                    },
                    'balance': {
                        'type': 'number',
                        'description': 'Account balance'
                    }
                }
            }
        },
        '404': {
            'description': 'Account not found'
        }
    }
})

def get_account(account_number):
        account = account_service.get_account(account_number)
        if account:
                return jsonify(account.to_dict())
        else:
                return jsonify({'message': 'Account not found'}), 404

@account_routes.route('/accounts/<account_number>', methods=['PUT'])
@swag_from({
    'parameters': [
        {
            'name': 'account_number',
            'in': 'path',
            'required': 'true',
            'type': 'string',
            'description': 'Account number'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'id': 'Account',
                'properties': {
                    'balance': {
                        'type': 'number',
                        'description': 'New balance for the account'
                    }
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Account updated successfully',
            'schema': {
                'id': 'Response',
                'properties': {
                    'message': {
                        'type': 'string',
                        'description': 'Success message'
                    }
                }
            }
        },
        '404': {
            'description': 'Account not found'
        }
    }
})
def update_account(account_number):
        data = request.get_json()
        balance = data.get('balance')
        account = account_service.get_account(account_number)
        if account:
                account.balance = balance
                account_service.update_account(account)
                return jsonify({'message': 'Account updated successfully'})
        else:
                return jsonify({'message': 'Account not found'}), 404

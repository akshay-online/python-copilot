from flask import Blueprint, request, jsonify
from models.account import Account
from services.account_service import AccountService

account_routes = Blueprint('account_routes', __name__)
account_service = AccountService()

@account_routes.route('/accounts', methods=['POST'])
def create_account():
        """
        Create a new account.

        ---
        tags:
            - Accounts
        parameters:
            - name: account_number
                in: body
                type: string
                required: true
                description: The account number.
            - name: balance
                in: body
                type: number
                required: true
                description: The account balance.
        responses:
            200:
                description: Account created successfully.
        """
        data = request.get_json()
        account_number = data.get('account_number')
        balance = data.get('balance')
        account = Account(account_number, balance)
        account_service.create_account(account)
        return jsonify({'message': 'Account created successfully'})

@account_routes.route('/accounts/<account_number>', methods=['GET'])
def get_account(account_number):
        """
        Get account details by account number.

        ---
        tags:
            - Accounts
        parameters:
            - name: account_number
                in: path
                type: string
                required: true
                description: The account number.
        responses:
            200:
                description: Account details retrieved successfully.
            404:
                description: Account not found.
        """
        account = account_service.get_account(account_number)
        if account:
                return jsonify(account.to_dict())
        else:
                return jsonify({'message': 'Account not found'}), 404

@account_routes.route('/accounts/<account_number>', methods=['PUT'])
def update_account(account_number):
        """
        Update account balance by account number.

        ---
        tags:
            - Accounts
        parameters:
            - name: account_number
                in: path
                type: string
                required: true
                description: The account number.
            - name: balance
                in: body
                type: number
                required: true
                description: The new account balance.
        responses:
            200:
                description: Account updated successfully.
            404:
                description: Account not found.
        """
        data = request.get_json()
        balance = data.get('balance')
        account = account_service.get_account(account_number)
        if account:
                account.balance = balance
                account_service.update_account(account)
                return jsonify({'message': 'Account updated successfully'})
        else:
                return jsonify({'message': 'Account not found'}), 404

from flask import Blueprint, Flask, request, jsonify
from services.loans_service import LoanService

loans_routes = Blueprint('loan_routes', __name__)
loan_service = LoanService()

@loans_routes.route('/loans', methods=['POST'])
def create_loan():
    loan_data = request.get_json()
    new_loan = loan_service.create_loan(loan_data)
    return jsonify(new_loan), 201

@loans_routes.route('/loans/<int:loan_id>', methods=['GET'])
def get_loan(loan_id):
    loan = loan_service.get_loan(loan_id)
    if loan:
        return jsonify(loan), 200
    else:
        return jsonify({'message': 'Loan not found'}), 404

@loans_routes.route('/loans/<int:loan_id>', methods=['PUT'])
def update_loan(loan_id):
    loan_data = request.get_json()
    updated_loan = loan_service.update_loan(loan_id, loan_data)
    if updated_loan:
        return jsonify(updated_loan), 200
    else:
        return jsonify({'message': 'Loan not found'}), 404

@loans_routes.route('/loans/<int:loan_id>', methods=['DELETE'])
def delete_loan(loan_id):
    deleted = loan_service.delete_loan(loan_id)
    if deleted:
        return jsonify({'message': 'Loan deleted'}), 200
    else:
        return jsonify({'message': 'Loan not found'}), 404
from flask import Blueprint, Flask, request, jsonify
from services.loans_service import LoanService
from flasgger import swag_from

loans_routes = Blueprint('loan_routes', __name__)
loan_service = LoanService()


@loans_routes.route('/loans', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'id': 'Loan',
                'properties': {
                    'loan_amount': {
                        'type': 'number',
                        'description': 'Loan amount'
                    },
                    'interest_rate': {
                        'type': 'number',
                        'description': 'Interest rate'
                    },
                    'loan_term': {
                        'type': 'integer',
                        'description': 'Loan term in months'
                    },
                    'loan_date': {
                        'type': 'string',
                        'description': 'Loan date'
                    },
                    'loan_type': {
                        'type': 'string',
                        'description': 'Loan type'
                    },
                    'loan_status': {
                        'type': 'string',
                        'description': 'Loan status'
                    },
                    'customer_id': {
                        'type': 'integer',
                        'description': 'Customer ID'
                    }
                }
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Loan created successfully',
            'schema': {
                'id': 'Loan',
                'properties': {
                    'loan_id': {
                        'type': 'integer',
                        'description': 'ID of the loan'
                    },
                    'loan_amount': {
                        'type': 'number',
                        'description': 'Loan amount'
                    },
                    'interest_rate': {
                        'type': 'number',
                        'description': 'Interest rate'
                    },
                    'loan_term': {
                        'type': 'integer',
                        'description': 'Loan term in months'
                    },
                    'loan_date': {
                        'type': 'string',
                        'description': 'Loan date'
                    },
                    'loan_type': {
                        'type': 'string',
                        'description': 'Loan type'
                    },
                    'loan_status': {
                        'type': 'string',
                        'description': 'Loan status'
                    },
                    'customer_id': {
                        'type': 'integer',
                        'description': 'Customer ID'
                    }
                }
            }
        }
    }
})
def create_loan():
    loan_data = request.get_json()
    new_loan = loan_service.create_loan(loan_data)
    return jsonify(new_loan), 201


@loans_routes.route('/loans/<int:loan_id>', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'loan_id',
            'in': 'path',
            'required': 'true',
            'type': 'integer'
        }
    ],
    'responses': {
        '200': {
            'description': 'Loan fetched successfully',
            'schema': {
                'id': 'GetLoan',
                'properties': {
                    'loan_id': {
                        'type': 'integer',
                        'description': 'ID of the loan'
                    },
                    'loan_amount': {
                        'type': 'number',
                        'description': 'Loan amount'
                    },
                    'interest_rate': {
                        'type': 'number',
                        'description': 'Interest rate'
                    },
                    'loan_term': {
                        'type': 'integer',
                        'description': 'Loan term in months'
                    },
                    'loan_date': {
                        'type': 'string',
                        'description': 'Loan date'
                    },
                    'loan_type': {
                        'type': 'string',
                        'description': 'Loan type'
                    },
                    'loan_status': {
                        'type': 'string',
                        'description': 'Loan status'
                    },
                    'customer_id': {
                        'type': 'integer',
                        'description': 'Customer ID'
                    }
                }
            }
        }
    }
})
def get_loan(loan_id):
    loan = loan_service.get_loan(loan_id)
    if loan:
        return jsonify(loan), 200
    else:
        return jsonify({'message': 'Loan not found'}), 404


@loans_routes.route('/loans/<int:loan_id>', methods=['PUT'])
@swag_from({
    'parameters': [
        {
            'name': 'loan_id',
            'in': 'path',
            'required': 'true',
            'type': 'integer'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'id': 'Loan',
                'properties': {
                    'loan_amount': {
                        'type': 'number',
                        'description': 'Loan amount'
                    },
                    'interest_rate': {
                        'type': 'number',
                        'description': 'Interest rate'
                    },
                    'loan_term': {
                        'type': 'integer',
                        'description': 'Loan term in months'
                    },
                    'loan_date': {
                        'type': 'string',
                        'description': 'Loan date'
                    },
                    'loan_type': {
                        'type': 'string',
                        'description': 'Loan type'
                    },
                    'loan_status': {
                        'type': 'string',
                        'description': 'Loan status'
                    },
                    'customer_id': {
                        'type': 'integer',
                        'description': 'Customer ID'
                    }
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Loan updated successfully',
            'schema': {
                'id': 'Loan',
                'properties': {
                    'loan_id': {
                        'type': 'integer',
                        'description': 'ID of the loan'
                    },
                    'loan_amount': {
                        'type': 'number',
                        'description': 'Loan amount'
                    },
                    'interest_rate': {
                        'type': 'number',
                        'description': 'Interest rate'
                    },
                    'loan_term': {
                        'type': 'integer',
                        'description': 'Loan term in months'
                    },
                    'loan_date': {
                        'type': 'string',
                        'description': 'Loan date'
                    },
                    'loan_type': {
                        'type': 'string',
                        'description': 'Loan type'
                    },
                    'loan_status': {
                        'type': 'string',
                        'description': 'Loan status'
                    },
                    'customer_id': {
                        'type': 'integer',
                        'description': 'Customer ID'
                    }
                }
            }
        },
        '404': {
            'description': 'Loan not found'
        }
    }
})
def update_loan(loan_id):
    loan_data = request.get_json()
    updated_loan = loan_service.update_loan(loan_id, loan_data)
    if updated_loan:
        return jsonify(updated_loan), 200
    else:
        return jsonify({'message': 'Loan not found'}), 404

@loans_routes.route('/loans/<int:loan_id>', methods=['DELETE'])

@swag_from({
    'parameters': [
        {
            'name': 'loan_id',
            'in': 'path',
            'required': 'true',
            'type': 'integer'
        }
    ],
    'responses': {
        '200': {
            'description': 'Loan deleted successfully',
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
            'description': 'Loan not found'
        }
    }
})

def delete_loan(loan_id):
    deleted = loan_service.delete_loan(loan_id)
    if deleted:
        return jsonify({'message': 'Loan deleted'}), 200
    else:
        return jsonify({'message': 'Loan not found'}), 404

# loan preclosure api, evaluate the preclosure amount and the final amount to be paid
@loans_routes.route('/loans/<int:loan_id>/preclosure', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'loan_id',
            'in': 'path',
            'required': 'true',
            'type': 'integer'
        }
    ],
    'responses': {
        '200': {
            'description': 'Loan preclosure calculated successfully',
            'schema': {
                'id': 'Preclosure',
                'properties': {
                    'preclosure_amount': {
                        'type': 'number',
                        'description': 'Preclosure amount'
                    }
                }
            }
        },
        '404': {
            'description': 'Loan not found'
        }
    }
})

def preclosure_loan(loan_id):
    loan = loan_service.get_loan(loan_id)
    if loan:
        preclosure_amount = loan_service.preclosure_loan(loan)
        return jsonify(preclosure_amount), 200
    else:
        return jsonify({'message': 'Loan not found'}), 404
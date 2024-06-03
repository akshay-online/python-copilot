# FILE: offer_routes.py

from flask import Flask, jsonify, Blueprint
from services.offer_service import OfferService
from flasgger import swag_from


offer_routes = Blueprint('offer_routes', __name__)
offer_service = OfferService()

@offer_routes.route('/offers', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'The name of the offer'
                    },
                    'price': {
                        'type': 'number',
                        'description': 'The price of the offer'
                    }
                }
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Offer created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {
                        'type': 'integer',
                        'description': 'The ID of the created offer'
                    },
                    'name': {
                        'type': 'string',
                        'description': 'The name of the created offer'
                    },
                    'price': {
                        'type': 'number',
                        'description': 'The price of the created offer'
                    }
                }
            }
        },
        '400': {
            'description': 'Invalid request payload'
        }
    }
})
def create_offer():
    offer = offer_service.create_offer()
    return jsonify(offer), 201


@offer_routes.route('/offers', methods=['GET'])
@swag_from({
    'responses': {
        '200': {
            'description': 'All offers',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {
                            'type': 'integer',
                            'description': 'The ID of the offer'
                        },
                        'name': {
                            'type': 'string',
                            'description': 'The name of the offer'
                        },
                        'price': {
                            'type': 'number',
                            'description': 'The price of the offer'
                        }
                    }
                }
            }
        }
    }
})
def get_all_offers():
    offers = offer_service.get_all_offers()
    return jsonify(offers), 200


@offer_routes.route('/offers/<int:offer_id>', methods=['PUT'])
@swag_from({
    'parameters': [
        {
            'name': 'offer_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'The ID of the offer to update'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'The updated name of the offer'
                    },
                    'price': {
                        'type': 'number',
                        'description': 'The updated price of the offer'
                    }
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Offer updated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {
                        'type': 'integer',
                        'description': 'The ID of the updated offer'
                    },
                    'name': {
                        'type': 'string',
                        'description': 'The updated name of the offer'
                    },
                    'price': {
                        'type': 'number',
                        'description': 'The updated price of the offer'
                    }
                }
            }
        },
        '400': {
            'description': 'Invalid request payload'
        },
        '404': {
            'description': 'Offer not found'
        }
    }
})
def get_offer(offer_id):
    offer = offer_service.get_offer(offer_id)
    if offer:
        return jsonify(offer), 200
    else:
        return jsonify({'message': 'Offer not found'}), 404
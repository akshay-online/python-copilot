# FILE: offer_routes.py

from flask import Flask, jsonify, Blueprint
from services.offer_service import OfferService


offer_routes = Blueprint('offer_routes', __name__)
offer_service = OfferService()

@offer_routes.route('/offers', methods=['GET'])
def get_all_offers():
    offers = offer_service.get_all_offers()
    return jsonify(offers), 200

@offer_routes.route('/offers/<int:offer_id>', methods=['GET'])
def get_offer(offer_id):
    offer = offer_service.get_offer(offer_id)
    if offer:
        return jsonify(offer), 200
    else:
        return jsonify({'message': 'Offer not found'}), 404
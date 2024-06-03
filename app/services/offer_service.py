# FILE: offer_service.py

class OfferService:
    def __init__(self):
        # Mock data
        self.offers = [
            {"id": 1, "name": "Offer 1", "description": "Description for offer 1"},
            {"id": 2, "name": "Offer 2", "description": "Description for offer 2"},
        ]

    def get_all_offers(self):
        return self.offers

    def get_offer(self, offer_id):
        for offer in self.offers:
            if offer["id"] == offer_id:
                return offer
        return None
# FILE: offer_service.py

class OfferService:
    def __init__(self):
        # Mock data
        self.offers = [
            {"id": 1, "name": "Offer 1", "description": "Description for offer 1"},
            {"id": 2, "name": "Offer 2", "description": "Description for offer 2"},
        ]

    def get_all_offers(self):
        try:
            return self.offers
        except Exception as e:
            print(f"Error fetching all offers: {e}")
            return []

    def get_offer(self, offer_id):
        try:
            for offer in self.offers:
                if offer["id"] == offer_id:
                    return offer
            return None
        except Exception as e:
            print(f"Error fetching offer: {e}")
            return None
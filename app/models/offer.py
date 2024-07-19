class offer:
    def __init__(self):
        self.id = 1
        self.name = "Offer 1"
        self.description = "Description for offer 1"
        self.id = 2
        self.name = "Offer 2"
        self.description = "Description for offer 2"
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
import unittest

from app.services.offer_service import OfferService

class TestOfferService(unittest.TestCase):
    def setUp(self):
        self.offer_service = OfferService()

    def test_get_offer(self):
        # Test with valid offer id
        offer_id = 1
        offer = self.offer_service.get_offer(offer_id)
        self.assertEqual(offer, {"id": 1, "name": "Offer 1", "description": "Description for offer 1"})

        # Test with invalid offer id
        offer_id = 999
        offer = self.offer_service.get_offer(offer_id)
        self.assertIsNone(offer)

if __name__ == "__main__":
    unittest.main()
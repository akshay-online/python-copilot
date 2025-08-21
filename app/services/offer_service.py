# FILE: offer_service.py

import pyodbc

class OfferService:
    def __init__(self):
        # SQL Server connection string (update with your actual credentials)
        self.CONNECTION_STRING = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=YOUR_SERVER_NAME;"
            "DATABASE=YOUR_DATABASE_NAME;"
            "UID=YOUR_USERNAME;"
            "PWD=YOUR_PASSWORD"
        )

    def get_all_offers(self):
        """
        Retrieves all offers from the SQL Server database.

        Returns:
            list: A list of dictionaries representing offers.
        """
        try:
            offers = []
            with pyodbc.connect(self.CONNECTION_STRING) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, name, description FROM Offers")
                rows = cursor.fetchall()
                for row in rows:
                    offers.append({
                        "id": row.id,
                        "name": row.name,
                        "description": row.description
                    })
            return offers
        except Exception as e:
            print(f"Error fetching all offers: {e}")
            return []

    def get_offer(self, offer_id):
        """
        Retrieves a specific offer by ID from the SQL Server database.

        Parameters:
            offer_id (int): The ID of the offer to retrieve.

        Returns:
            dict or None: A dictionary representing the offer if found, else None.
        """
        try:
            with pyodbc.connect(self.CONNECTION_STRING) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT id, name, description FROM Offers WHERE id = ?", offer_id
                )
                row = cursor.fetchone()
                if row:
                    return {
                        "id": row.id,
                        "name": row.name,
                        "description": row.description
                    }
                return None
        except Exception as e:
            print(f"Error fetching offer: {e}")
            return None
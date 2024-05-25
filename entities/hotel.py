class Hotel:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def check_availability(self, hotel_id):
        query = "SELECT name, city FROM hotels WHERE id = %s AND available = True"
        cursor = self.db_connection.execute_query(query, (hotel_id,))
        result = cursor.fetchone()
        if result:
            return True, result[0], result[1]  # (available, hotel_name, city)
        else:
            return False, None, None

    def book_hotel(self, hotel_id, user_id):
        try:
            query = "UPDATE hotels SET available = False WHERE id = %s"
            self.db_connection.execute_query(query, (hotel_id,))
            self.db_connection.commit()
            query = "INSERT INTO reservations (hotel_id, user_id) VALUES (%s, %s)"
            self.db_connection.execute_query(query, (hotel_id, user_id))
            self.db_connection.commit()
        except Exception as e:
            self.db_connection.rollback()
            print(f"An error occurred: {e}")

    def show_available_hotels(self):
        query = "SELECT id, name, city, price FROM hotels WHERE available = True"
        cursor = self.db_connection.execute_query(query)
        available_hotels = cursor.fetchall()
        if available_hotels:
            print("Available Hotels:")
            for hotel in available_hotels:
                print(f"ID: {hotel[0]}, Name: {hotel[1]}, City: {hotel[2]}, Price: {hotel[3]}")
        else:
            print("No available hotels.")

    def filter_hotels(self, filters):
        query = "SELECT id, name, city, price FROM hotels WHERE available = True"
        params = []

        if filters["city"]:
            query += " AND city = %s"
            params.append(filters["city"])
        if filters["name"]:
            query += " AND name LIKE %s"
            params.append(f"%{filters['name']}%")
        if filters["min_price"]:
            query += " AND price >= %s"
            params.append(filters["min_price"])
        if filters["max_price"]:
            query += " AND price <= %s"
            params.append(filters["max_price"])

        cursor = self.db_connection.execute_query(query, params)
        filtered_hotels = cursor.fetchall()
        if filtered_hotels:
            print("Filtered Hotels:")
            for hotel in filtered_hotels:
                print(f"ID: {hotel[0]}, Name: {hotel[1]}, City: {hotel[2]}, Price: {hotel[3]}")
        else:
            print("No hotels match your filters.")

from entities.user import User
from helpers.database import DatabaseConnection

class Admin(User):
    def __init__(self, db_connection):
        super().__init__(db_connection)

    def add_hotel(self, name, city, price):
        query = "INSERT INTO hotels (name, city, price, available) VALUES (%s, %s, %s, %s)"
        self.db_connection.execute_query(query, (name, city, price, True))
        self.db_connection.commit()
   

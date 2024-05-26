import mysql.connector
from datetime import datetime
from entities.hotel import Hotel
from entities.creditcard import CreditCard
from entities.user import User
from helpers.database import DatabaseConnection
from entities.admin import Admin
from helpers.filters import filter_hotels
from helpers.login import login
from helpers.create_acount import create_account


class HotelBookingSystem:
    def __init__(self):
        self.db_connection = DatabaseConnection()
        self.user = User(self.db_connection)
        self.admin = Admin(self.db_connection)
        self.credit_card = CreditCard(self.db_connection)
        self.hotel = Hotel(self.db_connection)
        self.current_user_id = None

    def run(self):
        while True:
            print("1. Show available hotels")
            print("2. Filter hotels")
            print("3. Book a hotel")
            print("4. Create a new account")
            print("5. Login")
            print("6. Exit")
            print("7. Add new hotel (Admin)")
            choice = input("Choose an option: ")
            if choice == '1':
                self.hotel.show_available_hotels()
            elif choice == '2':
                self.filter_hotels()
            elif choice == '3':
                self.book_hotel()
            elif choice == '4':
                create_account(self.user)  
            elif choice == '5':
                self.current_user_id = self.login()
            elif choice == '6':
                break
            elif choice == '7':
                admin_password = input('Enter admin password: ')
                if admin_password == 'adminedhem':
                    name = input("Enter the name of the hotel: ")
                    city = input("Enter the city of the hotel: ")
                    price = float(input("Enter the price per night: "))
                    self.admin.add_hotel(name, city, price)
                else:
                    print("Only admin can perform this action.")
            else:
                print("Invalid choice, please try again.")

    def filter_hotels(self):
        filter_hotels(self.hotel)

    def add_hotel(self):
        name = input("Enter the name of the hotel: ")
        city = input("Enter the city of the hotel: ")
        price = float(input("Enter the price per night: "))
        self.admin.add_hotel(name, city, price)

    def book_hotel(self):
        if self.current_user_id is None:
            print("Please login first.")
            return

        hotel_id = input("Enter the ID of the hotel you want to book: ")

        available, hotel_name, city = self.hotel.check_availability(hotel_id)
        if available:
            print(f"Hotel '{hotel_name}' in {city} is available for booking.")
            card_number = input("Enter your credit card number: ")
            expiration = input("Enter the expiration date (MM/YY): ")
            cvc = input("Enter the CVV/CVC: ")
            holder = input("Enter the card holder's name: ")
            valid, card_holder = self.credit_card.validate_credit_card(card_number, expiration, cvc, holder)
            if valid:
                print(f"Credit card validation successful for card holder '{card_holder}'. Booking hotel '{hotel_name}'...")
                self.hotel.book_hotel(hotel_id, self.current_user_id)
                print("Booking successful! Enjoy your stay.")
            else:
                print("Invalid credit card details.")
        else:
            print("Hotel is not available for booking.")

    def login(self):
        return login(self.user)

def main():
    booking_system = HotelBookingSystem()
    booking_system.run()

if __name__ == "__main__":
    main()
# Hotel Booking System

Introduction

Welcome to the Hotel Booking System! This is a command-line based application that allows users to browse, filter, and book hotels. Additionally, admins have the ability to add new hotels to the system. The system ensures secure booking by validating credit card details.

## Features

1. Show Available Hotels: View a list of all available hotels.
2. Filter Hotels: Apply various filters to find hotels that meet specific criteria.
3. Book a Hotel: Securely book a hotel by providing valid credit card details.
4. Create a New Account: Create a user account to enable booking.
5. Login: Login to the system to access booking functionalities.
6. Exit: Exit the application.
7. Add New Hotel (Admin): Admins can add new hotels to the system by providing hotel details and a password.

## How to Run the Application

Ensure you have Python installed on your machine.
Install MySQL and create a database for the hotel booking system.
Set up the database schema and tables as per the requirements.
Configure the DatabaseConnection class in helpers/database.py to connect to your MySQL database.
Clone the repository and navigate to the project directory.
Run the application using the command:
bash
Copy code
python main.py

## Code Structure

main.py: The entry point of the application. It initializes the HotelBookingSystem class and runs the main loop.
entities: Contains the entity classes Hotel, CreditCard, User, and Admin.
helpers: Contains helper functions and classes such as DatabaseConnection, filter_hotels, login, and create_account.
Class Descriptions
HotelBookingSystem
This is the main class that orchestrates the application's functionality.

## Methods:
__init__(): Initializes the database connection and entity instances.
run(): Runs the main loop of the application, displaying options and executing user choices.
filter_hotels(): Allows users to apply filters to the list of hotels.
add_hotel(): Admin function to add a new hotel.
book_hotel(): Allows users to book a hotel after validating credit card details.
login(): Handles user login.

## Hotel
Handles hotel-related operations such as displaying available hotels and checking availability.

## CreditCard
Handles credit card validation.

## User
Manages user-related operations including account creation and authentication.

## Admin
Handles admin-specific operations such as adding new hotels.

## Usage
Show Available Hotels
Select option 1 from the main menu to view all available hotels.
Filter Hotels
Select option 2 from the main menu to apply filters.
Book a Hotel
Select option 3 from the main menu.
If not logged in, the system will prompt you to log in first.
Enter the ID of the hotel you want to book.
Provide valid credit card details to complete the booking.
Create a New Account
Select option 4 from the main menu.
Follow the prompts to create a new user account.
Login
Select option 5 from the main menu.
Provide your username and password to log in.
Add New Hotel (Admin)
Select option 7 from the main menu.
Enter the admin password to gain access.
Provide the hotel details to add a new hotel to the system.
Admin Password
The default admin password is adminedhem. Ensure to change this in the production environment for better security.

## Conclusion
The Hotel Booking System is a simple yet powerful tool for managing hotel bookings. By following the instructions provided, users can easily navigate through the system and perform various operations. For any further assistance or contribution, please refer to the project's repository.
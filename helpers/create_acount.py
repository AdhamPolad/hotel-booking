def create_account(user):
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    email = input("Enter your email: ")
    user.create_account(username, password, email)
    print("Account created successfully.")
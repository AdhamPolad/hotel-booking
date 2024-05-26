def create_account(user):
    while True:
        username = input("Enter a username: ")
        if ' ' in username or '@' not in username:
            print("Invalid username. Make sure there are no spaces and the email contains '@'.")
            continue

        password = input("Enter a password: ")
        if ' ' in password:
            print("Password should not contain spaces. Please try again.")
            continue

        email = input("Enter your email: ")
        if ' ' in email or '@' not in email:
            print("Invalid email. Make sure there are no spaces and the email contains '@'.")
            continue
        
        break

    user.create_account(username, password, email)
    print("Account created successfully.")

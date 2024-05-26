def login(user):
    while True:
        username = input("Enter your username (email): ")
        if ' ' in username or '@' not in username:
            print("Invalid username. Make sure there are no spaces and the email contains '@'.")
            continue
        
        password = input("Enter your password: ")
        if ' ' in password:
            print("Password should not contain spaces. Please try again.")
            continue
        
        authenticated, user_id = user.authenticate(username, password)
        if authenticated:
            print("Login successful.")
            return user_id
        else:
            print("Invalid username or password.")
            return None
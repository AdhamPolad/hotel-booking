def login(user):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    authenticated, user_id = user.authenticate(username, password)
    if authenticated:
        print("Login successful.")
        return user_id
    else:
        print("Invalid username or password.")
        return None
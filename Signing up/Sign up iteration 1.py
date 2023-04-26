username_list = []
password_list = []

# Add a test user
username_list.append("testuser")
password_list.append("Testing123")

# login and signup options
while True:
    option = input("Enter '1' to log in, '2' to sign up: ")
    if option == '1':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in username_list and password == password_list[username_list.index(username)]:
            print(f"Welcome back {username}! What would you like to order?")
            break  # if user logs in successfully, exit the loop
        else:
            print("Incorrect username or password. Please try again.")
    elif option == '2':
        new_username = input("Enter your desired username: ")
        new_password = input("Enter your desired password: ")
        # TODO: Add age verification for new users
        username_list.append(new_username)
        password_list.append(new_password)
        print("Sign up successful! Please log in with your new credentials.")
    else:
        print("Invalid input. Please enter either '1' or '2'.")
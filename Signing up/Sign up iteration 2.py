import os

# create user_details.txt if it doesn't exist
if not os.path.exists("user_details.txt"):
    with open("user_details.txt", "w") as f:
        pass

# login and signup options
while True:
    option = input("Enter '1' to log in, '2' to sign up: ")
    if option == '1':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        with open("user_details.txt", "r") as f:
            for line in f:
                line = line.strip().split(",")
                if line[0] == username and line[1] == password:
                    print(f"Welcome back {username}! What would you like to order?")
                    break  # if user logs in successfully, exit the loop
            else:
                print("Incorrect username or password. Please try again.")
    elif option == '2':
        new_username = input("Enter your desired username: ")
        new_password = input("Enter your desired password: ")
        # TODO: Add age verification for new users
        with open("user_details.txt", "a") as f:
            f.write(f"{new_username},{new_password}\n")
        print("Sign up successful! Please log in with your new credentials.")
    else:
        print("Invalid input. Please enter either '1' or '2'.")
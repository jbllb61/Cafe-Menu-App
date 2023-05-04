import os

# create user_details.txt if it doesn't exist
if not os.path.exists("user_details.txt"):
    with open("user_details.txt", "w") as user_file:
        pass

# login and signup options
while True:
    option = input("Enter '1' to log in, '2' to sign up: ")
    if option == '1':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        with open("user_details.txt", "r") as user_file:
            for line in user_file:
                line = line.strip().split(",")
                if line[0] == username and line[1] == password:
                    print(f"Welcome back {username}! What would you like to order?")
                    break  # end the loop after logging in successfully
            else:
                print("Incorrect username or password. Please try again.")
        if line[0] == username and line[1] == password:
            break  # end the loop after logging in successfully
    elif option == '2':
        while True:
            new_username = input("Enter your desired username: ")
            new_password = input("Enter your desired password: ")
            # check if username already exists
            with open("user_details.txt", "r") as user_file:
                for line in user_file:
                    line = line.strip().split(",")
                    if line[0] == new_username:
                        print("This username already exists. Please choose a different username.")
                        break
                else:
                    # password requirements
                    if len(new_password) < 8:
                        print("Password must be at least 8 characters long.")
                    elif not any(char.isupper() for char in new_password):
                        print("Password must contain at least one uppercase letter.")
                    elif not any(char.islower() for char in new_password):
                        print("Password must contain at least one lowercase letter.")
                    elif not any(char.isdigit() for char in new_password):
                        print("Password must contain at least one digit.")
                    else:
                        # add new user to file if username is unique and password is valid
                        with open("user_details.txt", "a") as user_file:
                            user_file.write(f"{new_username},{new_password}\n")
                        print("Sign up successful! Please log in with your new credentials.")
                        break  # end the loop after successful registration
    else:
        print("Invalid input. Please enter either '1' or '2'.")
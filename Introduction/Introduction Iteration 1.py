print("Welcome to the school cafe app!")
name = input("Please enter your name: ")

while True:
    try:
        age = int(input("Please enter your age: "))
        if age < 13 or age > 18:
            print("Sorry, this app is only available for students aged 13-18.")
            print("Farewell! Please come back when you are within the age range.")
            exit()
        break  # if age is valid, exit the loop
    except ValueError:
        print("Invalid input. Please enter a valid age.")

print(f"Hello, {name}! Please log in or create an account to use the app.")

# TODO: Implement login and account creation functionality
# TODO: Implement index data list for username and password verification
# TODO: Add age verification for new users 
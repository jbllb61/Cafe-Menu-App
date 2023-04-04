print("Welcome to the school cafe app!")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if age < 13 or age > 18:
    print("Sorry, this app is only available for students aged 13-18.")
    print("Please come back when you are within the age range.")
    exit()

print(f"Hello, {name}! Please log in or create an account to use the app.")

# TODO: Implement login and account creation functionality
# TODO: Implement index data list for username and password verification
# TODO: Add age verification for new users 
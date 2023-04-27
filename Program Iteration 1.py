ITEMS = {'sandwich': 2.50, 'pizza': 3.00, 'salad': 2.00, 'fruit cup': 1.50}
username_list = []
password_list = []

# Add a test user
username_list.append("testuser")
password_list.append("Testing123")

# Intro
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
        print("Invalid input. Please enter a valid number. eg 15")

print(f"Hello, {name}! Please log in or create an account to use the app.")

#login and signup options
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


# Display the menu
print('MENU')
for item, price in ITEMS.items():
    print(f'{item.title()} - ${price:.2f}')

# Take the order
print('\nPLACE AN ORDER')
order = {}
while True:
    choice = input('Enter an item to order (or "done" to finish): ').lower()
    if choice == 'done':
        break
    if choice not in ITEMS:
        print('Sorry, that item is not available.')
        continue
    quantity_str = input('Enter the quantity you want to order: ')
    if not quantity_str.isdigit():
        print('Sorry, the quantity should be a valid number. Please try again.')
        continue
    quantity = int(quantity_str)
    if quantity <= 0:
        print('Sorry, the quantity must be above 0. Please try again.')
        continue
    order[choice] = quantity

# Display the order summary
print('\nORDER SUMMARY')
total = 0
for item, quantity in order.items():
    price = ITEMS[item]
    subtotal = price * quantity
    print(f'{item.title()} x{quantity} - ${subtotal:.2f}')
    total += subtotal
print(f'TOTAL: ${total:.2f}')
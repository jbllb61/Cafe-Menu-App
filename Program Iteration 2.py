import os

ITEMS = {'sandwich': 2.50, 'pizza': 3.00, 'salad': 2.00, 'fruit cup': 1.50, 'chips': 1.00, 'soda': 1.50}


def intro():
    print("Welcome to the school cafe app!")
    while True:
        try:
            age = int(input("Please enter your age (This programme is for students aged 13-18): "))
            if age < 13 or age > 18:
                print("Sorry, this app is only available for students aged 13-18.")
                exit()
            break  # if age is valid, exit the loop
        except ValueError:
            print("Invalid input. Please enter a valid number. eg 13 or 15")
    print("Please log in or create an account to use the app.")

intro()

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
            # check if username already exists
            with open("user_details.txt", "r") as user_file:
                for line in user_file:
                    line = line.strip().split(",")
                    if line[0] == new_username:
                        print("This username already exists. Please choose a different username.")
                        break
                else:
                    # password requirements
                    while True:
                        new_password = input("Enter your desired password: ")
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
                    break # end the loop after validating password and adding new user to file
    else:
        print("Invalid input. Please enter either '1' or '2'.")

# Display the menu
print('MENU')
for i, (item, price) in enumerate(ITEMS.items(), start=1):
    print(f'{i}. {item.title()} - ${price:.2f}')

# Take the order
print('\nPLACE AN ORDER')
order = {}
while True:
    choice = input('Enter an item number to order (or "done" to finish): ')
    if choice == 'done':
        break
    try:
        choice = int(choice)
    except ValueError:
        print('Sorry, that is not a valid item number. Please try again.')
        continue
    if choice not in range(1, len(ITEMS) + 1):
        print('Sorry, that item number is not available.')
        continue
    quantity_str = input('Enter the quantity you want to order: ')
    if not quantity_str.isdigit():
        print('Sorry, the quantity should be a valid number. Please try again.')
        continue
    quantity = int(quantity_str)
    if quantity <= 0:
        print('Sorry, the quantity must be above 0. Please try again.')
        continue
    item_name = list(ITEMS.keys())[choice - 1]
    if item_name in order:
        order[item_name] += quantity  # Update the quantity if the item is already in the order
    else:
        order[item_name] = quantity  # Add the item and its quantity to the order

# Display the order summary as a receipt
print('\n' + '-'*30)
print('{:^30}'.format('ORDER SUMMARY'))
print('-'*30)
for item, quantity in order.items():
    if item not in ITEMS:
        continue
    price = ITEMS[item]
    subtotal = price * quantity
    print('{:<20} x{:>2}  ${:>6.2f}'.format(item.title(), quantity, subtotal))
print('-'*30)
total = sum(ITEMS[item] * order[item] for item in order)
print('{:<20}  ${:>6.2f}'.format('TOTAL', total))
print('-'*30)

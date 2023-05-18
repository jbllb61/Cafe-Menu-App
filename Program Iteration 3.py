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

def login():
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

def display_menu():
    # Display the menu
    print('MENU')
    for i, (item, price) in enumerate(ITEMS.items(), start=1):
        print(f'{i}. {item.title()} - ${price:.2f}')

def place_order():
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
            
        # Check if the quantity of the item exceeds 10, and if so, set the quantity to 10
        if quantity > 10:
            quantity = 10
            print('Warning: you cannot order more than 10 of the same item. The quantity has been changed to 10.')
        
        item_name = list(ITEMS.keys())[choice - 1]
        if item_name in order:
            order[item_name]['quantity'] += quantity  # Update the quantity if the item is already in the order
        else:
            order[item_name] = {'quantity': quantity, 'gluten-free': False, 'dairy-free': False}  # Add the item and its quantity to the order

        gluten_free = input(f'Is {item_name.title()} gluten-free? (y/n): ')
        if gluten_free.lower().strip() == 'y' or gluten_free.lower().strip() == 'yes':
            order[item_name]['gluten-free'] = True
        
        dairy_free = input(f'Is {item_name.title()} dairy-free? (y/n): ')
        if dairy_free.lower().strip() == 'y' or dairy_free.lower().strip() == 'yes':
            order[item_name]['dairy-free'] = True

    # Display the order summary as a receipt
    print("NOTE: ITEM LIMIT OF 10")
    print('\n' + '-'*57)
    print('{:^57}'.format('ORDER SUMMARY'))
    print('-'*57)
    item_num = 1
    total = 0
    for item, details in order.items():
        if item not in ITEMS:
            continue
        price = ITEMS[item]
        quantity = details['quantity']
        gluten_free = details['gluten-free']
        dairy_free = details['dairy-free']
        
        # Check if the quantity of the item exceeds 10, and if so, set the quantity to 10
        if quantity > 10:
            quantity = 10
        
        item_name = item.title()
        if gluten_free:
            item_name += ' (gluten-free)'
        if dairy_free:
            item_name += ' (dairy-free)'
        subtotal = price * quantity
        total += subtotal
        print('{:<5}{:<30} x {:>2}  ${:>6.2f}'.format(item_num, item_name, quantity, subtotal))
        item_num += 1
    print('-'*57)
    print('{:<5}{:<30}      ${:>6.2f}'.format('', 'TOTAL', total))
    print('-'*57)

    # Remove items from the order
    while True:
        choice_remove = input('Enter an item number to remove (or "done" to continue): ')
        if choice_remove == 'done':
            break
        try:
            choice_remove = int(choice_remove)
        except ValueError:
            print('Sorry, that is not a valid item number. Please try again.')
            continue
        if choice_remove not in range(1, len(order) + 1):
            print('Sorry, that item number is not available.')
            continue
        item_name_remove = list(order.keys())[choice_remove - 1]
        del order[item_name_remove]
        # Display the updated order summary
        print('\n' + '-'*57)
        print('{:^57}'.format('UPDATED ORDER SUMMARY'))
        print('-'*57)
        item_num = 1
        total = 0
        for item, details in order.items():
            if item not in ITEMS:
                continue
            price = ITEMS[item]
            quantity = details['quantity']
            gluten_free = details['gluten-free']
            dairy_free = details['dairy-free']
            item_name = item.title()
            if gluten_free:
                item_name += ' (gluten-free)'
            if dairy_free:
                item_name += ' (dairy-free)'
            subtotal = price * quantity
            total += subtotal
            print('{:<5}{:<30} x {:>2}  ${:>6.2f}'.format(item_num, item_name, quantity, subtotal))
            item_num += 1
        print('-'*57)
        print('{:<30}  ${:>6.2f}'.format('TOTAL', total))
        print('-'*57)

def collect_feedback():
    feedback_text = input("Please provide your feedback (Optional): ")
    # Check if feedback is not empty and has length greater than 5
    if feedback_text.strip() != "" and len(feedback_text) > 5:
        print("Thank you for your feedback!")
        

# create user_details.txt if it doesn't exist
if not os.path.exists("user_details.txt"):
    with open("user_details.txt", "w") as user_file:
        pass


# main routine
intro()
login()
display_menu()
place_order()
collect_feedback()

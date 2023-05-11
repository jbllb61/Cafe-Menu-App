ITEMS = {'sandwich': 2.50, 'pizza': 3.00, 'salad': 2.00, 'fruit cup': 1.50, 'chips': 1.00, 'soda': 1.50}

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
        order[item_name]['quantity'] += quantity  # Update the quantity if the item is already in the order
    else:
        order[item_name] = {'quantity': quantity, 'gluten-free': False, 'dairy-free': False}  # Add the item and its quantity to the order

    gluten_free = input('Is this item gluten-free? (y/n): ')
    if gluten_free.lower().strip() == 'y' or gluten_free.lower().strip() == 'yes':
        order[item_name]['gluten-free'] = True
    
    dairy_free = input('Is this item dairy-free? (y/n): ')
    if dairy_free.lower().strip() == 'y' or dairy_free.lower().strip() == 'yes':
        order[item_name]['dairy-free'] = True

# Display the order summary as a receipt
print('\n' + '-'*45)
print('{:^45}'.format('ORDER SUMMARY'))
print('-'*45)
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
    print('{:<30} x{:>2}  ${:>6.2f}'.format(item_name, quantity, subtotal))
print('-'*45)
total = sum(ITEMS[item] * order[item]['quantity'] for item in order)
print('{:<30}  ${:>6.2f}'.format('TOTAL', total))
print('-'*45)

feedback_text = input("Please provide your feedback: ")

# Check if feedback is not empty and has length greater than 5
if feedback_text.strip() != "" and len(feedback_text) > 5:
    print("Thank you for your feedback!")
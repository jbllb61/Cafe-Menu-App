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
    order[item_name] = quantity

# Display the order summary
print('\nORDER SUMMARY')
total = 0
for item, quantity in order.items():
    if item not in ITEMS:
        continue
    price = ITEMS[item]
    subtotal = price * quantity
    print(f'{item.title()} x{quantity} - ${subtotal:.2f}')
    total += subtotal
print(f'TOTAL: ${total:.2f}')

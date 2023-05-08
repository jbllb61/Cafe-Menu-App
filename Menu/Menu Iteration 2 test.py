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

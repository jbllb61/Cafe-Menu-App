ITEMS = {'sandwich': 2.50, 'pizza': 3.00, 'salad': 2.00, 'fruit cup': 1.50}

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

groceries = ['apple', 'banana', 'cherry', 'orange']

item = 'dates'
if item in groceries:
    groceries.remove(item)
    print(f'{item} removed from the list')
    print('Updated list:',groceries)
elif:
    print(f'{item} not found. Appending to the list')
    groceries.append(item)
    print('Updated list:',groceries)
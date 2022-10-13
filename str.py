#Handling strings

letter = 'D'
name = "John"
multiples = ''' This can go on and on and on ....  '''

print(len(multiples))

print('can' in multiples)

#slicing
print(multiples[0:5])

# print(dir(multiples))
print(multiples)
multi_array = multiples.strip()
multi_array = multi_array.split(" ")
print(multi_array)

# format method for concatenation

quantity = 35
itemno = 567
price = 46.67

print(f'I want to pay ${price} for {itemno} pieces of {quantity} mangos ')

# use / to escape illegal characters
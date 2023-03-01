#!/usr/bin/python

# 2c - Modify your program to generate a tuple of random numbers of a random length
# Still show what the difference and product is

from random import randint, randrange

MAX_LENGTH = 100  # Constant that is the maximum length of the tuple
MAX_NUMBER = 500  # Constant that is the highest value the tuple can hold

# randrange is exclusive of the stop parameter
number_of_items = randrange(2, MAX_LENGTH + 1)

# Create a list so we can append rather than generating lots of tuples
list_items = []

# Add items to our list
for i in range(number_of_items):
    list_items.append(randint(1, MAX_NUMBER))

# Convert to a tuple
tuple_items = tuple(list_items)
print(f'Our tuple is: {tuple_items}')

# Use same methods as in 2a and 2b
print(f'Difference between max and min is {max(tuple_items) - min(tuple_items)}')

result = 1
for number in tuple_items:
    result *= number

# This might be very, very big
print(f'Product is {result}')

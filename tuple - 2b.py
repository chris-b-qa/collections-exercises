#!/usr/bin/python

# 2b - Find the product of the elements of the tuple (product is each item multiplied together)

# Remember that the brackets are optional on a tuple
my_tuple = 2, 5, 12, 7, 9

# This must be 1 rather than 0 because otherwise anything multiplied by 0 is always 0
# For an empty tuple we should probably throw an exception before trying to calculate the product
result = 1

# Iterate through the items in my_tuple and multiply the result by that value
for number in my_tuple:
    result *= number

print(result)

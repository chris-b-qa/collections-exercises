#!/usr/bin/python

# 1b - Modify your program to remove a random number

from random import randint

# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Choose the index of a number to remove at random
# The 2nd parameter for randint is inclusive (unusual for Python) so subtract 1 from the length
index_to_remove = randint(0, len(numbers) - 1)
removed_number = numbers.pop(index_to_remove)

all_numbers = set(range(1, 11))

diff = all_numbers.difference(set(numbers))
print(f'We removed {diff.pop()}')

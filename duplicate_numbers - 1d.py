#!/usr/bin/python

from random import randint

# Make a nice long list
LIST_LENGTH = 1000

numbers = list(range(1, LIST_LENGTH + 1))

number_to_duplicate = randint(1, LIST_LENGTH)

# Our number has the same index as the value, this inserts it after the existing version of that number
numbers.insert(number_to_duplicate, number_to_duplicate)

# Use a list comprehension to loop through our numbers and check whether the index + 1 doesn't equal the number
# This will return a list which begins with the duplicated number followed by all the remaining numbers
diff = [number for i, number in enumerate(numbers) if i + 1 != number]

# Only print out the 1st element in the list to get the duplicated number
print(f'The duplicate number was {diff[0]}')

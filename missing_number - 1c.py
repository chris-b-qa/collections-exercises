#!/usr/bin/python

# 1c - Update the program to have all numbers from 1 to 100 and remove a random number of elements.
# Find how many numbers were removed and what they were

from random import randrange

# Set a constant for the length of the list
LIST_LENGTH = 100

numbers = list(range(1, LIST_LENGTH + 1))

# Use randrange to choose how many numbers to remove
# The 2nd parameter to randrange is the end of the range + 1
amount_of_numbers_to_remove = randrange(1, len(numbers) + 1)

# Remember range is also end of the range + 1
for i in range(1, amount_of_numbers_to_remove + 1):
    # Indexes count from 0 rather than 1
    index_to_remove = randrange(0, len(numbers))
    # Use the del statement rather than pop-ing the value
    del numbers[index_to_remove]

all_numbers = set(range(1, LIST_LENGTH + 1))
diff = list(all_numbers.difference(set(numbers)))

# Sort the list before printing as we have lost our order due to using sets to calculate the difference
diff.sort()
print(f'We removed {len(diff)} numbers\n', diff)

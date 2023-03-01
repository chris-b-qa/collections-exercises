#!/usr/bin/python

# 1a - Given a list of the numbers between 1 and 10 (but excluding one number) find the missing number

# Our list of numbers excluding the number 6
numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10]

# Go from 1 to 11 as range's 2nd value is exclusive (end + 1)
all_numbers = set(range(1, 11))

# Use a set difference to find what isn't in the 2nd set
diff = all_numbers.difference(set(numbers))

# diff is currently a set with 1 element so print out the element that we've pop-ed from it
# NB if the lists were identical this would throw an exception!
print(f'We removed {diff.pop()}')

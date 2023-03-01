#!/usr/bin/python
# 2a - Given the following tuple of numbers, what is the difference between the biggest and smallest number?
# 2, 5, 12, 7, 9

my_tuple = (2, 5, 12, 7, 9)

# Use the max and min functions to find the highest and lowest values in our tuple
diff = max(my_tuple) - min(my_tuple)
print(diff)

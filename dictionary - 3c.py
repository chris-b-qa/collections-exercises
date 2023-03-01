#!/usr/bin/python

# 3c - Write code to create a new dictionary that has the key as each colour’s name and
# the value being how many people have that colour as their favourite

# Create a dictionary storing our people as the keys and the colours as the values (with updates in place)
colour_preferences = {'Becci': 'green', 'Steve': 'orange', 'Melinda': 'green', 'Ryan': 'orange', 'Nate': 'green',
                      'Anna': 'green', 'Chris': 'blue'}

# Create a new empty dictionary
colour_counts = {}

# Iterate through the keys as a list of tuples
for name, colour in colour_preferences.items():
    # If we have that colour already increment it
    if colour in colour_counts.keys():
        colour_counts[colour] += 1
    # Otherwise set it to 1
    else:
        colour_counts[colour] = 1

print(colour_counts)

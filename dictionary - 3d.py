#!/usr/bin/python

# 3d - Write code to create another dictionary that has the colour name as the key and
# a list of all the people that don’t have that colour as their favourite as the value

# Create a dictionary storing our people as the keys and the colours as the values (with updates in place)
colour_preferences = {'Becci': 'green', 'Steve': 'orange', 'Melinda': 'green', 'Ryan': 'orange', 'Nate': 'green',
                      'Anna': 'green', 'Chris': 'blue'}

# Use a set to get unique colour preferences from the values view object
unique_colours = set(colour_preferences.values())

# Initialise a dictionary using a comprehension with an empty list as the value for each unique colour
disliked_colours = {unique_colour: [] for unique_colour in unique_colours}

# Iterate through each of the names and preferred colours in our initial dictionary
for name, preferred_colour in colour_preferences.items():
    # Use a set difference to iterate only the non-favourite colours
    for colour in unique_colours - {preferred_colour}:
        # Add the person to the list for each non-favourite colour
        disliked_colours[colour].append(name)

# Use a generator to iterate over the items and insert them into an f string for each element
# We use the join to display the people as a string without the enclosing brackets when printing a list
# We then unpack them as separate parameters to the print function using the unpacking operator *
# This means that we have to set a separator of a line break in order to print one item per line
print(*(f'The people who disliked {colour} were {", ".join(people)}'
        for colour, people in disliked_colours.items()), sep='\n')

#!/usr/bin/python

# 3b - Add your own favourite colours.
# Update Melinda’s preference to green and remove Sandy’s preference from the dictionary

# Create a dictionary storing our people as the keys and the colours as the values
colour_preferences = {
    'Becci': 'green',
    'Steve': 'orange',
    'Melinda': 'purple',
    'Ryan': 'orange',
    'Nate': 'green',
    'Anna': 'green',
}

# Add and update our preferences
colour_preferences['Chris'] = 'blue'
colour_preferences['Melinda'] = 'green'

# Typo in question but can use pop with a default parameter to allow us to not throw an exception
# when trying to remove a key that doesn't exist in the dictionary
colour_preferences.pop('Sandy', False)

print(colour_preferences)

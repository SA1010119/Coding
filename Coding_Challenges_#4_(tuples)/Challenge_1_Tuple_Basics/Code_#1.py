# Name: Tuple Basics
# Purpose: To learn how to create a tuple with five different elements, including an integer, a float, a string, a boolean, and another tuple.


#            Work on Python
#
# Author:      Soltan
# Created:     27-March-2025
# Updated:     27-March-2025
#----------------------------------------------------------------------------

# Creating a tuple with mixed data types
my_tuple = (42, 3.14, 'Python', True, (1, 2, 3))

# Printing the entire tuple
print("Full tuple:", my_tuple)

# Accessing and printing the third element
print("Third element:", my_tuple[2])

# Extracting and printing the first element of the nested tuple
nested_tuple = my_tuple[4]
print("First element of nested tuple:", nested_tuple[0])

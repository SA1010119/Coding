#-----------------------------------------------------------------------------
# Name: Tuple Operations & Count
# Purpose: To learn how to create a tuple with repeated values, such as `("apple", "banana", "apple", "cherry", "banana", "apple")`.


#            Work on Python
#
# Author:      Soltan
# Created:     28-March-2025
# Updated:     28-March-2025
#----------------------------------------------------------------------------

# Creating a tuple with repeated fruit names
fruits = ("apple", "banana", "apple", "cherry", "banana", "apple")

# Asking the user to enter a fruit name
fruit_name = input("Enter a fruit name: ")

# Counting the occurrences of the fruit
count = fruits.count(fruit_name)

# Displaying the result
print(f"'{fruit_name}' appears {count} times in the tuple.")

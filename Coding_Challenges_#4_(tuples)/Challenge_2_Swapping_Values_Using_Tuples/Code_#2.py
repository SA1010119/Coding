#-----------------------------------------------------------------------------
# Name: Swapping Values Using Tuples
# Purpose: Swapping values easily using tuples


#            Work on Python
#
# Author:      Soltan
# Created:     27-March-2025
# Updated:     28-March-2025
#----------------------------------------------------------------------------

# Getting two numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Storing the numbers in a tuple
numbers = (num1, num2)

# Swapping the values using tuple unpacking
num1, num2 = numbers[1], numbers[0]

# Displaying the swapped values
print("Swapped values:", (num1, num2))

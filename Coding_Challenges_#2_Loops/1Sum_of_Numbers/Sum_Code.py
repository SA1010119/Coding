#-----------------------------------------------------------------------------
# Name:  Sum of Number
# Purpose:calculates the sum of all numbers from `1` to `n` using a `for` loop.


#            Work on Python
#
# Author:      Soltan
# Created:     9-March-2025
# Updated:     9-March-2025
#-----------------------------------------------------------------------------

# Ask the user to enter a number
n = int(input("Enter a number: "))

# Initialize sum variable
total = 0

# Loop from 1 to n and add each number to total
for num in range(1, n + 1):
    total += num  # Add the number to the sum

# Print the final sum
print("Sum =", total)
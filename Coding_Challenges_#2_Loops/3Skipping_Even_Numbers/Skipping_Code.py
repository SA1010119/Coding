#-----------------------------------------------------------------------------
# Name: Skipping Even Number
# Purpose: program that prints numbers from `1` to `10`, but **skips even numbers** using the `continue` statement.


#            Work on Python
#
# Author:      Soltan
# Created:     16-March-2025
# Updated:     17-March-2025
#-----------------------------------------------------------------------------

# Loop through numbers 1 to 10
for num in range(1, 11):
    if num % 2 == 0:  # Check if the number is even
        continue  # Skip the even number and go to the next iteration
    print(num)  # Print only odd numbers

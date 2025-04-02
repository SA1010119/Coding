#-----------------------------------------------------------------------------
# Name: Set Methods 
# Purpose: Demonstrate copying, popping, and clearing a set.


#            Work on Python
#
# Author:      Soltan
# Created:     2-March-2025
# Updated:     2-March-2025
#----------------------------------------------------------------------------

# Create a set
data = {10, 20, 30, 40, 50}

# Copy the set
data_copy = data.copy()
print("Copy:", data_copy)

# Pop a random element
data.pop()
print("After pop:", data)

# Clear the set
data.clear()
print("After clear:", data)

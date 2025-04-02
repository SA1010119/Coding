#-----------------------------------------------------------------------------
# Name:  Subsets and Supersets
# Purpose: Check if one set is a subset or superset of another.


#            Work on Python
#
# Author:      Soltan
# Created:     2-March-2025
# Updated:     2-March-2025
#----------------------------------------------------------------------------

# Define sets
set_a = {1, 2, 3, 4, 5}
set_b = {2, 3, 4}

# Check subset and superset relations
print(set_b.issubset(set_a))  # True
print(set_a.issuperset(set_b))  # True

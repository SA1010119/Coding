#-----------------------------------------------------------------------------
# Name:        Voting Eligibility Checker
# Purpose:     To know if you can vote or not
#
# Author:      Soltan
# Created:     25-Feb-2025
# Updated:     26-Feb-2025
#----------------------------------------------------------------------------

# Voting Eligibility Checker
# This program checks if a person is eligible to vote based on their age.
# Get the user's age as input
myAge = int(input("Enter your age: "))
# Check if the user is eligible to vote
if myAge >= 18:
    print("You are eligible to vote!")  # 18 or older: Can vote
else:
    print("Sorry, you are not eligible to vote yet.")  # Under 18: Cannot vote

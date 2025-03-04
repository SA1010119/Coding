#-----------------------------------------------------------------------------
# Name:        Even or Odd Number Checker
# Purpose:     To make the student know the even and odd numbers.
#			   Work on Python
#
# Author:      Soltan Arbab
# Created:     25-Feb-2025
# Updated:     26-Feb-2025
#-----------------------------------------------------------------------------

# Ask the user for a number and convert it to an integer
myNumber = int(input("Enter a number: "))
# Check if the number is even or odd
if myNumber % 2 == 0:  # If the number is divisible by 2, it's even
   print("Even")
else:  # If the number is not divisible by 2, it's odd
   print("Odd")

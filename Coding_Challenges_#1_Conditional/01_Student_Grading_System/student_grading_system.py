#-----------------------------------------------------------------------------
# Name:        Student Grading System
# Purpose:     To make the student know their grade, so they know if it's good or not.
#			   Work on Python
#
# Author:      Soltan
# Created:     25-Feb-2025
# Updated:     25-Feb-2025
#-----------------------------------------------------------------------------

# Ask the user to enter their score (out of 100)
myScore = input("Enter your score: ")
# Check the score and assign a grade
if myScore >= "90":  # If score is 90 or above, assign Grade A
   print("Grade: A")
elif myScore >= "80":  # If score is between 80 and 89, assign Grade B
   print("Grade: B")
elif myScore >= "70":  # If score is between 70 and 79, assign Grade C
   print("Grade: C")
elif myScore >= "60":  # If score is between 60 and 69, assign Grade D
   print("Grade: D")
elif myScore >= "50":  # If score is between 50 and 59, assign Grade F
   print("Grade: F")
elif myScore <= "49":  # If score is below 50, print a message
   print("You Are Stupid")

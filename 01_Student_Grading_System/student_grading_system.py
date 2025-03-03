#-----------------------------------------------------------------------------
# Name:        Student Grading System
# Purpose:     To make the student know their grade, so they know if it's good or not.
#			   Work on Python
#
# Author:      Soltan Arbab
# Created:     25-Feb-2025
# Updated:     25-Feb-2025
#-----------------------------------------------------------------------------

myScore = input("Enter your score: ")
if myScore >= "90":
    print("Grade: A")
elif myScore >= "80":
    print("Grade: B")
elif myScore >= "70":
    print("Grade: C")
elif myScore >= "60":
    print("Grade: D")
elif myScore >="50":
    print("Grade: F")
elif myScore <="49":
    print("You Are Stupid")

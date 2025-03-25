#-----------------------------------------------------------------------------
# Name:  Nested List Operations
# Purpose: to learn hie to work with a nested list to access, modify, and manipulate data.


#            Work on Python
#
# Author:      Soltan
# Created:     25-March-2025
# Updated:     26-March-2025
#----------------------------------------------------------------------------

# Create the nested list with student data
students = [['Alice', 25, 'Physics'], ['Bob', 22, 'Chemistry'], ['Charlie', 24, 'Biology']]
# Modify Bob's age and major
students[1][1] = 23  # Change age to 23
students[1][2] = 'Mathematics'  # Change major to Mathematics
# Print the updated list
print("Updated Students List:", students)
# Print the name of the student studying Biology
for student in students:
   if student[2] == 'Biology':
       print("Student studying Biology:", student[0])
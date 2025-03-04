#-----------------------------------------------------------------------------
# Name:        Day of the Week Activity Recommender
# Purpose:     To know the activity based on the day of the week.
#
# Author:      Soltan
# Created:     25-Feb-2025
# Updated:     3-Mar-2025
#----------------------------------------------------------------------------

# Day of the Week Activity Recommender
# This program suggests an activity based on the day of the week.
# Get the current day from the user
day = input("Enter the day of the week: ").strip().capitalize()  # Normalize input
# Suggest an activity based on the day
if day == "Monday":
    print("Start your week with a workout!")
elif day == "Tuesday":
    print("It's a great day to read a book!")
elif day == "Wednesday":
    print("Mid-week movie night!")
elif day == "Thursday":
    print("Try a new recipe!")
elif day == "Friday":
    print("Relax and enjoy the weekend!")
elif day == "Saturday":
    print("Go for a hike!")
elif day == "Sunday":
    print("Prepare for the week ahead with some self-care.")

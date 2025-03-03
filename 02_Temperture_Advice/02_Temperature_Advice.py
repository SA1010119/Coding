#-----------------------------------------------------------------------------
# Name:        Temperature Advice
# Purpose:      for the current temperature and suggests whether they should wear a jacket, short-sleeves, or stay indoors.
#
# Author:      Soltan Arbab
# Created:     25-Feb-2025
# Updated:     27-Feb-2025
#-----------------------------------------------------------------------------

myTemperature = input("What is the temperature: ")
if myTemperature < "10":
    print("It's cold outside. Wear a jacket!")
elif myTemperature <= "25":
    print("It's a nice day. Wear short-sleeves!")
else:
    print("It's hot outside. Stay cool!")


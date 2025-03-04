#-----------------------------------------------------------------------------
# Name:        Temperature Advice
# Purpose:      for the current temperature and suggests whether they should wear a jacket, short-sleeves, or stay indoors.
#
# Author:      Soltan
# Created:     25-Feb-2025
# Updated:     27-Feb-2025
#-----------------------------------------------------------------------------

# Ask the user for the current temperature in Celsius
myTemperature = input("What is the temperature: ")
# Provide advice based on the temperature
if myTemperature < "10":  # If temperature is below 10°C, it's cold
   print("It's cold outside. Wear a jacket!")
elif myTemperature <= "25":  # If temperature is between 10°C and 25°C, it's nice weather
   print("It's a nice day. Wear short-sleeves!")
else:  # If temperature is above 25°C, it's hot
   print("It's hot outside. Stay cool!")


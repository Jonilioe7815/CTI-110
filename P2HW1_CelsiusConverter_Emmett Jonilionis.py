# This is a program which calculates the temperature in farehneit given a degree in celcius
# 23SEP2018
# CTI-110 P2HW1 - Celsius Fahrenheit Converter 
# Emmett Jonilionis
#

#Get the celsius degree from user
degrees_celsius = float(input('enter temperature celsius: '))

# Convert the degrees celsius to degrees farenheit
degrees_farenheit = 9/5 * degrees_celsius + 32

# Display the temperature in degrees farenheit
print('The temperature is  F', format (degrees_farenheit, ',.1f'))

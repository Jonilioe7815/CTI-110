# This program will convert kilometers to miles
# 10NOV2018
# CTI-110 P5T1_KilometerConverter
# Emmett Jonilionis
#

conversion_factor = 0.6214

# This function has a user input kilometers and converts it to miles

def main():

    # User will input the number of kilometers
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the kilometers converted to miles
    show_miles(kilometers)

# This function converts kilometers to "km" to miles and displays the result

def show_miles(km):

    # Calculate the miles    
    miles = km * conversion_factor

    # Display the miles
    print(km, 'kilometers equals', miles, 'miles.')

# Call the main function
main()

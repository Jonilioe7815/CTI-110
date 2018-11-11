# This program will convert inches to feet
# 10NOV2018
# CTI-110 P5T2_FeetToInches
# Emmett Jonilionis
#

inches_per_foot = 12

# This function has a user input feet to be converted to inches

def main():

    # User will input the number of feet
    feet = int(input('Enter a number of feet: '))

    # Convert that to inches
    print(feet, 'equals', feet_to_inches(feet), 'inches.')
    
# This function converts feet to inches

def feet_to_inches(feet):

    return feet * inches_per_foot

# Call the main function
main()

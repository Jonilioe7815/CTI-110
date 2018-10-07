#This program defines shipping price for specified weights
#CTI-110
#P3HW2 - Shipping Charges
#Emmett Jonilionis
#06OCT2018
#

#user inputs the weight in order to find our shipping charge
weight1 = float(input('Please enter the shipping weight of your package in Lbs:'))

#Determine the shipping charge
if weight1 >=.01 and weight1 <= 2.00:
    print('Your shipping charge is $1.50')
elif weight1 >= 2.01 and weight1 <= 6.00:
    print('Your shipping charger is $3.00')
elif weight1 >= 6.01 and weight1 <= 10.00:
    print('Your shipping charge is $4.00')
elif weight1 >= 10.01:
        print('Your shipping charge is $4.75')
else:
    if weight1 < .01:
        print('Error, please enter a valid weight')

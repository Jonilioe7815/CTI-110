#This program converts whole numbers between 1 and 10 to Roman Numerals
#CTI-110
#P3HW1 - Roman Numerals
#Emmett Jonilionis
#06OCT2018
#

#User inputs a whole number between 1 and 10
number = int(input('Enter a whole number between 1 an 10:'))

#Convert the number to a Roman Numeral
if number == 1:
    print('The Roman Numeral is: I')
elif number == 2:
    print('The Roman Numeral is: II')
elif number == 3:
    print('The Roman Numeral is: III')
elif number == 4:
    print('The Roman Numeral is: IV')
elif number == 5:
    print('The Roman Numeral is: V')
elif number == 6:
    print('The Roman Numeral is: VI')
elif number == 7:
    print('The Roman Numeral is: VII')
elif number == 8:
    print('The Roman Numeral is: VIII')
elif number == 9:
    print('The Roman Numeral is: IX')
elif number == 10:
    print ('The Roman Numeral is: X')
else:
    if number < 1 or number > 10:
        print('Error. The number is out of range, input a number between 1 and 10')

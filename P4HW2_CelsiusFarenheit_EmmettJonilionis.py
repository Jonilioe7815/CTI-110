#This program displays the degree C for 20 degrees and converts it to F
#25OCT2018
#CTI-110 P4HW2 - Celsius to Farenheit Table
#Emmett Jonilionis
#

#define the main portion of the code

def main():

#make a table for the Celsius and the corresponding Farenheit conversion

    print('Degrees Celsius\tDegrees Farenheit')
    print('----------------------------------')

#display the degrees in Celsius and farenheit from a for loop 

    for number in range (1, 21):
        convert = 9/5 * number +32
        print(number, '\t', convert)

main()

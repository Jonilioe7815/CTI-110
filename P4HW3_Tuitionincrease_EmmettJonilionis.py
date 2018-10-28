#This program applies a three percent increase over five years of semseter
#tutition
#27OCT2018
#CTI-110 P4HW3 - Tuition Increase
#Emmett Jonilionis
#

#Create the main
def main():

#define the variables for the running totals

    year = 0
    tuition = 8000

#Create the table for the display of information

    print('Year\tTuition Amount')
    print('--------------------')

#create the loop and formula for the three percent tuition increase for 5 years

    for year in range (1, 6):
        tuition += ( 3 / 100) * tuition
        print(year,'\t',format(tuition,'.2f'))

main()

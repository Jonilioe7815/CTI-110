# This program calculates percentage of students based on gender in a 20 student class
# 23SEP2018
# CTI-110 P2HW2 - Male Female Percentage
# Emmett Jonilionis
#

#get the number of males and females in a class
males = float(input('Enter number of males: '))
females = float(input('Enter number of females: '))

#calculate the percentage of males based on 20 students
Percent_males = males / 20 

#calculate the percentage of females based on 20 students
Percent_females = females / 20 

#diplay the percentage of males and females in a class
print('The percent of Males is  ', format (Percent_males, '.0%'))
print('The percent of Females is  ',format (Percent_females, '.0%'))


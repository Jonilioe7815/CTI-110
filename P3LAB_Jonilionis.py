# This program takes a number grade and outputs a letter grade.
# CTI-110
# P3LAB - Debugging
# Emmett Jonilionis
# 07OCT2018
#

#define what score determines the corresponding letter grade
def main():
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

#have the user input the number score    
    score = int(input('Enter number score: '))

#assign and print the letter grade that corresponds to the number score
    if score >= A_score:
        print('Your grade is: A')
    else:
        if score >= B_score:
            print('Your grade is: B')
        else:
            if score >= C_score:
                print('Your grade is: C')
            else:
                if score >= D_score:
                    print('Your grade is: D')
                else:
                    print('Your grade is: F')
main()






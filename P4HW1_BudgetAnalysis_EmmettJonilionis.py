#This is a budget analysis program that takes some values and tells the user if they are over
#or under thier input of a projected budget
#25OCT2018
#CTI-110 P4HW1 - Budget Analysis
#Emmett Jonilionis
#


def main():
#define the variables

    AExpenses = 'y' or 'Y'
    TotExp = 0

#have the user input their budget for the month

    Budget = float(input('Enter the budget for the month: '))

#create the input validation loop for the user to be able to stop the loop

    while AExpenses == "y":
        userExpense = float(input("Enter an expense: "))
        TotExp += userExpense
        AExpenses = input("Do you have another expense to add?: Type y "+ \
                         "for yes, or n for no: ")

#calculate if the user is over, under or right on the budget that they entered

        if TotExp > Budget:
            print("You were over your budget of","$" + format( Budget, ",.2f"), \
                  "by $", format (TotExp - Budget, ",.2f"))
        elif Budget > TotExp:
            print("You were under your budget of","$" + format( Budget, ",.2f"), \
                  "by $", format ( Budget - TotExp, ",.2f"))
        else:
            if Budget == TotExp:
                print("You used your exact budget of","$" + format( Budget, ",.2f"))
    
main()

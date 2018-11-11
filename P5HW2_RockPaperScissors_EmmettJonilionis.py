#This program pits the user in an epic Rock Paper Scissors battle with a computer
#11NOV2018
#CTI-110 P5HW2 - Rock, Paper, Scissors
#Emmett Jonilionis
#

#This function creates a Rock Paper Scissors game
def main():
    import random
    user = ''

#create a while loop in order to populate the game and as for input from
#the user

    while user != 'q':
        print('Select Rock, Paper or Scissors')
        print('type r for rock\ntype p for paper\ntype s for scissors\nor q to quit')
        user = input('')
        user = user.lower()
        if user == 'q':
            break
        pc = random.randrange(1, 4)
        choice = pc

#assign number value to the "random" PC selection
        if   pc == 1:
            choice = 'rock'
        elif pc == 2:
            choice = 'paper'
        else:
            pc == 3
            choice = 'scissors'
        
# assign a number value to each user selection
        if user == 'r':
            user = 1
        elif user == 'p':
            user = 2
        else:
            user == 's'
            user = 3

        print('The computer picked:', choice)

#establish who won the match
        
        if user == 1 and pc == 3:
            print('You beat the computer\n')
        elif user == 3 and pc == 1:
            print('You lost to the computer\n')
        elif user > pc:
            print('You beat the computer\n')
        elif user < pc:
            print('You lost to the computer\n')
        else:
            user == pc
            print('You tied the computer\n')

#Call the main
main()

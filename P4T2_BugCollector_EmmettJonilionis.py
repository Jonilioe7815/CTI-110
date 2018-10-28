#this program collects a running total of over seven days, a number of bugs
#that a user has input as collected and displays them
#25OCT2018
#CTI-110 P4T2 - Bug Collector
#Emmett Jonilionis
#

#Create the nest
def main():
    total = 0
#get the bugs collected per day for seven days
    for day in range (1,8):
        print('Enter the number of bugs collected on day', day)
#input the number of bugs
        bugs = int(input())
        total += bugs
#display the total number of bugs
    print('You have collected', total, 'bugs')

main()

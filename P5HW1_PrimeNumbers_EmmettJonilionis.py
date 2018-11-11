#This program identifies if a number is prime or not based on user input numbers
#11NOV2018
#CTI-110 P5HW1 - Prime Numbers
#Emmett Jonilionis
#

#This function identifies if a number is prime or not based on user input
def main():

    # define what a prime number is and eliminate negatives and 1

    def is_prime(n):
        if (n<2):
            return False

        # generate the range of prime number seeking and if it is prime or not

        for i in range(2,n//2+1):
            if(n%i==0):
                return False
        return True

    # display to the user if the number is prime or not

    num = int(input("Enter a number: "))
    if is_prime(num):
        print(num, "is a prime number")
    else:
        print(num, "is NOT a prime number")

main()

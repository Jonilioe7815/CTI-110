#The turtle will draw a square and a triangle for you
#27OCT2018
#CTI-110 P4Lab1 "Tutorial 1"
#Emmett Jonilionis
#

#import the turtle
import turtle
AName = turtle.Turtle()

#make the main block

def main():

#create the square loop for the turtle
    
    for _ in range(4):
        AName.forward(60)
        AName.right(90)
    AName.penup()
    AName.forward(100)
    AName.pendown()
#Create the triangle loop for the turtle
    
    for _ in range(3):
        AName.forward(60)          
        AName.left(120)

main()



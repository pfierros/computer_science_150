#Author: <name>
#Date: <date>
#Language: Python3
#Assignment: Lab 1, montecarlo.py 
#Class: CSCI150 
###########################################################################
#DEPENDENCIES
import random 
import picture as p
###########################################################################
#Create Canvas 
canvas = p.Picture(600, 600)

#Tells user what program does 
print("This program calculates the calue of Pi by simulating the throwing of darts onto a round target on a square background.")
#Set Canvas Color 
canvas.setFillColor(97, 250, 240)
#Print circle 
p.Circle(300,300,300,fill=True)
#Ask user for input
user_input  = int(input("How many darts do you want to throw?"))
#Set Dart Color 
canvas.setFillColor(0,0,0)
#Place darts onto Canvas
for dart in range(user_input):
    randX = random.randint(0,600)
    randY = random.randint(0,600)
    canvas.drawCircleFill(randX,randY,5)
    
input() 
#File Name: FinalProjectGame.py
# Grisel Nunez
#Date: Aug 2,2020
#Program Description: Board like game for final project

import time
import random

#cards and card scenarios
card1= "You are Timmy the high schooler"
card2= "You are John the Soldier"
card3= "You move forward"
card4= "You spot the evil creature"
card5= "You try to sneakily move past the evil creature"
card6= "You move forward past the evil creature"
card7= "You move slightly closer to freedom"
card8= "You move to pick up a weapon"
card9= "You run from the creature"
card10= "You are safe"
yes= "yes", "y", "Y"
no= "no", "n", "N"

#Number of spaces/positions
c1=1
c2=1
c3=2
c4=4
c5=6
c6=6
c7=2
c8=4
c9=3
c10=8

#answer choices for menus
answerA= "A", "a"
answerB= "B", "b"
answerC="C","c"

#Accumulator
position= 0.0

#Grabbing objects used for weapons
laser=0

required= ''

#Game is broken into sections, starting with main function

def main():
    #Header/ Introduction
    print("######     #    ######     #    #       #       ####### #")       
    print("#     #   # #   #     #   # #   #       #       #       #")       
    print("#     #  #   #  #     #  #   #  #       #       #       #")       
    print("######  #     # ######  #     # #       #       #####   # ")      
    print("#       ####### #   #   ####### #       #       #       #")       
    print("#       #     # #    #  #     # #       #       #       #")       
    print("#       #     # #     # #     # ####### ####### ####### #######")
    time.sleep(.5)
                                                                
    print("\n#     # #     # ### #     # ####### ######   #####  ####### ")
    print("#     # ##    #  #  #     # #       #     # #     # #")       
    print("#     # # #   #  #  #     # #       #     # #       #")      
    print("#     # #  #  #  #  #     # #####   ######   #####  #####")   
    print("#     # #   # #  #   #   #  #       #   #         # # ")      
    print("#     # #    ##  #    # #   #       #    #  #     # # ")      
    print(" #####  #     # ###    #    ####### #     #  #####  #######")
    time.sleep(.5)

    print("\n   #    ######  #     # ####### #     # ####### #     # ######  #######")    
    print("  # #   #     # #     # #       ##    #    #    #     # #     # #")          
    print(" #   #  #     # #     # #       # #   #    #    #     # #     # # ")         
    print("#     # #     # #     # #####   #  #  #    #    #     # ######  #####")      
    print("####### #     #  #   #  #       #   # #    #    #     # #   #   #")          
    print("#     # #     #   # #   #       #    ##    #    #     # #    #  #")          
    print("#     # ######     #    ####### #     #    #     #####  #     # #######  ")
    time.sleep(.5)
                                                                           
    print("\n #####     #    #     # ####### ")
    print("#     #   # #   ##   ## #")       
    print("#        #   #  # # # # # ")    
    print("#  #### #     # #  #  # ##### ")  
    print("#     # ####### #     # # ")      
    print("#     # #     # #     # # ")      
    print(" #####  #     # #     # ####### ")
    time.sleep(1)

    

    #GAME DESCRIPTION & RULES
    print("\n\nWelcome to the Parallel Universe Adventure Game!")
    print ("\n\nYou have been abducted by evil persons from a parallel universe and they")
    print ("would like to use you as an experiment!")
    print ("OH NO! BUT YOU CANNOT LET THAT HAPPEN!")
    print ("In this game you will have run through different scenarios and use your skills")
    print ("to outrun these evil people and survive.")
    print ("Your ultimate goal is to get back to earth in one piece!")
    print ("*******************************************************************************")

    #RULES
    print ("\n\nThe rules of the game are:")
    print ("1. You will first be given a character")
    print ("2. After choosing your character, you will draw cards for different scenarios")
    print ("These cards will determine your fate in the game, so choose wisely.")
    print ("GOOD LUCK!")
    print ("*******************************************************************************")
    
    #Using random and input functions to draw cards for character
    shuffle= input ("\n\nPress any key to draw a card:")
    time.sleep(1)
    choice=random.randint (1,2)
    print ("Your card is:", choice) 


    if choice==1:
        print ("\n\n")
        print (card1) #Character name
        print ("You are at position:",c1)
        option_1() #Scenario given
    elif choice==2:
        print ("\n\n")
        print (card2)
        print ("You are at position:",c2)
        option_1()
       
    else:
        print ("Try again")

    print ("*******************************************************************************")

    
#Function for first scenario using input validation and a menu
def option_1():
    print ("\n\nYou have encountered an evil creature that is trying to attack you!")
    print ("*******************************************************************************")
    shuffle= input ("\n\nHit any key to draw a card:")
    choice=random.randint (3,5)
    print ("Your card is:", choice)

    if choice==3:
        print ("\n\n")
        print (card3)
        print ("You are at position:", c3)
    elif choice==4:
        print ("\n\n")
        print (card4)
        print ("You are at position:",c4)
    elif choice==5:
        print ("\n\n")
        print (card5)
        print ("You are at position:", c5)
    else:
        print ("Try again")
    
    time.sleep(.5)
    print ("\nChoose what you would like to do.")
    print ("A. Run")
    print ("B. Throw a grenade")
    print ("C. Hide")

    answer= input ("Please pick an option:")

    if answer in answerA:
        option_2()
    elif answer in answerB:
        print ("Oh no. You launched the grenade but it didn't go off and"
                   " the creature ate you! You died!")
    elif answer in answerC:
        option_3()
    else:
        print ("Please try again")

    print ("*******************************************************************************")

     
#Function for second scenario using input validation and a menu       
def option_2():
    print ("You made it to the next step and moved closer to a vortex.")
    shuffle= input ("\n\nPress any key to draw a card:")
    choice=random.randint(6,8)
    print ("Your card is:", choice)
    
    if choice==6:
        print ("\n\n")
        print (card6)
        print ("You are at position:", c6)
    elif choice==7:
        print ("\n\n")
        print (card7)
        print ("You are at position:",c7)
    elif choice==8:
        print ("\n\n")
        print (card8)
        print ("You are at position:", c8)
    else:
        print ("Try again")
    
    time.sleep(.5)
    print ("\n\nChoose what you would like to do.")
    print ("A. Hide")
    print ("B. Fight")
    print ("C. Run")
    

    answer= input ("Please pick a choice:")

    if answer in answerA:
        option_3()
    elif answer in answerB:
        print (" Oh no, the vortex swallowed you! You didn't make it!")
        time.sleep(1)
        print ("GAME OVER.")
    elif answer in answerC:
        option_3()
    else:
        print ("Please try again")

    print ("\n*******************************************************************************")
    

#Function for scenario 3 using input validation and a menu
def option_3():
    print ("\n\nCongrats! You made it this far! But even though you thought you were safe")
    print ("the creature still spots you!")
    shuffle= input ("\n\nPress any key to draw a card:")
    choice=random.randint(9,10)
    print ("Your card is:", choice)

    if choice==9:
        print ("\n\n")
        print (card9)
        print ("You are at position:", c9)
    elif choice==10:
        print ("\n\n")
        print (card10)
        print ("Current position:", c10)
    else:
        print ("Try again")

    
    time.sleep(.5)
    print ("Choose what you would like to do next.")
    print ("A. Hide")
    print ("B. Run")
    print ("C. Fight")

    answer= input ("Please pick a choice:")

    if answer in answerA:
        print ("\n\nAhh! You were spotted! GAME OVER.")
    elif answer in answerB:
        print ("\n\nYou can't outrun the creature! GAME OVER.")
    elif answer in answerC:
        option_4()
    else:
        print ("Please Try Again.")

    print ("*******************************************************************************")
    

#Function for scenario 4 using input validation and a menu
def option_4():
    print ("\n\nYAY! You're almost free and might make it back to Earth!")
    print ("But first, you must defeat the evil scientists waiting for you")
    print ("at the end of your trek!")
    print ("Are you up for the challenge? Type yes or no (Y or N)?")

    choice= input ("Please make your choice here:")
    print ("*******************************************************************************")

    if choice in yes:
        laser=1 #adds a laser/ acquires a laser
    else:
        laser=0
    print ("\n\nYou hear massive footsteps! IT'S THE MONSTER!")
    time.sleep(1)

    if laser>0:
        print ("\n\nYou use your laser and you fight!")
        print ("You are worried it won't stop the monster but you try anyway")
        print ("But it works! You killed the monster and you lived!")

        print("\n#   # ####### #     #") 
        print("#  #  #     # #     #") 
        print("# #   #     # #     #") 
        print(" #    #     # #     # ")
        print(" #    #     # #     #") 
        print(" #    #     # #     #") 
        print(" #    #######  ##### ")
        time.sleep(.5)
                        
        print("\n#     # ####### #     #") 
        print("#  #  # #     # ##    #") 
        print("#  #  # #     # # #   #") 
        print("#  #  # #     # #  #  #") 
        print("#  #  # #     # #   # #")
        print("#  #  # #     # #    ##") 
        print(" ## ##  ####### #     # ")
        time.sleep(.5)

        position= float (c10)
        print ("Your ending total position=",position)
    else:
        print ("\n\nOh no, you should've used the laser! You lost!")
        
        print("\n #####     #    #     # ####### ")
        print("#     #   # #   ##   ## #")       
        print("#        #   #  # # # # # ")    
        print("#  #### #     # #  #  # ##### ")  
        print("#     # ####### #     # # ")      
        print("#     # #     # #     # # ")      
        print(" #####  #     # #     # ####### ")
        time.sleep(.5)


        print("\n\n####### #     # ####### ######")  
        print("#     # #     # #       #     #") 
        print("#     # #     # #       #     #") 
        print("#     # #     # #####   ######")  
        print("#     #  #   #  #       #   # ")  
        print("#     #   # #   #       #    #")  
        print("#######    #    ####### #     #")
        time.sleep(.5)
        
        print ("*******************************************************************************")

#Open file in read mode
        file= open( "grades.txt","r")
        file=file.readline()
        file=file.close()



main()
        
    


   
    

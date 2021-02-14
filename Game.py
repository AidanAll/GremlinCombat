#written by: Aidan All
#text based battle game to get some python exp and learn how to store shit in text files

import random #Random number generation is basically how I'm gonna build the combat system
import math
import string

#This code opens the high score text file and reads its contents to variable 'high_score'
file_hs = open(r"C:\Users\Owner\Desktop\Code Demo\GremlinCombat\High_Score.txt","r")
high_score = file_hs.read()
file_hs.close()

player_health = 100 
gremlin_health = 100
player_damage = 1.00
gremlin_damage = 1.00

#Introduction
print("Welcome Adventurer, what is your name? ")
name = input() #Getting users name
print("Hello "+ name + "! Keep an eye out, there is danger in every- LOOK OUT A GREMLIN!!")
print("Type Start when you are ready.")
begin = input()

#Game code
if begin =="start" or "Start":
    print("alright "+ name + ", you have three options: \n Heavy Attack(50%) \n Light attack(80%) \n Block(60%)")

    counter = 0 #This is for tracking how many times the Combat loop runs

    #Combat loop
    while player_health > 0 and gremlin_health > 0: #iterates until player or gremlin health hits 0
        counter += 1
        print("")
        print("Which move do you want to use?")
        move = input().lower() #gets the move the user wants to use and case checks it.

        #Heavy attack
        if move == "heavy attack" or move == "heavy":
            chance = random.randint(1,2) #chance of success 

            #successful heavy attack
            if chance==1: 
                gremlin_health -= 15 * player_damage
                print("You hit the gremlin with a heavy attack! \n Your health: ", round(player_health) ,"\n Gremlin health: ", round(gremlin_health))
             
                if gremlin_health < 50:
                    print("The gremlin looks hurt...")

            #miss   
            else: 
                player_health -= 5 * gremlin_damage
                print("You missed and the gremlin countered! \n Your health: " ,round(player_health), "\n Gremlin health: ",round(gremlin_health))


        #Light attack
        elif move == "light attack" or move == "light":
            chance = random.randint(1,5) #chance of success

            #successful light attack
            if chance<5: 
                gremlin_health -= 5 * player_damage
                print("You hit the gremlin with a light attack! \n Your health: ", round(player_health) ,"\n Gremlin health: ", round(gremlin_health))
              
                if gremlin_health < 50:
                    print("The gremlin looks hurt...")
            #miss
            else:
                player_health -= 5 * gremlin_damage
                print("You missed and the gremlin countered! \n Your health: ",round(player_health) , "\n Gremlin health: ", round(gremlin_health))
      
        #Block
        elif move == "block":
            chance = random.randint(1,10)

            #successful block
            if chance < 7:
                gremlin_damage -= .05
                print("You blocked the gremlin's strike and damaged his weapon!(-Gremlin Damage) \n Your health: ",round(player_health),"\n Gremlin health: ",round(gremlin_health))
            
            #failed block
            else:
                player_health -= 5 * gremlin_damage
                print("You failed to block.\n Your health: ", round(player_health) ,"\n Gremlin health: ",round(gremlin_health))

        else: 
            print("not a valid move")

     #Loss       
    if player_health <= 0:
        print("Oof! The gremlin got you")
    
    #Win
    elif gremlin_health <= 0:
        print("Good job! Looks like you showed that gremlin who's boss.")
        print("you killed the gremlin in ",counter," moves.")

        #Checks if there is a new high score. 
        if int(high_score) == 0 or counter < int(high_score):
            print("New High Score!")
            file_hs = open(r"C:\Users\Owner\Desktop\Code Demo\GremlinCombat\High_Score.txt","w")
            file_hs.write(str(counter)) #writes new high score to text file
            file_hs.close()
        else:
            print("High Score: ", high_score," moves")
        
else: 
    print("Type Start when you are ready.")

#Notes: 
#Increase gremlin damage and buff block move. Makes blocking useful and spamming heavy attack less viable. 
#Randomize the amount of damage a move does each time. i.e. Heavy Attack has a chance to deal between 10-20 dmg.
#Maybe add an algorithim for rating player preformance based on moves taken and health left. 
#Add sound effects
#Possibly break out combat loop into its own .py file


            



                

        
            
    
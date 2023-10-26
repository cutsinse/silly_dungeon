#Silly Dungeon, try again! (Ex45.py)

from sys import exit
from textwrap import dedent

from  sd_user import *
from sd_rooms import *
from sd_items import *

#step 1: create single instances of the items, the rooms, the user. 
	#single instances are important so that changes 
	#can be saved to each instance as player does things, such as take items

#This creates a single instance of the dictionary of all the items 
#in the game. 
item_dict = IEngine().all_items

#This creates single instances all of the rooms in the game.
alchemy = Alchemy()
enchanting = Enchanting()
basement = Basement()
entryway = Entryway()


	

print("*" * 5, "Welcome to the Silly Dungeon", "*" * 5)
player_name = input("What is your name?\n").lower()

#creates the user instance. 
user = User(player_name, ["bag"])


print(dedent(f"""
Welcome {player_name.capitalize()}!
This is a simple typing game, type what you want to do and explore!
To win, find and open the treasure chest!  Also, don't die....

This game only has a fixed set of commands, to see the list, just type
"help" or even just "h".

Good luck!

"""))
#The "help" function is a general Room class function.  The user is automatically 
#put into a room, and will always be in a room for the game. 

input("Press enter to continue")
print(" ")


#Below is the first major loop.  This loop is what changes what the 
	#current room is, and uses single instances of the rooms to 
	#save any changes made as the player moves from room to room. 
	
	#the enter function always returns a string with the name of the 
	#room to enter next. 
	#For the second major game play loop, the one ther player will 
	#interact with, see sd_rooms.py, class Room(), function enter()

dev_input = entryway.enter(user, item_dict)
while True:
	if dev_input == 'alchemy':
		dev_input = alchemy.enter(user, item_dict)
	elif dev_input == 'enchanting':
		dev_input = enchanting.enter(user, item_dict)
	elif dev_input == 'basement':
		dev_input = basement.enter(user, item_dict)
	elif dev_input == 'entryway':
		dev_input = entryway.enter(user, item_dict)
	elif "q" in dev_input:
		print('bye!')
		exit(0)
	



#Silly Dungeon, try again! (Ex45.py)

from sys import exit
from textwrap import dedent

from  sd_user import *
from sd_rooms import *
from sd_items import *



#This creates a single instance of the dictionary of all the items 
#in the game. 
item_dict = I_Engine().all_items

#This initializea all of the rooms in the game
alchemy = Alchemy()
enchanting = Enchanting()
basement = Basement()
entryway = Entryway()


	

print("*" * 5, "Welcome to the Silly Dungeon", "*" * 5)
player_name = input("What is your name?\n").lower()
#For testing I got tired of dealing with the input part

player = User(player_name, ["bag"])

#test area, turn play to True to activate the game loop. 

print(dedent(f"""
Welcome {player_name.capitalize()}!
This is a simple typing game, type what you want to do and explore!
To win, find and open the treasure chest!  Also, don't die....

This game only has a fixed set of commands, to see the list, just type
"help" or even just "h".

Good luck!

"""))

input("Press enter to continue")
print(" ")
#gameplay loop. 
dev_input = entryway.enter(player, item_dict)
while True:
	if dev_input == 'alchemy':
		dev_input = alchemy.enter(player, item_dict)
	elif dev_input == 'enchanting':
		dev_input = enchanting.enter(player, item_dict)
	elif dev_input == 'basement':
		dev_input = basement.enter(player, item_dict)
	elif dev_input == 'entryway':
		dev_input = entryway.enter(player, item_dict)
	elif "q" in dev_input:
		print('bye!')
		exit(0)
	



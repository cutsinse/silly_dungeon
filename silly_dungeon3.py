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


	


player_name = "Sally" #input("What is your name?\n")
#For testing I got tired of dealing with the input part

player = User(player_name, ["bag"])

#test area, turn play to True to activate the game loop. 


#gameplay loop. 
dev_input = entryway.enter(player, item_dict)
while True:
	if dev_input == 'alchemy':
		dev_input = alchemy.enter(player, item_dict)
	elif dev_input == 'enchanting':
		dev_input = enchanting.enter(player, item_dict)
	elif dev_input == 'basement':
		dev_input == basement.enter(player, item_dict)
	elif dev_input == 'entryway':
		dev_input = entryway.enter(player, item_dict)
	elif "q" in dev_input:
		print('bye!')
		exit(0)
	



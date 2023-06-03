#Silly Dungeon, try again! (Ex45.py)

from sys import exit
from textwrap import dedent

from  sd_user import *
from sd_rooms import *
from sd_items import *
from sd_engine import *

#Initializing all the items in the game:
#These are items that have their own classes and methods

red = Red()
#does not teleport
blue = Blue()
green = Green()
purple = Purple()
yellow = Yellow()
chest = Chest()
#it not added to an inventory yet, should be added to the alchemy inventory 
#after drinking the yellow potion
paper = Paper('paper', """
	It's rolled up, but very loosely.
	Doesn't look like anyone cared about it much 
	""", 
	"""
	red = poison 
	blue = enchanting room 
	green = entrance 
	purple = basement 
	yellow = chest
	""")

#does not teleport

#This are simple items that the user can collect, but can't really
#do anything with as of yet.
bag = Item('bag of holding', 'this is a test item')
key = Item('key', 'A shiny, gold key, with no markings on it.')
sword = Item('sword', 'It is a simple, but effective, sword')
stone = Item('glowing stone', "It's a stone....that glows!!")
knife = Item('knife', """
It looks like a utility knife, used for cutting leather or the like
""")

#This initializea all of the rooms in the game, and sets which items 
#are in the inventory of each room at the start of the game. 
alchemy = Alchemy([red, blue, green, purple, yellow])
enchanting = Enchanting([key, sword, stone, knife])
basement = Basement([paper])
entryway = Entryway([])

#functions needed to add teleport targets for the potions
blue.set_teleport_target(enchanting)
green.set_teleport_target(entryway)
purple.set_teleport_target(basement)



current_room = entryway


player_name = "Sally" #input("What is your name?\n")
#For testing I got tired of dealing with the input part

player = User(player_name, [bag])

play = True

#test area, turn play to True to activate the game loop. 


#gameplay loop. 
current_room.enter()
while play == True:

	current_room_dict_list = items_dict(current_room)
	choice = input("> ").lower()
	if "straight" in choice or "door" in choice:
		current_room = alchemy
	elif "up" in choice:
		current_room = enchanting
	elif "down" in choice:
		current_room = basement
	elif "q" in choice:
		exit(0)
	elif 'inventory' in choice:
		player.check_inventory()
		break
	else:
		player.troll()
	current_room.enter()
	current_room_dict_list = items_dict(current_room)
	player_dict_list = items_dict(player)
	while True:
		
		choice2 = input("What now? \n").lower()
		choice2_split = choice2.lower().split()
		#The user input is now a list of words, all lowercase 
		
		#creating 2 separate variables for the input allows for 2, separate
		#processes, one to handle single word items, 
		#but you can take more than one at a time
		#and one to handle multiple word items, but you can only take 
		#one at a time. (
			#ex: you can't take the "yellow potion" and "blue potion" 
			#with a single command "take the yellow and blue potions"
			
		if "take" in choice2:
			for word in choice2_split:
				#This loops through the choice2_split list to look for matching
				#items in the current_room.inventory list and if they match
				#goes to the player.take() function to take the item from
				#the room inventory list and put it in the 
				#player inventory list
				if word in current_room_dict_list:
					player.take(current_room_dict_list[word], current_room)
				elif word in player_dict_list:
					print('You already took that')
					
				else:
					#By passing, this helps disregard any non-useful words
					#like "the" or other grammer words
					#Unfortunately, this loop is limited in that I can 
					#only use single word items in the inventories 
					#and I don't have a way to use synonyms or account for
					#plural vs singular of the items
					pass
			#this section handles choice2 as a joined string, 
			#allowing for multiple word items to be taken. 
			#not the prettiest option		
			if "blue potion" in choice2:
				player.take('blue potion', current_room)
			elif "red potion" in choice2:
				player.take(red, current_room)
			elif "purple potion" in choice2:
				player.take('purple potion', current_room)
			elif "green potion" in choice2:
				player.take('green potion', current_room)
			elif "yellow potion" in choice2:
				player.take('yellow potion', current_room)
			elif "stone" in choice2 or "glow" in choice2:
				player.take('glowing stone', current_room)
			else:
				pass			
			
			player.check_inventory()
			current_room.check_inventory()
			
		elif "drink" in choice2:
			if "blue" in choice2:
				current_room = blue.drink()

		elif "leave" in choice2:
			current_room = entryway
			break
		elif "q" in choice2:
			exit(0)
		else:
			print("I don't understand")

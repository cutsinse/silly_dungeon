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

	


player_name = "Sally" #input("What is your name?\n")
#For testing I got tired of dealing with the input part

player = User(player_name, [bag])

#test area, turn play to True to activate the game loop. 


#gameplay loop. 
dev_input = entryway.enter(player)
while True:
	if dev_input == 'alchemy':
		dev_input = alchemy.enter(player)
	elif dev_input == 'enchanting':
		dev_input = enchanting.enter(player)
	elif dev_input == 'basement':
		dev_input == basement.enter(player)
	elif dev_input == 'entryway':
		dev_input = entryway.enter(player)
	elif "q" in dev_input:
		print('bye!')
		exit(0)
	



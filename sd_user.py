#This is a module that holds the user class, and all the commands the 
#user can execute. 

from sys import exit
from textwrap import dedent

from sd_items import *

class User():
	#contains all the user specific functions and the inventory variable.
	#There is only 1 instance, the variable of which is named "player"
	def __init__(self, name, items):
		self.name = name.capitalize()
		self.inventory = items
		#inventories are lists of strings, exactly like the room 
		#inventories.  For more details, see sd_rooms.py comments

	def check_inventory(self):
		print(self.inventory)
	
	def take(self, item, item_dict, current_room):
		#The item variable is taken from user input, see sd_rooms enter function 
		#loop for more details. 
		#Takes in the instances of the item dictionary and rooms created in silly_dungeon3.py
		
		if item in current_room.inventory:
			item_object = item_dict.get(item)
			#setting this variable is what links to the string in the
			#list of inventories
			#to the item objects themselves
			
			if item_object.taken == False:
				self.inventory.append(item)
				current_room.inventory.remove(item)
				item_object.taken = True
			elif item_object.taken == True:
				print("""item_object.taken == True, but it was found in
				the current_room.inventory? """)
				#if all goes according to plan, this elif statment should 
				#never be seen. It is here for testing purposes 
		else:
			print("""Item not taken.  Did you already take it?.""")
	


	def blank(self):
		"""Used when the user tries to take something not from the list or that they cannot take"""
		print("That's not here")
	def troll(self):
		"""Used when the user types something in the program can't do anything with"""
		print(f"I'm sorry {self.name} I don't understand\n")

	def poof(self):
		"""used when the user drinks a potion that takes them to another room."""
		print("""\n***As the potion is consumed, you are engulfed in a swirling vortex of color and sensation!***\n""")

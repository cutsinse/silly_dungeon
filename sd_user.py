#This is a module that holds the user class, and all the commands the 
#user can execute. 

from sys import exit
from textwrap import dedent

from sd_items import *

class User():
	#contains all the user specific functions and the inventory variable.
	#There is only 1 instance, the variable of which is named "player"
	def __init__(self, name, items):
		self.name = name
		self.inventory = items

	def check_inventory(self):
		for item in self.inventory:
			print(f"[{item.name},]")
	
	def take(self, item, current_room):
		if item in current_room.inventory:
			if not item.taken:
				current_room.inventory.remove(item)
				self.inventory.append(item)
				item.taken = True
		else:
			print("You can't do that")
	
	def drop(self, item, current_room):
		if item in self.inventory:
			self.inventory.remove(item)
			current_room.inventory.append(item)
		else:
			print("You can't do that")

	def blank(self):
		"""Used when the user tries to take something not from the list or that they cannot take"""
		print("That's not here")
	def troll(self):
		"""Used when the user types something in the program can't do anything with"""
		print(f"I'm sorry {self.name} I don't understand\n")

	def poof(self):
		"""used when the user drinks a potion that takes them to another room."""
		print("""\n***As the potion is consumed, you are engulfed in a swirling vortex of color and sensation!***\n""")

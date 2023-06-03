#This is the module that holds all the room classes

from sys import exit
from textwrap import dedent

from sd_items import *

class Room(object):
	#this will hold the general room functions
	def __init__(self, items):
		self.inventory = items
		
	def enter(self):
		print(f"You are in the {self.name}. \n", dedent(self.desc))
	
	def look_around(self):
		print(dedent(self.desc))
	
	def check_inventory(self):
		for item in self.inventory:
			print(f"-{item.name}")
		#the self.inventory attribute will be defined in each individual
		#child class.
	
	
class Alchemy(Room):
	
	def __init__(self, items):
		super(Alchemy, self).__init__(items)
		self.desc = """
			The room is dimly lit and filled with the heady aroma of various ingredients. 
			On a cluttered table, four small vials stand out, each containing a shimmering potion in the following colors: 
			red, purple, green, blue, and yellow, each promising their own unique magical effects."""
		self.name = 'Alchemy Room'

		


class Enchanting(Room):
	
	def __init__(self, items):
		super(Enchanting, self).__init__(items)
		self.desc = """
		This is a magical room, with a glowing stone, a knife, 
		a sword and a key.
		"""
		self.name = 'Enchanting Room'


class Entryway(Room):
	
	def __init__(self, items):
		super(Entryway, self).__init__(items)
		self.desc = """
			In front of you, you see:
			A wooden door straight ahead
			A staircse going up
			A staircase going down
			"""
		self.name = 'Entryway'


class Basement(Room):
	def __init__(self, items):
		super(Basement, self).__init__(items)
		self.desc = """
			The basement is very steriotypical. It's damp, with dripping pipes 
			in the ceiling, and you see a peice of paper on top of a 
			few barrels of god knows what.
			"""

		self.name = 'Basement'



	

	
	
	

#This is the module that holds all the room classes

from sys import exit
from textwrap import dedent

from sd_items import *

class Room(object):
	#this will hold the general room functions
	def __init__(self, items):
		self.inventory = items
		
	def enter_callback(self):
		print(f"You are in the {self.name.capitalize()} Room. \n", dedent(self.desc))
		print("What will you do now?")
	
	def look_around(self):
		print(dedent(self.desc))
	
	def check_inventory(self):
		print(self.inventory)
		
	
	
class Alchemy(Room):
	
	def __init__(self):
		super(Alchemy, self).__init__([
		"red potion", "blue potion", "green potion", 
		"purple potion", "yellow potion", "bag"
		])
		self.desc = """
			The room is dimly lit and filled with the heady aroma of various ingredients. 
			On a cluttered table, four small vials stand out, each containing a shimmering potion in the following colors: 
			red, purple, green, blue, and yellow, each promising their own unique magical effects."""
		self.name = 'alchemy'
	
	def enter(self, user, item_dict):
		self.enter_callback()
		while True:
			choice = input(">").lower()
			i = 0
			if 'q' in choice:
				print('quiting from alchemy room')
				exit(0)
			elif 'take' in choice:
				print(self.inventory)	
				for item in choice.split():
					print(i, item)
					if item in self.inventory:
						user.take(item, item_dict, self)
						break
					elif f"{item} potion" in self.inventory:
						user.take(f"{item} potion", item_dict, self)
						break
				else:
					print("item not found in in the alchemy room")
					i += 1
				#APPARENTLY!!!!! If you want to run the for loop and then 
				#have something happen if the loop is never broken, you
				#add a 'break' command within the if statement within the 
				#for loop, and then put an else statement ALIGNED WITH THE
				#'for' instead instead of aligned with 'if' and 'elif' 
				#which is nested under the for loop. 	
					
					
						
				
				#if 'blue' in choice:
				#	user.take("blue potion", item_dict, self)
			elif 'drink' in choice:
				#if 'blue' in choice:
				#	if 'blue potion' in user.inventory:
				#		return item_dict.get('blue potion').drink()
				#	else:
				#		print("You have to take the blue potion first")
				
				for item in choice.split():	
					print(i, item)
					if f"{item} potion" in user.inventory:
						return item_dict.get(f"{item} potion").drink(user, self)
					i = i +1
				else:
					print("You can't drink that.  Did you take it first?")
					
					
			elif 'open' in choice:
				if "chest" in user.inventory:
					item_dict.get("chest").open(user)
				else:
					print("Open the what now?")
			elif 'inventory' in choice:
				user.check_inventory()
			elif "leave" in choice or "back" in choice:
				return 'entryway'
			else:
				user.troll()
				
				

		


class Enchanting(Room):
	
	def __init__(self):
		super(Enchanting, self).__init__([
		"knife", "glowing stone", "sword", "key" 
		])
		self.desc = """
		This is a magical room, with a glowing stone, a knife, 
		a sword and a key.
		"""
		self.name = 'enchanting'
	
	def enter(self, user, item_dict):
		self.enter_callback()

		while True:
			choice = input(">").lower()
			#stone_bool = "glowing" in choice or "stone" in choice and "glowing stone" in self.inventory
			i = 0
			if 'take' in choice:
				print(self.inventory)	
				if "stone" in choice:
					user.take("glowing stone", item_dict, self)
				else:
					for item in choice.split():
						print(i, item)
						if item in self.inventory:
							user.take(item, item_dict, self)
							break
						elif f"{item} potion" in self.inventory:
							user.take(f"{item} potion", item_dict, self)
							break
					else:
						print("Not found.  Did you take it already?")
						i += 1		
			elif "leave" in choice or "back" in choice:
				return 'entryway'		
			elif "inventory" in choice:
				user.check_inventory()					
			elif 'q' in choice:
				print('quiting from enchanting room')
				exit(0)
			elif "look around" in choice:
				self.look_around()				
			else:
				user.troll()


class Entryway(Room):
	
	def __init__(self):
		super(Entryway, self).__init__(["bag"])
		self.desc = """
			In front of you, you see:
			A wooden door straight ahead
			A staircse going up
			A staircase going down
			"""
		self.name = 'entryway'
		
	def enter(self, user, item_dict):

		self.enter_callback()
		while True:
			choice = input("> ").lower()
			if "straight" in choice or "door" in choice:
				return "alchemy"
			elif 'take' in choice:
				print(self.inventory)	
				if "stone" in choice:
					user.take("glowing stone", item_dict, self)
				else:
					for item in choice.split():
						print(i, item)
						if item in self.inventory:
							user.take(item, item_dict, self)
							break
						elif f"{item} potion" in self.inventory:
							user.take(f"{item} potion", item_dict, self)
							break
					else:
						print("Not found.")
			elif "up" in choice:
				return "enchanting"
			elif "down" in choice:
				return "basement"
			elif "q" in choice or "leave" in choice:
				print("quitting from the entryway")
				exit(0)
			elif 'inventory' in choice:
				user.check_inventory()
			else:
				user.troll()

class Basement(Room):
	def __init__(self):
		super(Basement, self).__init__(["paper"])
		self.desc = """
			The basement is very steriotypical. It's damp, with dripping pipes 
			in the ceiling, and you see a peice of paper on top of a 
			few barrels of god knows what.
			"""

		self.name = 'basement'
		
	def enter(self, user, item_dict):
		self.enter_callback()
		i = 0
		while True:
			choice = input(">").lower()
			if "inventory" in choice:
				user.check_inventory()		
			elif 'take' in choice:
				print(self.inventory)	
				if "stone" in choice:
					user.take("glowing stone", item_dict, self)
				else:
					for item in choice.split():
						print(i, item)
						if item in self.inventory:
							user.take(item, item_dict, self)
							break
						elif f"{item} potion" in self.inventory:
							user.take(f"{item} potion", item_dict, self)
							break
					else:
						print("Not found.  Did you take that already?")	
			elif "leave" in choice or "back" in choice:
				return 'entryway'			
			elif'q' in choice:
				print('quiting from the basement')
				exit(0)
			elif 'name' in choice:
				print(f"Your name is: {user.name}")
			else:
				user.troll()


	
if __name__ == "__main__":

	Alchemy().check_inventory()
	Basement().check_inventory()
	Entryway().check_inventory()
	Enchanting().check_inventory()

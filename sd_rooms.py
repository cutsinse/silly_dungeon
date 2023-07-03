#This is the module that holds all the room classes

from sys import exit
from textwrap import dedent

from sd_items import *

class Room(object):

	def __init__(self, items):
		self.inventory = items
		
		#inventories are simple lists of strings, which match the 
		#keys of the all_items dictionary in sd_items.py. Then you use the 
		#.get() to get and use the item functions, such as:
			#item_dict.get(f"{item} potion").drink(user, self)
			
		#I did it this way because moving strings around to different lists
		#is a LOT simpler than moving the item objects themselves.
		
		self.exit = "entryway"
		self.up = "entryway"
		self.down = "entryway"
		self.straight = "entryway"
		
		#sets the default exits to entryway, which is true for almost all
		#rooms in the first dungeon layout. 
			#not all rooms have more than one exit.  setting all the 
			#possible exit defaults prevents the game crashing if the 
			#user tries to leave a room incorrectly, such as typing 
			#"up" in the enchanting room, which has no up exit. 
			#not a perfect solution, it adds some logical errors to the game, 
			#but it prevents it from crashing so I'm rolling with it for now. 
		
		#each room that is subclassed can override this, as well as add 
		#other exits, like the north exit or the south exit. 

		
	def enter_callback(self):
		print(f"You are in the {self.name.capitalize()} Room. \n", dedent(self.desc))
		print("What will you do now?")
	
	def look_around(self):
		print(dedent(self.desc))
	
	def check_inventory(self):
		print(self.inventory)
		#very similar to the user class version, but this prints the 
		#rooms inventory
	
	def help(self):
		#commands the user can use when playing, to be used if the 
		#player gets stuck. 
		
		print(dedent("""
		Command:  what it does. 
		
		look: see the room's current inventory
		
		look around: re-print the room's description
		
		look at: look at a specific item
		
		leave: leaves using the most obvious exit
		
		inventory: check the player's current inventory
		
		take: take an item from the room
		
		drink: drink a specific item (item must first be taken)
		
		read: read a specific item (item must first be taken)
		
		open: open a specific item (item must be in player's inventory)
		
		help: prints this list
		
		q:  quit the game
		
		
		What will you do now?
		"""))

	
	
#enter() is the primary game loop that the player will be interacting
		#with.  If you want the user to type something and then have something 
		#happen, this is the function to do make it happen.
		
		#Also note, there are several pieces of code that are commented out, 
		#most of these I put in for testing purposes, and can be 
		#uncommented for further testing. 
		
		#The main way the user input is processed is with simple 
			#if "x" in choice:  statements. 
			#with some f strings to help deal with 2 word item keys 
				#such as "red potion" or "glowing stone"
		#However, when working with both user and room inventories, a 
		#for loop is used to compare the input to the lists.  
			
		
	def enter(self, user, item_dict):
		#passing in the user and item_dict instances each time 
		#helps keep everything consistent.
		i = 0
		self.enter_callback()
		while True:
			choice = input(">").lower()
			#i = 0
			if 'q' in choice:
				print(f'quiting from the {self.name.capitalize()} Room')
				exit(0)
			
			elif 'take' in choice or "pick up" in choice:
				#print(self.inventory)	
				for item in choice.split():
					#print(i, item)
					if item in self.inventory:
						user.take(item, item_dict, self)
												
						#self = current room in the take function.  passing
						#the room instance allows changes to the room's 
						#inventory to be saved and remain the same as the 
						#user keeps playing. 
						
						print("taken")
						break
					elif f"glowing {item}" in self.inventory or f'{item} stone' in self.inventory:
						user.take("glowing stone", item_dict, self)
						print("taken")
						break
					elif f"{item} potion" in self.inventory:
						user.take(f"{item} potion", item_dict, self)
						print("taken")
						break
					
				else:
					print(f"item not found in in the {self.name.capitalize()} Room")
					#i += 1
				#APPARENTLY!!!!! If you want to run the for loop and then 
				#have something happen if the loop is never broken, you
				#add a 'break' command within the if statement within the 
				#for loop, and then put an else statement ALIGNED WITH THE
				#'for' instead instead of aligned with 'if' and 'elif' 
				#which is nested under the for loop. 	

			elif 'drink' in choice:							
				for item in choice.split():	
					#print(i, item)
					if f"{item} potion" in user.inventory:
						return item_dict.get(f"{item} potion").drink(user, self)
					#i = i +1
				else:
					print("You can't do that yet.")
					
			
			elif "help" in choice or "h" == choice:
				self.help()	
			elif "straight" in choice or "door" in choice:
				return self.straight
			elif "up" in choice:
				return self.up
			elif "down" in choice:
				return self.down			
			
			elif 'open' in choice:				
				if "chest" in user.inventory:
					item_dict.get("chest").open(user)
				else:
					print("Open the what now?")
			
			elif "read" in choice: 
				if "paper" in user.inventory:
					item_dict.get("paper").read()
				else:
					print("Read what?")
			elif 'inventory' in choice:
				user.check_inventory()

			elif "look" in choice:
				if "around" in choice:
					self.look_around()
				elif "at" in choice:
					#i = 0
					for item in choice.split():
						#print(i, item)
						if item in self.inventory:
							item_dict.get(item).look_at()
							#i =+ 1
							break
						elif f"glowing {item}" in self.inventory or f'{item} stone' in self.inventory:
							item_dict.get("glowing stone").look_at()
							break
						elif f"{item} potion" in self.inventory:
							item_dict.get(f'{item} potion').look_at()
							break
					else:
						print("Look at what?")
				else:
					self.check_inventory()
						
					
			
			elif "leave" in choice or "back" in choice:
				return self.exit			
			else:
				user.troll()
				i += 1
				if i > 7:
					print('Type "help" to see the different commands')
				

		
	
	
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
		self.down = 'entryway'
		
		



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
		self.up = 'enchanting'
		self.down = 'basement'
		self.straight = 'alchemy'
		self.exit = 'q'
		


class Basement(Room):	
	def __init__(self):
		super(Basement, self).__init__(["paper"])
		self.desc = """
			The basement is very steriotypical. It's damp, with dripping pipes 
			in the ceiling, and you see a peice of paper on top of a 
			few barrels of god knows what.
			"""

		self.name = 'basement'
		self.up = 'entryway'



	
if __name__ == "__main__":

	basement = Basement()
	print(basement.name)
	print(basement.inventory)
	print(basement.exit)
	print(isinstance(basement, Room))

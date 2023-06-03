#the module is all about inventories and items. 

from sys import exit
from textwrap import dedent


class Item(object):
	def __init__(self, name, desc):
		self.name = name
		self.desc = desc
		self.taken = False
	
	def kill(self):
		print(self.kill_desc)
		exit(0)
	
	def look_at(self):
		print(dedent(self.desc))


class Paper(Item): 
	def __init__(self, name, desc, contents):
	#contents = what's written on the paper
	#desc = description of the paper itself. 
		super(Paper, self).__init__(name, desc)
		self.contents = contents
	def read(self):
		print(dedent(self.contents))

class Chest(Item):
	def __init__(self):
		super(Chest, self).__init__('Treasure Chest', """
		A large chest with a lock on it.
		""")
	def open(self, user_inventory):
		pass
		#use "isinstance() functoin?
		
		

class Potion(Item):
	def __init__(self, name, desc):
		super(Potion, self).__init__(name, desc)
		self.teleport_target = None
	
	def set_teleport_target(self, target):
		self.teleport_target = target
		
	def drink(self):
		return self.teleport_target


class Red(Potion):
	def __init__(self):
		super(Red, self).__init__('red potion', """
		A swirling, blood red potion.  
		It almost seems alive.
		""")
		self.kill_desc = "AAAAAAAAAH"
		
	def drink(self):
		self.kill()

class Blue(Potion):
	def __init__(self):
		super(Blue, self).__init__('blue potion', """
		The bottle is glass, but shaped like a stone. 
		The deep blue is almost...glowing?
		""")
		
class Purple(Potion):
	def __init__(self):
		super(Purple, self).__init__('purple potion', """
		The bottle is very dusty, with a rich, deep purple color.
		""")
		


class Green(Potion):
	def __init__(self):
		super(Green, self).__init__('green potion', """
		This potion glows a dappled green color. 
		Much like the forest outside.
		""")

class Yellow(Potion):
	def __init__(self):
		super(Yellow, self).__init__('yellow potion', """
		The brightest of all the potions, it almost glitters like...
		gold? 
		""")
	
	def drink(self, user_inventory):
		pass


		
if __name__ == "__main__":
	#print("Testing Testing!!!\n\n")
	r = Red()
	#g = Green()
	#b = Blue()
	#bag = Item('bag of holding', 'this is a test item')
	print("Red taken: ", r.taken)
	#print("Green taken: ", g.taken)
	#print("Blue taken: ", b.taken)
	#print("Bag taken: ", bag.taken)
	#r.drink()

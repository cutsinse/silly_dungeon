#the module is all about inventories and items. 

from sys import exit
from textwrap import dedent

#Base class for all of the objects.  Also used to make simple objects 
	#that don't do anything
class Item(object):
	def __init__(self, name, desc):
		self.name = name
		self.desc = desc
		self.taken = False
	
	#cannot be used with simple objects
			#must be subclassed in order to use. 
	def kill(self):
		print(self.kill_desc)
		exit(0)
	
	def look_at(self):
		print(dedent(self.desc))


class Paper(Item): 
	def __init__(self, name, desc, contents):
	#contents = what's written on the paper
	#desc = description of the paper itself. (ex: "It's a crumpled note")
		super(Paper, self).__init__(name, desc)
		self.contents = contents
		
	def read(self):
		print(dedent(self.contents))

class Chest(Item):
	def __init__(self):
		super(Chest, self).__init__('chest', """
		A small chest with a lock on it.
		""")
		
	def open(self, user):
		if "key" in user.inventory:
			print(dedent("""
			Congratulations!!! You found the gold and won the game!!!!
			"""))
			exit(0)
		else: 
			print("You need a key to do that")
		
		

class Potion(Item):
	def __init__(self, name, desc):
		super(Potion, self).__init__(name, desc)
		#self.teleport_target = None
			#every potion sets their own teleport_target
			#I left this here in case anyone wants to set a default
			#teleport target for all potions. 
	
	#def set_teleport_target(self, target):
		#self.teleport_target = target
		#ended up not needing this function, but saving just in case. 
		
	def drink(self, user, room):
		#This is the default option for drinking a potion, 
		print("""\n***As the potion is consumed, you are engulfed in a swirling vortex of color and sensation!***\n""")
		return self.teleport_target
					
		#drink() can and should be overriden for potions that do
			#something different, like the red and yellow potions
			
		#The default version of drink() doesn't need the user argument, 
			#but it is needed when you override it in a subclass, 
			#like the yellow potion (see below)

class Red(Potion):
	def __init__(self):
		super(Red, self).__init__('red potion', """
		A swirling, blood red potion.  
		It almost seems alive.
		""")
		self.kill_desc = "AAAAAAAAAH"
		
	def drink(self, user, room):
		self.kill()

class Blue(Potion):
	def __init__(self):
		super(Blue, self).__init__('blue potion', """
		The bottle is glass, but shaped like a stone. 
		The deep blue is almost...glowing?
		""")
		self.teleport_target = "enchanting"
		
class Purple(Potion):
	def __init__(self):
		super(Purple, self).__init__('purple potion', """
		The bottle is very dusty, with a rich, deep purple color.
		""")
		self.teleport_target = "basement"


class Green(Potion):
	def __init__(self):
		super(Green, self).__init__('green potion', """
		This potion glows a dappled green color. 
		Much like the forest outside.
		""")
		self.teleport_target = "entryway"

class Yellow(Potion):
	def __init__(self):
		super(Yellow, self).__init__('yellow potion', """
		The brightest of all the potions, it almost glitters like...
		gold? 
		""")
	
	def drink(self, user, room):
		print(dedent("""
		You drank the yellow potion! A poof of a yellow cloud and 
		the bottle turns into a small treasure chest!
		"""))
		user.inventory.append("chest")
		print("added chest")
		user.inventory.remove("yellow potion")
		print("removed yellow potion\n")
		return room.name
		
		#drinking the yellow potion perminantly removes it from the game
			#but still has some hiccups I haven't quite figured out. 
			#For example, the entire room description is written again, 
			#which is a bit akward and makes it harder to see what the 
			#yellow potion did. 
			#however, it's the only way to loop back to the room's enter() 
			#function that I've been able to figure out so the user 
			#can continue playing properly. 
			
		#The yellow potion is also not removed from the description, 
			#which is also confusing. 
				
				
		

#I made this a class instead of a global variable so that you can quickly
	#and easily create one instance of everything, so that the object 
	#attributes can be changed and then remain consistent.
	#such as the "taken" attribute, which can be changed from False to True
	
class IEngine():
	all_items = {
	"red potion": Red(), "blue potion": Blue(),
	"green potion": Green(), "purple potion": Purple(), 
	"yellow potion": Yellow(),
	"paper":Paper('paper', """
	It's rolled up, but very loosely.
	Doesn't look like anyone cared about it much 
	""", 
	"""
	red = poison 
	blue = enchanting room 
	green = entrance 
	purple = basement 
	yellow = chest
	bottomless bottles!
	"""), "bag": Item('bag of holding', 'this is a test item'),
	"key": Item('key', 'A shiny, gold key, with no markings on it.'),
	"sword": Item('sword', 'It is a simple, but effective, sword'),
	"glowing stone": Item('glowing stone', "It's a stone....that glows!!"),
	"knife": Item('knife', """
	It looks like a utility knife, used for cutting leather or the like
	"""),
	"chest": Chest()
	} 
	
	


		
if __name__ == "__main__":
	pass
	#Testing area

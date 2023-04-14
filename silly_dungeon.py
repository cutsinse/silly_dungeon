#Exercise 36: Silly Dungeon
#This program takes the user through a series a series of rooms, lets the user look around, take items, and drink potions
#This program uses while loops in order to allow the user to input multiple times in the same room
#The goal is to find and take the key, then find and open the treasure chest with the key.

from sys import exit
#need this for the exit(0) command, which allows me to end the program at any point, within any function or loop

inventory = ["test item 1"] #global variable
#use the command "global" to access this list within a function

def taken():
    """Used when the user had already taken an item """
    print("You already took that.")
def blank():
    """Used when the user tries to take something not from the list or that they cannot take"""
    print("That's not here")
def troll():
    """Used when the user types something in the program can't do anything with"""
    print("I don't understand")

def alchemy_room():
    print("You are in the alchemy room.")

def enchanting_room():
    enchanting_description = """You are in the enchanting room!
    This is a magical room, with glowing stones, knives, swords and a key.
    What do you want to do?"""

    print(enchanting_description)
    #defining the enchanting_description makes it easier to type later in the code.
    #used to make the look command easier to code and understand.

    while True:
        #a while loop is used so the user can do multiple inputs, as many as they like
        #until another "action" is taken (such as take, look, or leave)
        global inventory
        choice = input(">").split(" ")
        #the "choice" variable is consistently used in this program to refer to whatever the user types if __name__ == '__main__':
        #Typically commands like take or look or leave
        if "take" in choice:
            #nested additional if staments so the program can skip checking for the rest of the items
            #this is also easier to type up the code and easier to read.
            if "stone" in choice or "stones" in choice:
                #note, the repitition of "in choice" here is not optional.
                #the computer gets confused and returns "true" if you do
                #if "stone" or "stones" in choice
                #I don't fully understand why just yet, but it basically is "truthy" because it returns a non-blank string
                if "glowing stones" in inventory:
                    taken()
                    #This if statement is needed so the user can't take more than one of each item
                else:
                    inventory.append("glowing stones")
                    print("stones added to your inventory")
                    print(inventory)
            elif "knife" in choice or "knives" in choice:
                if "knife" in inventory:
                    taken()
                else:
                    inventory.append("knife")
                    print("Adding a knife to your inventory")
                    print(inventory)
            elif "key" in choice:
                if "key" in inventory:
                    taken()
                else:
                    inventory.append("key")
                    print("Adding the key to your inventory")
                    print(inventory)
            elif "sword" in choice or "swords" in choice:
                if "sword" in inventory:
                    taken()
                else:
                    inventory.append("sword")
                    print("Adding a knife to your inventory")
                    print(inventory)
            else:
                blank()
        elif "look" in choice:
            print(enchanting_description)
        elif "inventory" in choice:
            print(inventory)
        elif "leave" in choice or "exit" in choice or "back" in choice:
            break
            #the break command breaks the while True loop, and goes to the next line in the function
            #or, to the next line after the function is finished running
        elif "quit" in choice:
            exit(0)
            #more for the developer, a way to quit from this room instead of leaving twice
            #I tried using "force quit" here, but because of the .split function in choice,
            #it didn't see a single list item called "force quit" and so returned False
            #I could use the the "and" operator to search for both, but this is just simpler
        else:
            troll()
    enter()
    #Since there is no where else to go from the enchanting_room, the user can only return to the entrance.

def basement():
    print("You are in the basement.")
    base_desc = """The basement is very steriotypical. It's damp, with dripping pipes in the ceiling,
    and you see a peice of paper on top of a few barrels of god knows what."""
    print("What do you do?")

    while True:
        global inventory
        choice = input(">").split(" ")
        if "take" in choice:
            if "paper" in choice or "note" in choice:
                if "note" in inventory:
                    taken()
                    #still to be implimented, a way to read this # NOTE:
                    #This note will eventually contain the key to what each potion does in the alchemy room
                else:
                    inventory.append("note")
                    print("Adding the note to your inventory")
                    print(inventory)
            if "barrel" in choice:
                print("You can't take that.")
            else:
                blank()
        elif "leave" in choice or "exit" in choice or "back" in choice:
            break
        elif "quit" in choice:
            exit(0)
        else:
            troll()
    enter()
    #There is no where else to go from the basement.

def enter():
    print("You see before you 3 options.")
    print("1: A wooden door straight ahead")
    print("2: A staircse going up")
    print("3: A staircase going down")
    print("4: Check inventory")
    while True:
        choice = input(">").split(" ")
        if "1" in choice or "door" in choice:
                alchemy_room()
        elif "2" in choice or "up" in choice:
            enchanting_room()
        elif "3" in choice or "down" in choice:
            basement()
        elif "4" in choice or "check" in choice or "inventory" in choice:
            global inventory
            print(inventory)
        elif "leave" in choice or "exit" in choice:
            print("Ok, bye!")
            exit(0)
        else:
            print("\nI'm sorry, I don't understand.")

#Program flow starts here.

enter()

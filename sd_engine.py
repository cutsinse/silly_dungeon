#This will hold other random functions that are needed separately
#in the main game file. 

from sys import exit
from textwrap import dedent

from  sd_user import *
from sd_rooms import *
from sd_items import *


def items_dict(room_variable):
	room_placeholder = room_variable
	str_dict = {}
	for item in room_placeholder.inventory:
		str_dict[item.name] = item
	return str_dict


import random, math ,os ,termios ,time, multiprocessing, threading
from typing import List

class Item:
	"""name:str
	type:str
	health:int"""
	def __init__(self, name:str, type:str, health:int):
		self.name = name
		self.type = type
		self.health = health
	name:str
	type:str
	health:int

class Monster:
	"""name:str
	health:int
	damage:int
	lootrarity:int
	loot:list[Item]"""
	def __init__(self, name, health, damage, lootrarity = 0, loot:List[Item] = []):
		self.name = name
		self.health = health
		self.damage = damage
		self.lootrarity = lootrarity
		self.loot = loot
	name:str
	health:int
	damage:int
	lootrarity:int
	loot:List[Item]

class Moves:
	"""north: List[True/False(bool),destination(str)]
	south :List[True/False(bool),destination(str)]
	east: List[True/False(bool),destination(str)]
	west: List[True/False(bool),destination(str)]"""
	def __init__(self,north,south,east,west):
		self.north = north
		self.south = south
		self.east = east
		self.west = west
	north:List[str]
	south:List[str]
	east:List[str]
	west:List[str]

def pprint(text):
	"""prints green text"""
	print('\x1b[6;30;42m' + text + '\x1b[0m')
def getAction(l, zerooption = True):
	"""gets desired options for X action"""
	if zerooption:
		pprint("0: return")
	for i,action in enumerate(l):
		pprint(f'{i+1}: {action}')
	while True:
		try:
			v = int(input("What do you want: "))
			if zerooption and v == 0:
				return None
			elif v > 0 and v <= len(l):
				return l[v-1]
		except:
			pass
		pprint("nope")

def inventoryCount(type = None):
	"""counts inventory len returns len of filtered type"""
	global invin
	if type == None:
		return len(invin)
	return len(filter(lambda item: item.type == type, invin))

def pickItem(type = None):
	"""has user pick from inventory"""
	global invin
	l = invin
	if type != None:
		l = filter(lambda item: item.type == type, l)
	pprint("0: return")
	for x in filter(lambda item: item.type == "all", l):
		l.append(x)
	for i,item in enumerate(l):
		pprint(f'{i+1}: {item.name}')
	while True:
		try:
			v = int(input("What do you want to use: "))
			if v == 0:
				return None
			elif v > 0 and v <= len(l):
				ret = l(v-1)
				invin.remove(ret)
				return ret
		except:
			pass
damageNegative=1

def applyItem(item: Item, monster: Monster):
	"""apply the item effect(s)"""
	global health
	global damageNegative
	if item.type == "RPG":
		monster.health = max(monster.health-20, 0)
	elif item.type == "holy hand grenade":
		print("""


 0 
 |/
 |
/ \\
""")
		for x in range(100):
			print()
		time.sleep(.01)
		print("""


 0      
 |/
 |
/ \\
""")
		for x in range(100):
			print()
		time.sleep(.01)
		print("""


 0              
 |/
 |
/ \\
""")
		for x in range(100):
			print()
		time.sleep(.01)
		print("""


 0                      
 |/
 |
/ \\
""")
		for x in range(100):
			print()
		time.sleep(.01)
		print("""


 0                               
 |/
 |
/ \\
""")
		for x in range(100):
			print()
		time.sleep(.01)
		print("""


 0                                      
 |/
 |
/ \\
""")
		for x in range(100):
			print()
		time.sleep(.01)
		print("""


 0                                                 
 |/
 |
/ \\
""")
		for x in range(100):
			print()
		time.sleep(.01)
		print("""


 0                                                                           
 |/
 |
/ \\
""")
		for x in range(100):
			print()
		time.sleep(.01)
		print("""


 0                                                                                                                    
 |/
 |
/ \\
""")
		for x in range(100):
			print()
			time.sleep(.01)
		print("""


 0                                                                                                  BOOM              "''"'"
 |/                                                                                                                ""'000000
 |                                                                                                                  ""'"0000
/ \\                                                                                                                  '""'"0
""")
		monster.health = 0
	elif item.type == "health potion +5":
		health += 5
	elif item.type == "health potion +10":
		health += 10
	elif item.type == "health potion +20":
		health += 10
	elif item.type == "health potion +25":
		health += 10
	elif item.type == "health potion +50":
		health += 10
	elif item.type == "health potion +75":
		health += 10
	elif item.type == "health potion +100":
		health += 10
	elif item.type ==  "deodorant":
		if monster.name== "shrek":
			print('"I love Shrek, so I ordered the DVD and ate it. It tasted terrible and it hurt really bad going down. And when I finally had the relief of it leaving I had some insane diarrhea. Not recommended and shrek was to hot to handle and thicc daddy shrek need to be thicc 3 no golira or moncey we want funny monce shrek hot monke funne" exact movie revue quote')
			monster.health = 0
	elif item.type == "15 foot long pole":
		damageNegative-=15
	elif item.type == "nuke":
		inp = input("conferm (this will also kill you the monster and the world) (y/n):")
		if inp == "y":
			pprint("all dead")
			pprint("gameover")
			health=0
			monster.health = 0
	else:
		print(f" error with apply item got Item:{item} monster:{monster}")
		
			

good = ['holy hand grenade one use insta kill','rpg once per battle 20 damage at begining','heth + 50 potion','Sten MK II tends to misfire sometimes has buletts bounce off of tagert +20% damage','Apache Revolver you can use it like a gun (terible aim) a nife (way to flexible) or a iron fist (the only safe way to use it) +30% damage','pickled lepercon head +1 luck for 7 turns','luck potion +1 luck for 2 turns']
norm = ["nuke (you cant use it cuse it will kill evorything and evoryone including you)","stick + 3% damage",'helth + 10 porion','deodorant (shreck wants it)','luck charm +1 luck for a turn','luck potion +1 luck for 2 turns']
rearer = ['a peace of a lemon','sord + 10% damage','helth + 20 prtion','slingshot +5% damage','a 15 foot long pole','clover +1 luck for 3 turns','luck potion +1 luck for 4 turns']

def max(a,b):
	"""returns bigger number"""
	if a > b:
		return a
	return b
def getloot(rearity):
	"""returns loot"""


invin=[Item("health +20 potion", 20,"anywhere")]

maps ={
	"grail":{"name": "grail",
	"lootrearity": -100,
	"movment": {"direction":None, "north": None, "south": None, "east": None, "west": None},
	"monster": None},

	"boss":{"name": "gliched cididel",
	"lootrearity": None,
	"movment": {"direction":None, "north": None, "south": None, "east": None, "west": "grail"},
	"monster": Monster("programer", 1000, 50)},

	"glichedplains2":{"name": "gliched plains",
	"loorearityt": 2,
	"movment": {"direction":"west" "south", "north": None, "south": "glichedplains1", "east": None, "west": "boss"},
	"monster": Monster("robot", 300, 50, 3)},

	"glichedplains1":{"name": "gliched plains",
	"loorearityt": 3,
	"movment": {"direction":"north" "east", "north": "glichedplains2", "south": None, "east": "mouantan5", "west": None},
	"monster": Monster("robot", 250, 45, 3)},

	"mountan5":{"name": "mounatn",
	"loorearityt": 3,
	"movment": {"direction":"west" "east", "north": None, "south": None, "east": "mountan4", "west": "glichedplains1"},
	"monster": Monster("robot", 200, 25, 2)},

	"mountan4":{"name": "mountan",
	"loorearityt": 2,
	"movment": {"direction":"west" "east", "north": None, "south": None, "east": "mountan3", "west": "mountan5"},
	"monster": None},

	"mountan3":{
		"name": "mountan",
		"loorearityt": 3,
		"movment": {"direction":"east" "west", "north": None, "south": None, "east": "mountan2", "west": "mountan4"},
		"monster": Monster("dragon", 100, 50, 3)
	},

	"mountan2":{"name": "mountan",
	"loorearityt": 3,
	"movment": {"direction":"west" "east", "north": None, "south": None, "east": None, "west": None},
	"monster": None},
	
	"mountan1":{"name": "mountan",
	"loorearityt": 3,
	"movment": {"direction":"north" "south", "north": None, "south": None, "east": None, "west": None},
	"monster": None},

	"swamp3":{"name": "swamp",
	"loorearityt": 2,
	"movment": {"direction":"north" "south", "north": None, "south": None, "east": None, "west": None},
	"monster": Monster("shreck", 300, 5, 3)},

	"swamp2":{"name": "swamp",
	"loorearityt": 2,
	"movment": {"direction":"east" "south", "north": None, "south": None, "east": None, "west": None},
	"monster": None},

	"swamp1":{"name": "swamp",
	"loorearityt": 3,
	"movment": {"direction":"west" "north", "north": None, "south": None, "east": None, "west": None},
	"monster": None},

	"viliage":{"name": "french castle (how did you get in here anyway)",
	"loorearityt": 7298047590287387642980743508,
	"movment": {"direction":"west" "south", "north": None, "south": None, "east": None, "west": None},
	"monster": Monster("napolean", 300000000, 50000000, 3719875493876904187549473295)},

	"forest":{"name": "forest",
	"loorearityt": 3,
	"movment": {"direction":"north" "south", "north": None, "south": None, "east": None, "west": None},
	"monster": Monster("killer bunny", 15, 10, 3)},

	"foothills3":{"name": "foot hills",
	"loorearityt": 2,
	"movment": {"direction":"west" "east", "north": None, "south": None, "east": None, "west": None},
	"monster": None},

	"foothills2":{"name": "foot hills",
	"loorearityt": 2,
	"movment": {"direction":"east" "south", "north": None, "south": None, "east": None, "west": None},
	"monster": None},

	"foothills1":{"name": "foot hills",
	"loorearityt": 3,
	"movment": {"direction":"west" "north" "east" "south", "north": None, "south": None, "east": None, "west": None},
	"monster": None},

	"field6":{"name": "field",
	"loorearityt": 2,
	"movment": {"direction":"west" "east", "north": None, "south": None, "east": None, "west": None},
	"monster": None},

	"field5":{"name": "field",
	"loorearityt": 2,
	"movment": {"direction":"west" "east", "north": None, "south": None, "east": None, "west": None},
	"monster": Monster("flying snake", 50, 10, 2)},

	"field4":{"name": "field",
	"loorearityt": 1,
	"movment": {"direction":"south", "north": None, "south": None, "east": None, "west": None},
	"monster": None},

	"field3":{"name": "field",
	"loorearityt": 2,
	"movment": {"direction":"east" "north", "north": None, "south": None, "east": None, "west": None},
	"monster": None},

	"field2":{"name": "field",
	"loorearityt": 1,
	"movment": {"direction":"west" "east", "north": None, "south": None, "east": None, "west": None},
	"monster": None},

	"field1":{"name": "field",
	"loorearityt": 2,
	"movment": {"direction":"north" , "north": None, "south": None, "east": None, "west": None},
	"monster": Monster("robot", 300, 50, 3)}
}
	
# player stats
damageBuff = 1
health = 100
damageBeforeBattle = 0
location = "field4"
luck = 0

while True:
	currentLocation = maps[location]
	if currentLocation["monster"] != None:
		monster = currentLocation["monster"]
		while monster["health"] > 0 and health > 0:
			actions = ["attack monster"]
			if inventoryCount("combat") > 0:
				actions.append("use item")
			choice = getAction(actions, False)
			if choice == "attack monster":
				damage = random.randint(10, 20) * damageBuff
				monster["health"] = max(monster["health"]-damage,0)
			elif choice == "use item":
				item, i = pickItem("combat")
				if item != None:
					continue
				else:
					applyItem(item,monster)
					
					
			
		pprint(f'{monster["name"]} defeated')
		if monster["loot"] != None:
			loot = monster["loot"]
			invin.append(loot)
			pprint(f'{monster["name"]} dropped {loot["name"]}. Its in your inventory')
		currentLocation["monster"] = None


				

				
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class tom:
	def __init__(self):
		pass





















































































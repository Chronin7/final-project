import random, math

def getAction(l, zerooption = True):
	if zerooption:
		print("0: return")
	for i,action in enumerate(l):
		print(f'{i+1}: {action}')
	while True:
		try:
			v = int(input("What do you want: "))
			if zerooption and v == 0:
				return None
			elif v > 0 and v <= len(l):
				return l[v-1]
		except:
			pass
		print("nope")

def inventoryCount(type = None):
	global invin
	if type == None:
		return len(invin)
	return len(filter(lambda item: item["type"] == type, invin))

def pickItem(type = None):
	global invin
	l = invin
	if type != None:
		l = filter(lambda item: item["type"] == type, l)
	print("0: return")
	for i,item in enumerate(l):
		print(f'{i+1}: {item["name"]}')
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


def applyItem(item, monster):
	global health
	match item["name"]:
		case "RPG":
			monster["health"] = max(monster["health"]-20, 0)
		case "holy hand grenade":
			monster["health"] = 0
		case "health potion +5":
			health += 5
		case "health potion +10":
			health += 10
		case "health potion +20":
			health += 10
		case "health potion +25":
			health += 10
		case "health potion +50":
			health += 10
		case "health potion +75":
			health += 10
		case "health potion +100":
			health += 10
		case "deodorant":
			if monster["name"]== "shrek":
				monster["health"] = 0
		
			

good = ['holy hand gernade one use insta kill','rpg once per battle 20 damage at begining','heth + 50 potion','Sten MK II tends to misfire sometimes has buletts bounce off of tagert +20% damage','Apache Revolver you can use it like a gun (terible aim) a nife (way to flexible) or a iron fist (the only safe way to use it) +30% damage','pickled lepercon head +1 luck for 7 turns','luck potion +1 luck for 2 turns']
norm = ["nuke (you cant use it cuse it will kill evorything and evoryone including you)","stick + 3% damage",'helth + 10 porion','deodorant (shreck wants it)','luck charm +1 luck for a turn','luck potion +1 luck for 2 turns']
rearer = ['a peace of a lemon','sord + 10% damage','helth + 20 prtion','slingshot +5% damage','a 15 foot long pole','clover +1 luck for 3 turns','luck potion +1 luck for 4 turns']

def max(a,b):
	if a > b:
		return a
	return b


invin=[{"name":"health +20 potion","health": 20,"special": None}]
maps={
	"grail": {
		"loot": [
			{"name": "grail", "health": 0, "special": "win", "type": "other"}
		],
		"monster": None
	},
	"boss": {
		"loot": [],
		"monster": {"name": "programer", "health":10000, "attack": 72, "special": "boss", "loot":None },
		"moves": [
			{"direction": "east", "dest": "glitch2"},
			{"direction": "west", "dest": "grail"}
		]
	},
}

# player stats
damageBuff = 1
health = 100
damageBeforeBattle = 0
location = "boss"
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
					
					
			
		print(f'{monster["name"]} defeated')
		if monster["loot"] != None:
			loot = monster["loot"]
			invin.append(loot)
			print(f'{monster["name"]} dropped {loot["name"]}. Its in your inventory')
		currentLocation["monster"] = None


				

				


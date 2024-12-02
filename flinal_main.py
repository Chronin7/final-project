from final_ascii import *
import random
import time
def inputcorect():
	print("thats not a valid input ",end="")
	if random.randint(1,10):
		print("so a troll throws you into lava...")
		time.sleep(1)
		print("just kidding just please input a valid input")
	else:
		print()
def get(raeraty):
	if raeraty == 1:
		return "heath potion",5
	if raeraty == 2:
		return "heath potion",10
	if raeraty == 3:
		return "heath potion",20
	if raeraty == 4:
		return "heath potion",50
	if raeraty == 5:
		return "heath potion",100
exoshtion = 0
rations = 5
monkilled = False
pythonbridge = False
win = False
loot = [f"hp{20}"]
name = ""
playedmount = 0
coller = ""
def intro():
	gointor = 1
	while gointor != 1000:
		for x in range(random.randint(1,gointor)):
			print("  ",end="")
		print("x")
		time.sleep(random.uniform(0,3/gointor))
		gointor+=1
		questens()
def questens():
	global name
	global exoshtion
	global monkilled
	global rations
	global pythonbridge
	global win
	global loot
	global playedmount
	global coller
	name = input("whats your name adventurer (type your name then press enter to continue): ")
	coller = input(f"hello {name} whats your favorite color: ")
	print(f"""hello {name} who likes the color {coller}, your quest is to "find the holy grail" without reaching exhaustion level 5 good luck""")
def main():
	global name
	global exoshtion
	global monkilled
	global rations
	global pythonbridge
	global win
	global loot
	global playedmount
	global coller
	while True:
		try:
			action = int(input(f"""rations left: {rations}
exhaustion level: {exoshtion}
what would you like to do
1 to continue along path
2 to rest
3 to hunt for food
4 to check inventory: """))
			if action not in [1,2,3,4]:
				inputcorect()
			else:
				break
		except:
			inputcorect()
		if action == 1:
			rations-=1
			if rations <0:
				print("you starved to death and killer guinea pigs ate you")
				print("game over")
				break
			event = random.randint(1,3)
			if event == 3:
				eventtype = random.randint(1,4)
				if eventtype == 1:
					lose = random.randint(0,exoshtion-1)
					print(f"a blizzard comes thru and you gain {lose} exhaustion",end=" ")
					exoshtion -= lose
					lose = random.randint(0,rations-1)
					print(f"and blew {lose} rations away.")
					rations-=lose
				if eventtype == 2:
					print("a robber came and stol a ration")

	
import random
import time

oneone = "-"
twoone = "-"
threeone = "-"
onetwo = "-"
twotwo = "-"
threetwo = "-"
onethree = "-"
twothree = "-"
threethree = "-"
plays = []
posplay = ["1, 1","1, 2","1, 3","2, 1","2, 2","2, 3","3, 1","3, 2","3, 3"]

def makeboard():
	print("Here is the current board:")
	print(f"{oneone} {twoone} {threeone}")
	print(f"{onetwo} {twotwo} {threetwo}")
	print(f"{onethree} {twothree} {threethree}")

def getbestmove(player):
	global oneone
	global twoone
	global threeone
	global onetwo
	global twotwo
	global threetwo
	global onethree
	global twothree
	global threethree

	if oneone == twoone == player and threeone == "-":
		return "1, 3"
	elif onetwo == twotwo == player and threetwo == "-":
		return "2, 3"
	elif onethree == twothree == player and threethree == "-":
		return "3, 3"
	elif oneone == onetwo == player and onethree == "-":
		return "3, 1"
	elif twoone == twotwo == player and twothree == "-":
		return "3, 2"
	elif threeone == threetwo == player and threethree == "-":
		return "3, 3"
	elif threeone == twotwo == player and onethree == "-":
		return "3, 1"
	elif oneone == twotwo == player and threethree == "-":
		return "3, 3"
	#
	elif oneone == threeone == player and onetwo == "-":
		return "1, 2"
	elif onetwo == threetwo == player and twotwo == "-":
		return "2, 2"
	elif onethree == threethree == player and twothree == "-":
		return "3, 2"
	elif oneone == onethree == player and onetwo == "-":
		return "2, 1"
	elif twoone == twothree == player and twotwo == "-":
		return "3, 2"
	elif threeone == threethree == player  and threetwo == "-":
		return "2, 3"
	elif threeone == onethree == player and twotwo == "-":
		return "2, 2"
	elif oneone == threethree == player and twotwo == "-":
		return "2, 2"
	#
	elif twoone == threeone == player and oneone == "-":
		return "1, 1"
	elif twotwo == threetwo == player and onetwo == "-":
		return "2, 1"
	elif twothree == threethree == player and onethree == "-":
		return "2, 3"
	elif onetwo == onethree == player and oneone == "-":
		return "1, 1"
	elif twotwo == twothree == player and twoone == "-":
		return "1, 2"
	elif threetwo == threethree == player and threeone == "-":
		return "2, 3"
	elif twotwo == onethree == player and threeone == "-":
		return "1, 3"
	elif twotwo == threethree == player and oneone == "-":
		return "1, 1"
	else :
		return "re"
		





def checkW():
	global oneone
	global twoone
	global threeone
	global onetwo
	global twotwo
	global threetwo
	global onethree
	global twothree
	global threethree

	if oneone == twoone == threeone:
		if oneone != "-":
			print(f"{oneone} wins!")
			exit()
	if onetwo == twotwo == threetwo:
		if onetwo != "-":
			print(f"{onetwo} wins!")
			exit()
	if onethree == twothree == threethree:
		if onethree != "-":
			print(f"{onethree} wins!")
			exit()
	if oneone == onetwo == onethree:
		if oneone != "-":
			print(f"{oneone} wins!")
			exit()
	if twoone == twotwo == twothree:
		if twoone != "-":
			print(f"{twoone} wins!")
			exit()
	if threeone == threetwo == threethree:
		if threeone != "-":
			print(f"{threeone} wins!")
			exit()
	if threeone == twotwo == onethree:
		if threeone != "-":
			print(f"{threeone} wins!")
			exit()
	if oneone == twotwo == threethree:
		if oneone != "-":
			print(f"{oneone} wins!")
			exit()




def decode(pos, player):
	if pos == "1, 1":
		global oneone
		if oneone == "-":
			oneone = player
		else:
			print("Error: space not open")
			exit()
	elif pos == "1, 2":
		global twoone
		if twoone == "-":
			twoone = player
		else:
			print("Error: space not open")
			exit()
	elif pos == "1, 3":
		global threeone
		if threeone == "-":
			threeone = player
		else:
			print("Error: space not open")
			exit()
	elif pos == "2, 1":
		global onetwo
		if onetwo == "-":
			onetwo = player
		else:
			print("Error: space not open")
			exit()
	elif pos == "2, 2":
		global twotwo
		if twotwo == "-":
			twotwo = player
		else:
			print("Error: space not open")
			exit()
	elif pos == "2, 3":
		global threetwo
		if threetwo == "-":
			threetwo = player
		else:
			print("Error: space not open")
			exit()
	elif pos == "3, 1":
		global onethree
		if onethree == "-":
			onethree = player
		else:
			print("Error: space not open")
			exit()
	elif pos == "3, 2":
		global twothree
		if twothree == "-":
			twothree = player
		else:
			print("Error: space not open")
			exit()
	elif pos == "3, 3":
		global threethree
		if threethree == "-":
			threethree = player
		else:
			print("Error: space not open")
			exit()
	else:
		print("Error: move not accepted")
		exit()

	global plays
	global posplay
	plays.append(pos)
	vari = 0
	while not(posplay[vari] == pos):
		vari +=1
	posplay.pop(vari)


#
#
#
#
#
#

gmode = input("1 player (type 1). 2 player (type 2). ")

makeboard()
if gmode == "2":

	rpt = 0

	for loop in range(9):

		if rpt == 0:
			move = input("Player X, what is your move? ")
			decode(move, "X")

			rpt = 1
		else:

			move = input("Player O, what is your move? ")
			decode(move, "O")
			rpt = 0

		makeboard()
		checkW()
	
	
	
else :
	if random.randint(1,2) == 2:
		print("You are O")

		rpt = 0

		for loop in range(9):

			if rpt == 0:
				print("Tic tac bot is thinking...")
				time.sleep(0.6)
				move = getbestmove("X")
				if move == "re":
					move = getbestmove("O")
					if move == "re":
						move = posplay[random.randint(0,len(posplay)-1)]
				decode(move, "X")
				rpt = 1
			else:

				move = input("Player O, what is your move? ")
				decode(move, "O")
				
				rpt = 0
			makeboard()
			checkW()
	else :
		print("You are X")

		rpt = 0

		for loop in range(9):

			if rpt == 0:
				move = input("Player X, what is your move? ")
				decode(move, "X")
					
				rpt = 1
			else:
				print("Tic tac bot is thinking...")
				time.sleep(1)
				move = getbestmove("O")
				if move == "re":
					move = getbestmove("X")
					if move == "re":
						move = (str(random.randint(1,3))) + ", " + (str(random.randint(1,3)))
						if move in plays:
							while move in plays:
								move = (str(random.randint(1,3))) + ", " + (str(random.randint(1,3)))
				decode(move, "O")
				rpt = 0

				
			makeboard()
			checkW()
print("It's a draw!")
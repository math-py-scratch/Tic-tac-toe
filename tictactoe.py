oneone = "-"
twoone = "-"
threeone = "-"
onetwo = "-"
twotwo = "-"
threetwo = "-"
onethree = "-"
twothree = "-"
threethree = "-"

def makeboard():
	print("Here is the current board:")
	print(f"{oneone} {twoone} {threeone}")
	print(f"{onetwo} {twotwo} {threetwo}")
	print(f"{onethree} {twothree} {threethree}")

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



#
#
#
#
#
#



makeboard()

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
print("It's a draw!")


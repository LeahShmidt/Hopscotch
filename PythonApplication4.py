#game:
#throw stone (input from user)
#jump to the 1st square
# and then again
#until square 10
#when player 1 is out player 2 starts
#
square = 1
oneFoot = [1,4,7,10]
twoFeet = [2,3,5,6,8,9]
print ("Welcome to the hopscotch game!")
while square <10:
	number = int(input("Please throw the stone, and jump. what square did the stone land in? "))
	feet = int(input("How many feet did you land on? "))
	if number != square:
		print ("You're out")
	if number in oneFoot:
		if  feet == 2:
			print ("You're out!")
			square = 10
	#elif:
		#if number in twoFeet:
			
	else: 
			print ("Very nice! Good job!")
			print (("now jump to square {0:d}").format (square))
		square = square + 1

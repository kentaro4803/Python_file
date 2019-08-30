lister = [4,5,7,9]
while True:
 	print("Type q to quit")
 	ans = input("Guess a number in the list.")
 	if ans == "q":
 		break
 	elif ans in lister:
 		print("Good guess, you got it.")
 	else:
 		print("Wrong, try again")

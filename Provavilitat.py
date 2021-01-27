import random
count = 0


while count < 3:
	print(pygame.mouse.get_pressed())
	count = count + 1
	number = random.randint(1,10)
	if number == 10:
			print("c")
	if number == 9:
		print("c")	
	if number == 8:
		print("b")
	if number == 7:
		print("b")
	if number == 6:
		print("b")
	if number == 5:
		print("a")
	if number == 4:
		print("a")
	if number == 3:
		print("a")
	if number == 2:
		print("a")
	if number == 1:
		print("a")
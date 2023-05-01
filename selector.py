import random

def select_6():
	numbers = []
	for i in range(6):
		numbers.append(random.randint(1,45))
	print(numbers)

print("printing 6 numbers. press 'q' to quit.")

while True:
	if (input() == 'q'):
		print('quitting...')
		break
	else:
		select_6()

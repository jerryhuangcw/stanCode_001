"""
File: rocket.py
Name: Jerry Huang
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


# This constant determines rocket size.
SIZE = 5


def main():
	"""
	This program prints out a rocket including 6 parts:
	head, belt, upper body, lower body, belt, and head.
	The size of the rocket is determined by the constant "SIZE".
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	This function prints out the rocket's head.
	"""
	for i in range(SIZE):
		for j in range(SIZE*2 + 1):
			if i+j < SIZE:
				print(" ", end="")
			elif j-i > SIZE + 1:
				print(" ", end="")
			elif j <= SIZE:
				if i+j >= SIZE:
					print("/", end="")
			else:
				print("\\", end="")
		print("")


def belt():
	"""
	This function prints out the rocket's belt.
	"""
	print("+", end="")
	for i in range(SIZE*2):
		print("=", end="")
	print("+")


def upper():
	"""
	This function prints out the rocket's upper body.
	"""
	for i in range(SIZE):
		for j in range(SIZE * 2 + 2):
			if j == 0:
				print("|", end="")  # left wall
			elif j == SIZE * 2 + 1:
				print("|", end="")  # right wall
			else:
				if i+j < SIZE:
					print(".", end="")  # left side dot
				elif j-i < SIZE+2:
					if SIZE % 2 == 0:
						if (i+j) % 2 == 0:
							print("/", end="")
						elif (i+j) % 2 == 1:
							print("\\", end="")
					elif SIZE % 2 == 1:
						if (i+j) % 2 == 0:
							print("\\", end="")
						elif (i+j) % 2 == 1:
							print("/", end="")
				else:  # elif j-i > SIZE:
					print(".", end="")  # right side dot
		print("")


def lower():
	"""
	This function prints out the rocket's lower body.
	"""
	for i in range(SIZE):
		for j in range(SIZE * 2 + 2):
			if j == 0:
				print("|", end="")  # left wall
			elif j == SIZE * 2 + 1:
				print("|", end="")  # right wall
			else:
				if j-i <= 0:
					print(".", end="")  # left side dot
				elif i+j <= SIZE*2:
					if SIZE % 2 == 1:
						if (i+j) % 2 == 1:
							print("\\", end="")
						elif (i+j) % 2 == 0:
							print("/", end="")
					elif SIZE % 2 == 0:
						if (i+j) % 2 == 0:
							print("/", end="")
						elif (i+j) % 2 == 1:
							print("\\", end="")
				else:
					print(".", end="")  # right side dot
		print("")


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == "__main__":
	main()

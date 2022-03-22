"""
File: quadratic_solver.py
Name: Jerry Huang
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This program solves quadratic equation ax^2 + bx + c = 0 after
	the user enters the three coefficients. It will print out
	the real roots of the equation.
	"""
	print('stanCode Quadratic Solver!')
	a = float(input('Enter a: '))
	if a == 0:
		print('a can not be zero')
	else:
		b = float(input('Enter b: '))
		c = float(input('Enter c: '))
		if b*b - 4*a*c < 0:  # discriminant
			print('No real roots.')
		else:
			delta = math.sqrt(b * b - 4 * a * c)
			root_1 = (-b - delta) / (2*a)
			root_2 = (-b + delta) / (2*a)
			if delta > 0:
				print('Two real roots: ' + str(root_1) + ' , ' + str(root_2))
			elif delta == 0:
				print('One real root: ' + str(root_1))


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
	main()

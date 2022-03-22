"""
File: weather_master.py
Name: Jerry Huang
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


QUIT = -1  # This constant controls when to quit


def main():
	"""
	This program gives 4 weather data analysis based on input temperature:
	highest temp, lowest temp, average temp, and total cold days (<16°C/°F).
	"""
	print("stanCode \"Weather Master 4.0\"!")
	temp = float(input('Next Temperature: (or ' + str(QUIT) + ' to quit)?: '))
	if temp == QUIT:
		print('No temperatures were entered.')
	else:
		cold = 0  # days that temp < 16
		days = 1  # day count
		total = temp  # total temp
		avg = total / days  # average temp
		high = temp
		low = temp
		if temp < 16:
			cold += 1  # find cold days
		while True:
			temp = float(input('Next Temperature: (or ' + str(QUIT) + ' to quit)?: '))
			if temp == QUIT:
				break
			elif temp < low:
				low = temp  # find lowest temp
			elif temp > high:
				high = temp  # find highest temp
			if temp != QUIT:
				total += temp
				days += 1
				avg = total / days
			if temp < 16:
				cold += 1
		print('Highest temperature =  ' + str(high))
		print('Lowest temperature =  ' + str(low))
		print('Average = ' + str(avg))
		print(str(cold) + " cold day(s)")


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
	main()

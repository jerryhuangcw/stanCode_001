"""
File: hailstone.py
Name: Jerry Huang
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program computes Hailstone sequences when the user enters
    a positive integer. The program will stop when the result
    is "1" and count how many steps are done.
    """
    print('This program computes Hailstone sequences.')
    data = int(input('Enter a positive integer: '))
    if data == 1:
        print('It took 0 steps to reach 1.')
    elif data < 1:
        print(str(data) + ' is not a valid positive integer.')
    else:
        y = 0  # y is step counter, starts from 0 steps
        while True:
            if data == 1:
                break  # stops when result is 1
            elif data % 2 == 1:  # data is odd
                x = data * 3 + 1
                print(str(data) + ' is odd, so I make 3n+1: ' + str(x))
                data = x  # run next loop
            elif data % 2 == 0:  # data is even
                x = data // 2
                print(str(data) + ' is even, so I take half: ' + str(x))
                data = x  # run next loop
            y += 1  # plus one step after a loop is done
        print('It took ' + str(y) + ' steps to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
    main()

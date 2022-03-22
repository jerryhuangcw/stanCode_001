from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: Jerry Huang
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""


def main():
    """
    Karel starts at (1,1) facing east, and will put beepers
    in staggered pattern which the gap between each beeper is 2 units.
    """
    put_beeper()
    fill_one_line()
    go_back()  # back to left boundary facing north
    if front_is_clear():
        move()
        turn_right()  # move to next row facing east
        if front_is_clear():
            move()
            put_beeper()
            fill_one_line()
            go_back()  # facing north
            if front_is_clear():
                move()
                turn_right()  # move to next row facing east
        else:
            fill_first_column()
    while front_is_clear():  # starting from the third row
        fill_the_rest()


def fill_one_line():
    """
    Pre-Condition: Karel is at the left boundary of the row facing east.
    Post-Condition: Karel is at the right boundary of the row facing east. Beepers are put in staggered pattern.
    """
    while front_is_clear():
        move()
        if front_is_clear():  # check if reach the wall
            move()
            put_beeper()


def go_back():
    """
    Pre-Condition: Karel is at the right boundary of the row facing east.
    Post-Condition: Karel is at the left boundary of the row facing north.
    """
    turn_left()
    turn_left()  # facing west
    while front_is_clear():
        move()
    turn_right()  # facing north


def fill_first_column():
    """
    When Karel realizes there's only one column to fill the beepers,
    Karel will go straight up and fill the beepers in staggered pattern.
    """
    turn_left()  # facing north
    move()
    put_beeper()
    fill_one_line()


def fill_the_rest():
    """
    Karel's initial position is at (1,3) facing east.
    After the first and second row are filled with beepers, and the third row
    has more than one column to be filled, Karel will fill the rest of the rows
    with beepers in staggered pattern.
    """
    put_beeper()
    fill_one_line()
    go_back()  # facing north
    if front_is_clear():
        move()
        turn_right()  # move to next row facing east
        if front_is_clear():
            move()
            put_beeper()
            fill_one_line()
            go_back()  # back to left boundary facing north
            if front_is_clear():
                move()
                turn_right()  # move to next row facing east
        else:
            turn_left()  # facing north
            move()
            turn_right()  # move to next row facing east


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)

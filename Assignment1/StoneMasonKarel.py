from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: Jerry Huang
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():
    """
    Karel's initial position is at (1,1) facing east.
    It will build a column that is 5 beepers tall,
    go back to the bottom, and move 4 units to the right to build next column.
    After building the last column, Karel stays at the bottom of the column facing east.
    """
    while front_is_clear():
        build_column()
        climb_down()
        if front_is_clear():
            for i in range(4):
                move()  # Move and ready to build next column
    build_column()  # build last column
    climb_down()


def build_column():
    """
    Pre-Condition: Karel is at the bottom of the column facing east.
    Post-Condition: Karel is at the top of the column facing south. Column is built.
    """
    turn_left()  # facing north
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        move()
    while not front_is_clear():
        if not on_beeper():
            put_beeper()
        else:
            turn_left()
            turn_left()  # facing south


def climb_down():
    """
    Pre-Condition: Karel is at the top of the column facing south.
    Post-Condition: Karel is at the bottom of the column facing east.
    """
    while front_is_clear():
        move()
    turn_left()  # facing east


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)

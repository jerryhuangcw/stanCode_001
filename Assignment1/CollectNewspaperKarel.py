from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: Jerry Huang
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    Karel's initial position is at (3,4) facing east.
    It needs to pick up the newspaper(beeper) at (6,3), go back
    to the initial position facing east, and drop the newspaper.
    """
    pick_newspaper()
    read_newspaper()


def pick_newspaper():
    """
    Pre-Condition: Karel is at (3,4) facing east.
    Post-Condition: Karel is at (6,3) facing east. Beeper is picked.
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()


def read_newspaper():
    """
    Pre-Condition: Karel is at (6,3) facing east. Beeper is picked.
    Post-Condition: Karel is at (3,4) facing east. Beeper is put.
    """
    turn_left()
    turn_left()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)

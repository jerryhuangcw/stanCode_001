from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: Jerry Huang
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    Karel will put a beeper at the midpoint of 1st Street and stop.
    """
    put_beeper()
    put_second_beeper()
    locate_midpoint()
    return_midpoint()


def put_second_beeper():
    """
    Pre-Condition: Karel is at the first(left) beeper.
    Post-Condition: Karel puts the second beeper at the right boundary.
    """
    while front_is_clear():
        move()
    put_beeper()
    turn_left()
    turn_left()  # facing west


def locate_midpoint():
    """
    Karel will find the midpoint by narrowing the distance of two beepers.
    Pre-Condition: 2 beepers are on both side of the boundaries. Karel is at right boundary.
    Post-Condition: 2 beepers are at midpoint. Karel is at either left or right boundary.
    """
    while front_is_clear():
        move()
        if on_beeper():
            pick_beeper()
            turn_left()
            turn_left()
            move()
            put_beeper()  # Put beeper 1 unit near the midpoint.


def return_midpoint():
    """
    Pre-Condition: 2 beepers at midpoint. Karel is at either left or right boundary.
    Post-Condition: Only 1 beeper at midpoint. Karel is also at midpoint.
    """
    turn_left()
    turn_left()
    while not on_beeper():
        move()
    pick_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)

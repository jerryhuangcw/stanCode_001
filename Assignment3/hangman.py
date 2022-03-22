"""
File: hangman.py
Name: Jerry Huang
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to correctly figure the
un-dashed word out by inputting one character each round.
If the user input is correct, show the updated word on console.
Players have N_TURNS chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    The program would first randomly select a word from random_word()
    as the final answer, and let the player know how many letters in it
    using multiple dash lines and how many guesses they have. The player
    is allowed to enter an letter each time. If the player guesses a correct
    letter, it will be revealed as a hint. If the player guesses a wrong letter,
    the player will lose a life. The program won't stop until the player guesses
    the final answer or the player has no guesses left.
    """
    lives = N_TURNS  # initial player's lives
    answer = random_word()  # final answer
    relay = ""  # relay is used to store player's best guess so far
    input_ch = first(answer)
    if answer.find(input_ch) == -1:
        print("There is no " + input_ch + "'s in the word.")
        lives -= 1
        relay = dash(answer)
    else:
        print("You are correct!")
        for i in range(len(answer)):
            ch = answer[i]
            if input_ch == ch:
                relay += input_ch
            elif input_ch != ch:
                relay += "-"
    print("The word looks like: " + str(relay))
    print("You have " + str(lives) + " guesses left.")
    input_ch = user_input()
    while lives > 1:
        if answer.find(input_ch) == -1:
            print("There is no " + input_ch + "'s in the word.")
            lives -= 1
        else:
            print("You are correct!")
            for j in range(len(answer)):
                guess = ""
                guess += relay[:j]  # load the previous guess result
                ch = answer[j]
                if input_ch == ch:
                    guess = relay[:j] + ch + relay[j+1:]
                elif input_ch != ch:
                    guess = relay
                relay = guess  # saves the best guess result to relay
        if relay == answer:
            break
        else:
            print("The word looks like: " + str(relay))
            print("You have " + str(lives) + " guesses left.")
            input_ch = user_input()
    if relay == answer:
        print("You win!! \nThe word was: " + answer)
    else:
        print("You are completely hung : ( \nThe word was: " + answer)


def user_input():
    """
    This function ask the player to take a guess and check if the input is valid.
    :return: str, a valid guess
    """
    while True:
        input_ch = str(input("Your guess: "))
        input_ch = input_ch.upper()
        if not input_ch.isalpha():  # input requires alphabets only
            print("illegal format.")
        elif len(input_ch) != 1:  # input requires single alphabet only
            print("illegal format.")
        else:
            break
    return input_ch


def dash(answer):
    """
    This function is used for printing the original hint(all dashes).
    :param answer: str, the final answer, determining how many dashes
    :return: str, the original hint(all dashes)
    """
    dashed = ""
    for i in range(len(answer)):
        dashed += "-"
    return dashed


def first(answer):
    """
    This function asks for the player's first guess.
    :param answer: str, the final answer, is used to print dashes
    :return: str, a valid first guess
    """
    dashed = dash(answer)
    print("The word looks like: " + str(dashed))
    print("You have " + str(N_TURNS) + " guesses left.")
    while True:
        input_ch = str(input("Your guess: "))
        input_ch = input_ch.upper()
        if not input_ch.isalpha():  # input requires alphabets only
            print("illegal format.")
        elif len(input_ch) != 1:  # input requires single alphabet only
            print("illegal format.")
        else:
            break
    return input_ch


def random_word():
    """
    The function randomly picks a word as the final answer.
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#  DO NOT EDIT THE CODE BELOW THIS LINE  #
if __name__ == '__main__':
    main()

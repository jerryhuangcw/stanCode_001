"""
File: similarity.py
Name: Jerry Huang
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program asks the user to input a DNA sequence and a
    shorter target DNA sequence, and them find the homology.
    """
    long_sequence = input("Please give me a DNA sequence to search: ")
    long_sequence = long_sequence.upper()  # case insensitive
    short_sequence = input("What DNA sequence would you like: ")
    short_sequence = short_sequence.upper()  # case insensitive
    homology(long_sequence, short_sequence)


def homology(long_sequence, short_sequence):
    """
    :param long_sequence: str, original DNA sequence to search
    :param short_sequence: str, DNA sequence to match
    :return: str, homology in the sequence
    """
    maximum = 0  # max homology found in the sequence
    match = long_sequence[len(short_sequence)]  # initial state of the best match
    for i in range(len(long_sequence) - len(short_sequence) + 1):
        y = 0  # similarity counter
        for j in range(len(short_sequence)):
            ls = long_sequence[i+j]  # locate partial original DNA
            ss = short_sequence[j]  # locate target DNA
            if ss == ls:
                y += 1
            if j == len(short_sequence) - 1:
                if y > maximum:
                    maximum = y
                    match = long_sequence[i:i + len(short_sequence)]  # find best match
    print("The best match is " + match)


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()

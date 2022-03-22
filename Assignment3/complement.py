"""
File: complement.py
Name: Jerry Huang
----------------------------
This program uses string manipulation to tackle a real world problem - finding the
complement strand of a DNA sequence. The program asks users for a DNA sequence as
a python string that is case-insensitive. Your job is to output the complement of it.
"""


def main():
    """
    The program asks user to input a DNA strand, and prints out
    the complementary DNA.
    """
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    dna = dna.upper()  # case insensitive
    new_dna = build_complement(dna)
    print('The complement of ' + str(dna) + ' is ' + str(new_dna))


def build_complement(dna):
    """
    :param dna: str, input DNA strand
    :return: str, complementary DNA
    """
    ans = ""
    for base in dna:
        if base == 'A':
            ans += 'T'
        elif base == 'T':
            ans += 'A'
        elif base == 'C':
            ans += 'G'
        elif base == 'G':
            ans += 'C'
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()

"""
File: caesar.py
Name: Jerry Huang
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    The program asks for a secret number, which will be the steps that
    the alphabets are moved to the right. The program will decipher the
    ciphered string based on "Caesar Cipher".
    """
    number = int(input("Secret Number: "))  # steps that the alphabet is moved to the right
    new_alphabet = ""
    for i in range(len(ALPHABET)):
        ch = ALPHABET[(i - number + 26) % 26]  # if i==0, (0-number+26)%26 is the first alphabet to stream, etc..
        new_alphabet += ch
    cipher = input("What's the ciphered string? ")
    cipher = cipher.upper()  # case insensitive
    print("The deciphered string is: ", end="")
    for j in range(len(cipher)):
        code = cipher[j]  # letter in ciphered string
        for k in range(len(new_alphabet)):
            new = new_alphabet[k]  # letter in new_alphabet
            if code == new:
                print(ALPHABET[k], end="")  # decipher
        if ALPHABET.find(code) == -1:
            print(cipher[j], end="")  # prints anything not alphabet, such as numbers or punctuation marks


#  DO NOT EDIT THE CODE BELOW THIS LINE  #
if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:
"""


CHAR2CODE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--"
}

CODE2CHAR = {v: k for k, v in CHAR2CODE.items()}


def encode(char):
    """Encode char to morse code """
    return CHAR2CODE[char.upper()]


def decode(code):
    """Decode morse code to char """
    return CODE2CHAR[code]


if __name__ == '__main__':
    print(CHAR2CODE)
    print(CODE2CHAR)

    MSG = "Spam"
    ENCODIERT = list()

    for c in MSG:
        ENCODIERT.append(encode(c))

    print(ENCODIERT)

    for co in ENCODIERT:
        print(decode(co), end='')
    print()

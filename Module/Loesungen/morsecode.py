#!/usr/bin/env python
# -*- coding: utf-8 -*-


morse_char2code = {
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

morse_code2char = {v: k for k, v in morse_char2code.items()}


def encode(char):
    return morse_char2code[char.upper()]


def decode(code):
    return morse_code2char[code]


if (__name__ == '__main__'):
    print(morse_char2code)
    print(morse_code2char)

    msg = "Spam"
    encodiert = list()

    for c in msg:
        encodiert.append(encode(c))

    print(encodiert)

    for code in encodiert:
        print(decode(code), end='')
    print()

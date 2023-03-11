#!/usr/bin/env python3 -tt
"""
File: crypto.py
---------------

Assignment 1: Cryptography
Name: Bence Racz

"""

from constants import SHIFT_BY
shiftBy = SHIFT_BY


def check_letter(character):
    """
    Checks if the given character is between A-Z or a-z (ascii table)
    """
    return (64 < ord(character) < 91) or (96 < ord(character) < 123)


def encrypt_caesar(plaintext):
    """
    Encrypts plain text using the Caesar cipher
    """
    cipher = ""
    for character in plaintext:
        if check_letter(character):
            character = chr((ord(character) + shiftBy - 65) % 26 + 65)
        cipher += character
    return cipher


def decrypt_caesar(ciphertext):
    """
    Decrypts the cipher text that was encrypted using the Caesar cipher
    """
    plainText = ""
    for character in ciphertext:
        if check_letter(character):
            character = chr((ord(character) - shiftBy - 65) % 26 + 65)
        plainText += character
    return plainText


def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts the plain text with the given keyword
    """
    cipher = ""
    for i in range(len(plaintext)):
        character = plaintext[i]
        if check_letter(character):
            character = chr((ord(character) + (ord(keyword[i]) - 65) - 65) % 26 + 65)
        cipher += character
    return cipher


def decrypt_vigenere(ciphertext, keyword):
    """
        Decrypts the cipher text with the given keyword
    """
    plainText = ""
    for i in range(len(ciphertext)):
        character = ciphertext[i]
        if check_letter(character):
            character = chr((ord(character) - (ord(keyword[i]) - 65) - 65) % 26 + 65)
        plainText += character
    return plainText


def encrypt_scytale(plainText, scytale_circumference):
    """
    Encrypts plain text with the given circumference
    """
    cipher = ""
    plainText = list(plainText)
    for i in range(0, int(scytale_circumference)):
        j = i
        while j < len(plainText):
            cipher += plainText[j]
            j += int(scytale_circumference)
    return cipher


def decrypt_scytale(cipherText, scytale_circumference):
    """
    Decrypts cipher that was encrypted with the Scytale cipher
    """
    plainText = ""
    cipherText = list(cipherText)
    for i in range(0, int(scytale_circumference) - 1):
        j = i
        while j < len(cipherText):
            plainText += cipherText[j]
            j += int(scytale_circumference) - 1
    return plainText


def encrypt_railfence(plainText):
    """
    Encrypts plain text using the Railfence cipher
    """
    cipher = ""
    plainText = list(plainText)
    dist = 4
    for i in range(0, 3):
        j = i
        while j < len(plainText):
            cipher += plainText[j]
            j += dist
        if i == 0:
            dist = 2
        else:
            dist = 4
    return cipher


def collect_line_members(cipherText, a, b, c):
    """
    Collects the characters on all 3 lines
    """
    if (len(cipherText) - 1) % 4 == 0:
        offset = 1
    else:
        offset = 0
    for i in range(0, len(cipherText)):
        if i < int(len(cipherText) / 3) - offset:
            a.append(cipherText[i])
        elif i < int(len(cipherText) / 2) + int(len(cipherText) / 3) - offset:
            b.append(cipherText[i])
        else:
            c.append(cipherText[i])


def decrypt_railfence(cipherText):
    """
    Decrypts a cipher encrypted using a railfence cipher
    """
    plainText = ""
    a = []; b = []; c = []
    x = 0; y = 0; z = 0
    collect_line_members(cipherText, a, b, c)
    lengthA = len(a)
    lengthB = len(b)
    lengthC = len(c)

    for i in range(0, len(cipherText)):
        if x < lengthA:
            plainText += a[x]
            x += 1
        if y < lengthB:
            plainText += b[y]
            y += 1
        if z < lengthC:
            plainText += c[z]
            z += 1
        if y < lengthB:
            plainText += b[y]
            y += 1

    return plainText

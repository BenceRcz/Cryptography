#!/usr/bin/env python3 -tt
"""
File: crypto.py
---------------
Assignment 1: Cryptography
Course: CS 41
Name: Bence Racz
SUNet: <SUNet ID>

Replace this with a description of the program.
"""
import math

import utils

shiftBy = 3


def check_letter(character):
    return (64 < ord(character) < 91) or (96 < ord(character) < 123)


# Caesar Cipher
def encrypt_caesar(plaintext):
    cipher = ""
    for character in plaintext:
        if check_letter(character):
            character = chr((ord(character) + shiftBy - 65) % 26 + 65)
        cipher += character
    return cipher


# Decrypts Caesar cypher
def decrypt_caesar(ciphertext):
    plainText = ""
    for character in ciphertext:
        if check_letter(character):
            character = chr((ord(character) - shiftBy - 65) % 26 + 65)
        plainText += character
    return plainText


# Vigenere Cipher
def encrypt_vigenere(plaintext, keyword):
    cipher = ""
    for i in range(len(plaintext)):
        character = plaintext[i]
        if check_letter(character):
            character = chr((ord(character) + (ord(keyword[i]) - 65) - 65) % 26 + 65)
        cipher += character
    return cipher


# Decrypts Vigenere Cipher
def decrypt_vigenere(ciphertext, keyword):
    plainText = ""
    for i in range(len(ciphertext)):
        character = ciphertext[i]
        if check_letter(character):
            character = chr((ord(character) - (ord(keyword[i]) - 65) - 65) % 26 + 65)
        plainText += character
    return plainText


# Scytale cipher
def encrypt_scytale(plainText, scytale_circumference):
    cipher = ""
    plainText = list(plainText)
    for i in range(0, int(scytale_circumference)):
        j = i
        while j < len(plainText):
            cipher += plainText[j]
            j += int(scytale_circumference)
    return cipher


# Decrypts Scytale
def decrypt_scytale(cipherText, scytale_circumference):
    plainText = ""
    cipherText = list(cipherText)
    for i in range(0, int(scytale_circumference) - 1):
        j = i
        while j < len(cipherText):
            plainText += cipherText[j]
            j += int(scytale_circumference) - 1
    return plainText


# Railfence cypher
def encrypt_railfence(plainText):
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


# Solitaire cipher
def encrypt_solitaire():
    return
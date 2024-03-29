# This module contains functions for the Merkle-Hellman Knapsack Cryptosystem

from random import randint
import math


# This function implements the private key generation for Merkle-Hellman Knapsack Cryptosystem
from lab1 import utils


def generate_private_key(n=8):          # By default, we create 8 bit long chunks
    """
    Generates private key
    """
    w = [0 for _ in range(n)]
    w[0] = randint(2, 10)
    total = w[0]

    for i in range(n):
        w[i] = total + randint(total + 1, 2 * total)
        total += w[i]

    q = randint(total + 1, 2 * total)
    r = randint(2, q - 1)

    while not math.gcd(r, q):
        r = randint(2, q - 1)

    return w, q, r


def create_public_key(privateKey):
    """
    Creates a public key using the given privateKey
    """
    w, q, r = privateKey
    n = len(w)

    beta = [0 for _ in range(n)]

    for i in range(n):
        beta[i] = (r * w[i]) % q

    return beta


def encrypt_mh(messageToBeEncrypted, publicKey):
    """
    Encryption of a given messageToBeEncrypted using the given publicKey
    """
    convertedChar = []
    cipher = []

    b = publicKey

    for char in messageToBeEncrypted:
        convertedChar = utils.byte_to_bits(ord(char))
        total = 0
        for i in range(len(b)):
            total += convertedChar[i] * b[i]

        cipher.append(total)

    return cipher


def decrypt_mh(messageToBeEncrypted, privateKey):
    """
    decryption of a cipher which was encrypted using the publicKey
    """
    decryptedBytes = []
    decryptedText = ""
    c_ = []
    a = []

    w, q, r = privateKey
    n = len(w)
    s = utils.modinv(r, q)

    for byte in messageToBeEncrypted:
        c_.append(byte * s % q)

    for c in c_:
        x = []
        m = 0
        while c != 0:
            for i in range(n - 1, 0, -1):
                if w[i] <= c:
                    c -= w[i]
                    x.append(i + 1)

        for i in x:
            m += pow(2, 8 - i)

        decryptedBytes.append(m)
        decryptedText += chr(m)

    return decryptedBytes, decryptedText


# pKey = generate_private_key(8)
# pubKey = create_public_key(pKey)
# message = encrypt_mh("I am hurt $end help120438 10248@#59", pubKey)
# print(message)
# byte_array, text = decrypt_mh(message, pKey)
# print(byte_array, "\n", text)

import math

from lab2.encryptors import (solitaire, bbs)


solitaire_deck_size = 54


def bin_to_decimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def convert_to_binary(data):
    binary = ''.join(format(ord(i), '032b') for i in data)
    return binary


def generate_key(data, enc_algorithm):
    if enc_algorithm == solitaire:
        seed = [i + 1 for i in range(54)]
    else:
        seed = 32
    key = ""
    size = math.trunc(len(data) / 32)
    for i in range(size):
        if enc_algorithm == solitaire:
            key += format(enc_algorithm(seed), '032b')
        else:
            key += enc_algorithm(seed)
    return key


def encrypt(data, key):
    new = [(ord(a) ^ ord(b)) for a, b in zip(key, data)]
    cipher = ""
    for i in new:
        cipher += str(i)
    return cipher


def decrypt(data, key):
    new = [(ord(a) ^ ord(b)) for a, b in zip(key, data)]
    message = ""
    for i in new:
        message += str(i)
    return message


def convert_bin_to_string(binary_data):
    str_data = ""
    for i in range(0, len(binary_data), 32):
        temp_data = int(binary_data[i:i + 32])
        decimal_data = bin_to_decimal(temp_data)
        str_data += chr(decimal_data)
    return str_data


def main():
    data = input("data to be encrypted: ")
    binary_data = convert_to_binary(data)
    key = generate_key(binary_data, bbs)
    cipher = encrypt(binary_data, key)
    message = decrypt(cipher, key)
    # print("The cipher: " + convert_bin_to_string(cipher))
    print(convert_bin_to_string(message))
    return


if __name__ == "__main__":
    main()

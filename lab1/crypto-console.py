#!/usr/bin/env python3 -tt
"""
File: crypto-byte_array_encryption.py
-----------------------
Implements a console menu to interact with the cryptography functions exported
by the crypto module.
"""

from crypto import (encrypt_caesar, decrypt_caesar,
                    encrypt_vigenere, decrypt_vigenere, encrypt_scytale,
                    decrypt_scytale, encrypt_railfence, decrypt_railfence,
                    check_letter)

from utils import clear


#############################
# GENERAL CONSOLE UTILITIES #
#############################

def get_tool():
    print("* Tool *")
    return _get_selection("(C)aesar, (V)igenere or (M)erkle-Hellman or (S)cytale or (R)ailfence ? ", "CVMSR")


def get_action():
    """Return true if encrypt"""
    print("* Action *")
    return _get_selection("(E)ncrypt or (D)ecrypt? ", "ED")


def get_filename():
    filename = input("Filename? ")
    while not filename:
        filename = input("Filename? ")
    return filename


def get_input(binary=False):
    print("* Input *")
    choice = _get_selection("(F)ile or (S)tring? ", "FS")
    clear()
    if choice == 'S':
        text = input("Enter a string: ").strip().upper()
        clear()
        while not text:
            text = input("Enter a string: ").strip().upper()
            clear()
        if binary:
            return bytes(text, encoding='utf8')
        return text
    else:
        filename = get_filename()
        flags = 'r'
        if binary:
            flags += 'b'
        with open(filename, flags) as infile:
            return infile.read()


def set_output(output, binary=False):
    print("* Output *")
    choice = _get_selection("(F)ile or (S)tring? ", "FS")
    if choice == 'S':
        print(output)
    else:
        filename = get_filename()
        flags = 'w'
        if binary:
            flags += 'b'
        with open(filename, flags) as outfile:
            print("Writing data to {}...".format(filename))
            outfile.write(output)


def _get_selection(prompt, options):
    choice = input(prompt).upper()
    while not choice or choice[0] not in options:
        choice = input("Please enter one of {}. {}".format('/'.join(options), prompt)).upper()
    clear()
    return choice[0]


def get_yes_or_no(prompt, reprompt=None):
    """
    Asks the user whether they would like to continue.
    Responses that begin with a `Y` return True. (case-insensitively)
    Responses that begin with a `N` return False. (case-insensitively)
    All other responses (including '') cause a reprompt.
    """
    if not reprompt:
        reprompt = prompt

    choice = input("{} (Y/N) ".format(prompt)).upper()
    while not choice or choice[0] not in ['Y', 'N']:
        choice = input("Please enter either 'Y' or 'N'. {} (Y/N)? ".format(reprompt)).upper()

    clear()
    return choice[0] == 'Y'


def check_length(text):
    return len(text) > 0


def clean_caesar(text):
    """Converts text to a form compatible with the preconditions imposed by Caesar cipher"""
    return text.upper()


def clean_vigenere(text):
    """
    Converts text to a form compatible with the preconditions imposed by Vigenere cipher

    Returns error if the user has provided an invalid input
    Returns without error if input was valid (or it could be modified)
    """
    if not check_length(text):
        print("The messageToBeEncrypted has to have a length greater then 0")
        exit(0)
    for x in text:
        if not check_letter(x):
            print("The messageToBeEncrypted and the keyword can only contain letters!")
            exit(0)
    return ''.join(ch for ch in text.upper() if ch.isupper())


def run_caesar():
    """
    Runs the caesar cryptosystem

    If the user selects encryption then it will call the encryption function
    Else it will call the decryption function
    """
    action = get_action()
    encrypting = action == 'E'
    data = clean_caesar(get_input(binary=False))

    print("* Transform *")
    print("{}crypting {} using Caesar cipher...".format('En' if encrypting else 'De', data))

    output = (encrypt_caesar if encrypting else decrypt_caesar)(data)

    set_output(output)


def run_vigenere():
    """
    Runs the vigenere cryptosystem

    If the user selects encryption then it will call the encryption function
    Else it will call the decryption function
    """
    action = get_action()
    encrypting = action == 'E'
    data = clean_vigenere(get_input(binary=False))

    print("* Transform *")
    keyword = clean_vigenere(input("Keyword? "))

    print("{}crypting {} using Vigenere cipher and keyword {}...".format('En' if encrypting else 'De', data, keyword))

    output = (encrypt_vigenere if encrypting else decrypt_vigenere)(data, keyword)

    set_output(output)


def run_scytale():
    """
    Runs the scytale cryptosystem

    If the user selects encryption then it will call the encryption function
    Else it will call the decryption function
    """
    action = get_action()
    encrypting = action == 'E'
    data = clean_caesar(get_input(binary=False))

    circumference = input("Circumference? ")

    print("* Transform *")
    print("{}crypting {} using Scytale cipher...".format('En' if encrypting else 'De', data))

    output = (encrypt_scytale if encrypting else decrypt_scytale)(data, circumference)

    set_output(output)


def run_railfence():
    """
    Runs the railfence cryptosystem

    If the user selects encryption then it will call the encryption function
    Else it will call the decryption function
    """
    action = get_action()
    encrypting = action == 'E'
    data = clean_caesar(get_input(binary=False))

    print("* Transform *")
    print("{}crypting {} using Scytale cipher...".format('En' if encrypting else 'De', data))

    output = (encrypt_railfence if encrypting else decrypt_railfence)(data)

    set_output(output)


def run_suite():
    """
    Runs a single iteration of the cryptography suite.

    Asks the user for input text from a string or file, whether to encrypt
    or decrypt, what tool to use, and where to show the output.
    """
    print('-' * 34)
    tool = get_tool()
    # This isn't the cleanest way to implement functional control flow,
    # but I thought it was too cool to not sneak in here!
    commands = {
        'C': run_caesar,  # Caesar Cipher
        'V': run_vigenere,  # Vigenere Cipher
        'S': run_scytale,  # Scytale Cipher
        'R': run_railfence  # Railfence
    }
    commands[tool]()


def main():
    """main function of console application"""
    print("Welcome to the Cryptography Suite!")
    run_suite()
    while get_yes_or_no("Again?"):
        run_suite()
    print("Goodbye!")


if __name__ == '__main__':
    main()

# The purpose of this file is to test encryption & decryption using Solitaire cryptosystem

import unittest
import lab1.utils as utils
from lab2.encryptors import solitaire
from lab2.byte_array_encryption import (convert_bin_to_string, convert_to_binary, encrypt, decrypt, generate_key)


# This class implements a test class for Solitaire cryptosystem
class TestSolitaire(unittest.TestCase):
    # Tests solitaire using a random string of length 3
    def test_Solitaire_3(self):
        message = utils.get_random_string(3)
        binary_data = convert_to_binary(message)
        key = generate_key(binary_data, solitaire)
        cipher = encrypt(binary_data, key)
        decryptedBin = decrypt(cipher, key)
        self.assertEqual(message, convert_bin_to_string(decryptedBin))

    # Tests solitaire using a random string of length 300
    def test_Solitaire_300(self):
        message = utils.get_random_string(300)
        binary_data = convert_to_binary(message)
        key = generate_key(binary_data, solitaire)
        cipher = encrypt(binary_data, key)
        decryptedBin = decrypt(cipher, key)
        self.assertEqual(message, convert_bin_to_string(decryptedBin))


if __name__ == '__main__':
    unittest.main()

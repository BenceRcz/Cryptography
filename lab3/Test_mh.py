# The purpose of this file is to test MerkleHellman encryption & decryption

import unittest
import random
import string
import MerkleHellman


# This function returns a random string
def get_random_string(length):
    letters = string.ascii_lowercase
    res = ''.join(random.choice(letters) for i in range(length))
    return res


# This class implements a test class for Merkle-Hellman
class TestMerkleHellman(unittest.TestCase):
    def test_mh_3(self):
        message = get_random_string(3)
        pvtK = MerkleHellman.generate_private_key(8)
        pubK = MerkleHellman.create_public_key(pvtK)
        cipher = MerkleHellman.encrypt_mh(message, pubK)
        byte_array, decryptedText = MerkleHellman.decrypt_mh(cipher, pvtK)
        self.assertEqual(message, decryptedText)

    def test_mh_16(self):
        message = get_random_string(16)
        pvtK = MerkleHellman.generate_private_key(8)
        pubK = MerkleHellman.create_public_key(pvtK)
        cipher = MerkleHellman.encrypt_mh(message, pubK)
        byte_array, decryptedText = MerkleHellman.decrypt_mh(cipher, pvtK)
        self.assertEqual(message, decryptedText)


if __name__ == '__main__':
    unittest.main()

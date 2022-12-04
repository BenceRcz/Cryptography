from encryptors import (solitaire, bbs)


def encrypt(func, data, seed):
    initial_solitaire_seed = [i for i in range(55)]         # 53 is the white joker and 54 is the black joker
    print(solitaire(initial_solitaire_seed))
    return


def decrypt(func, data, seed):
    return


def main():
    encrypt(1, 1, 1)
    return


if __name__ == "__main__":
    main()

from encryptors import (solitaire, bbs)


solitaire_deck_size = 54


def encrypt(func, data, seed):
    initial_solitaire_seed = [i + 1 for i in range(solitaire_deck_size)]   # 53 -> white joker and 54 -> black joker
    print(initial_solitaire_seed)
    print(solitaire(initial_solitaire_seed))
    return


def decrypt(func, data, seed):
    return


def main():
    encrypt(1, 1, 1)
    return


if __name__ == "__main__":
    main()

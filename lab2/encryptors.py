import numpy


# This function implements the first 2 steps of the Solitaire algorithm
# Moving the joker (black and white)
def move_joker(seed, joker, joker_index, seed_length):
    if joker == 53:             # joker type
        joker_offset = 1
    else:
        joker_offset = 2

    if joker_index < seed_length - joker_offset:       # -1 or -2
        seed[joker_index], seed[joker_index + joker_offset] = seed[joker_index + joker_offset], seed[joker_index]
    else:
        if joker == 53:         # white joker is last element
            i = seed_length - joker_offset
            while i > 1:
                seed[i] = seed[i - 1]
                i -= 1
            seed[1] = joker
    return seed


# This function implements the Solitaire algorithm to generate a key
def solitaire(seed):
    seed_length = len(seed)
    numpy.random.shuffle(seed)
    white_joker = seed.index(53)
    black_joker = seed.index(54)

    return seed


# This function implements the Blum-Blum-Shub algorithm to generate a key
def bbs(seed):
    return

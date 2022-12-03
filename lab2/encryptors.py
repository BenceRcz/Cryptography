import numpy


# This function implements the first 2 steps of the Solitaire algorithm
# Moving the joker (black and white)
def move_joker(seed, joker, joker_index, seed_length):
    if joker == 53:  # joker type
        joker_offset = 1
    else:
        joker_offset = 2

    if joker_index < seed_length - joker_offset:  # -1 or -2
        seed[joker_index], seed[joker_index + joker_offset] = seed[joker_index + joker_offset], seed[joker_index]
    else:
        if joker == 53 or (joker == 54 and joker_index == seed_length - 2):  # white joker is last element or
            # black joker is next to last
            i = seed_length - joker_offset
            while i > 1:
                seed[i] = seed[i - 1]
                i -= 1
            seed[1] = joker
        elif joker_index == seed_length - 1:
            i = seed_length - 1
            while i > 2:
                seed[i] = seed[i - 1]
                i -= 1
            seed[2] = joker
    return seed


# This function swaps the cards before the first joker with the ones after the second joker
def move_between_jokers(seed, first_index, last_index):
    new_seed = []
    seed_length = len(seed)
    for i in range(last_index, seed_length):    # after last joker
        new_seed.append(seed[i])
    new_seed.append(first_index)
    for i in range(first_index, last_index):    # between the 2 jokers
        new_seed.append(seed[i])
    new_seed.append(last_index)
    for i in range(first_index):        # before first joker
        new_seed.append(seed[i])

    return new_seed


# This function implements the Solitaire algorithm to generate a key
def solitaire(seed):
    seed_length = len(seed)
    numpy.random.shuffle(seed)
    white_joker = seed.index(53)
    black_joker = seed.index(54)

    seed = move_joker(seed, 53, white_joker, seed_length)
    seed = move_joker(seed, 54, black_joker, seed_length)

    white_joker = seed.index(53)
    black_joker = seed.index(54)

    if white_joker < black_joker:
        move_between_jokers(seed, white_joker, black_joker)
    else:
        move_between_jokers(seed, black_joker, white_joker)

    return seed


# This function implements the Blum-Blum-Shub algorithm to generate a key
def bbs(seed):
    return

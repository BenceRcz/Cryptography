import numpy


white_joker_value = 53
black_joker_value = 54


# This function implements the first 2 steps of the Solitaire algorithm
# Moving the joker (black and white)
def move_joker(seed, joker, joker_index, seed_length):
    if joker == white_joker_value:  # joker type
        joker_offset = 1
    else:
        joker_offset = 2

    if joker_index < seed_length - joker_offset:  # -1 or -2
        seed[joker_index], seed[joker_index + joker_offset] = seed[joker_index + joker_offset], seed[joker_index]
    else:
        if joker == white_joker_value or \
                (joker == black_joker_value and joker_index == seed_length - 2):  # white joker is last element or
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


# This function moves the first n elements before the last element
# Where n is the numeric value of the last element
def count_from_last(seed, seed_length):
    new_seed = []
    for i in range(seed[seed_length - 1], seed_length - 1):
        new_seed.append(seed[i])
    for i in range(seed[seed_length - 1]):
        new_seed.append(seed[i])
    new_seed.append(seed[seed_length - 1])
    return new_seed


# This function implements the Solitaire algorithm to generate a key
def solitaire(seed):
    seed_length = len(seed)
    numpy.random.shuffle(seed)
    white_joker = seed.index(white_joker_value)
    black_joker = seed.index(black_joker_value)

    seed = move_joker(seed, white_joker_value, white_joker, seed_length)
    seed = move_joker(seed, black_joker_value, black_joker, seed_length)

    white_joker = seed.index(white_joker_value)
    black_joker = seed.index(black_joker_value)

    if white_joker < black_joker:
        seed = move_between_jokers(seed, white_joker, black_joker)
    else:
        seed = move_between_jokers(seed, black_joker, white_joker)

    if seed[seed_length - 1] != white_joker_value and seed[seed_length - 1] != black_joker_value:
        # last element isn't a joker
        seed = count_from_last(seed, seed_length)

    if seed[0] == black_joker_value or seed[0] == white_joker_value:
        return solitaire(seed)
    else:
        print(seed)
        return seed[seed[0] + 1]


# This function implements the Blum-Blum-Shub algorithm to generate a key
def bbs(seed):
    return

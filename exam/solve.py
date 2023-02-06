

# This is one of the ugliest functions I have ever written, also generates all the possible solutions for the eq
def generate_possible_solutions():
    values = [0, 1]
    solutions = []
    for b0 in values:
        for b1 in values:
            for b2 in values:
                for b3 in values:
                    for b4 in values:
                        for b5 in values:
                            for b6 in values:
                                for b7 in values:
                                    solutions.append((b7, b6, b5, b4, b3, b2, b1, b0))
    return solutions


# This function prints the output
def print_solution(solution):
    print(solution)
    return


# This function solves the equation
def solve():
    possible_solutions = generate_possible_solutions()
    for (b7, b6, b5, b4, b3, b2, b1, b0) in possible_solutions:
        eq0 = (b0 + b4 + b5 + b6 + b7 + 1) % 2 == 1
        eq1 = (b0 + b1 + b5 + b6 + b7 + 1) % 2 == 0
        eq2 = (b0 + b1 + b2 + b6 + b7 + 0) % 2 == 0
        eq3 = (b0 + b1 + b2 + b3 + b7 + 0) % 2 == 1
        eq4 = (b0 + b1 + b2 + b3 + b4 + 0) % 2 == 1
        eq5 = (b1 + b2 + b3 + b4 + b5 + 1) % 2 == 1
        eq6 = (b2 + b3 + b4 + b5 + b6 + 1) % 2 == 1
        eq7 = (b3 + b4 + b5 + b6 + b7 + 0) % 2 == 0
        if eq0 and eq1 and eq2 and eq3 and eq4 and eq5 and eq6 and eq7:
            print_solution((b7, b6, b5, b4, b3, b2, b1, b0))
    return


# Main function of the file
def main():
    solve()
    return


if __name__ == "__main__":
    main()

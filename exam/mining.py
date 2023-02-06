import lab3.constants
import hashlib


# This function prints the output
def print_output(found6, sixes, found7, sevens, i):
    print("----------------------------SIMULATION RESULTS----------------------------")
    print("       - The simulation was completed in: " + str(i) + " iterations")
    print("       - Total numbers found with first 6 bits: " + str(found6))
    print("       - Total numbers found with first 7 bits: " + str(found7))
    for i in sixes:
        print("       - Found number with first six bits 0 at: " + str(i[1]) + " the number: " + str(i[0]))
    for i in sevens:
        print("       - Found number with first seven bits 0 at: " + str(i[1]) + " the number: " + str(i[0]))
    return


# This function simulates the mining process
def simulate():
    found6 = 0
    sixes = []
    found7 = 0
    sevens = []
    i = 0
    n = 0
    converted_string = hashlib.sha256(bytes(lab3.constants.INPUT_STRING, encoding="UTF-8")).hexdigest()
    for i in range(lab3.constants.ITERATIONS):
        converted_n = hex(n)[2:]    # we cut the first part of the hex number ex 0x0 becomes 0
        newValue = converted_string + str(converted_n)
        hashedValue = hashlib.sha256(bytes(newValue, encoding="UTF-8")).hexdigest()

        if hashedValue[:7] == "0000000":
            found7 += 1
            sevens.append((converted_n, i))
            print(str(converted_n) + " " + str(i))

        if hashedValue[:6] == "000000":
            found6 += 1
            sixes.append((converted_n, i))
            print(str(converted_n) + " " + str(i))

        i += 1
        n += 1

    print_output(found6, sixes, found7, sevens, i)
    return


# This is the main function of the file
def main():
    simulate()
    return


if __name__ == "__main__":
    main()

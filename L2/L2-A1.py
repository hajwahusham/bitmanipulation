def numberOfBits(n):
    ones = 0
    zeroes = 0
    while (n):
        if (n & 1 == 1):
            ones += 1
        else:
            zeroes += 1
        n = n >> 1
    print("number of onnes =", ones, "number of zeroes = ", zeroes)

number = int(input("enter your number: "))
numberOfBits(number)
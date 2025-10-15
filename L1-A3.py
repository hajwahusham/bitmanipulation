def numberOfBits(n):
    count = 0
    while (n):
        count += 1
        n >>= 1
    return count

n = int(input("enter a number: "))
print("number of bits: ", numberOfBits(n))
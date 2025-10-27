n = int(input("Enter a number: "))

rev = 0
while n > 0:
    rev = (rev << 1) | (n & 1)  # shift rev left, add the last bit of n
    n >>= 1                     # shift n right to process next bit

print("Reversed:", rev)


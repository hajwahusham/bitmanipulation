# check if a number is power of 4
def powerOf4(number):
    # check if number is positive and a power of 2
    if number <= 0 or (number & (number - 1)) != 0:
        return False
    
    count = 0
    while number > 1:
        number >>= 1
        count += 1

    # check if the only set bit is at an even position
    return count % 2 == 0

number = int(input("enter your number: "))
if powerOf4(number):
    print(number, "is a power of 4")
else:
     print(number, "is not a power of 4")
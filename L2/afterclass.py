# check the rightmost set bit in your number
def rightMostSetbit(number):
    count = 1
    while (number):
        if (number & 1 == 1):
            print("your right most set bit is in: " , count)
            break
        else:
            count += 1

        number = number >> 1


number = int(input("enter your number: "))
rightMostSetbit(number)
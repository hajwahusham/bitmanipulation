def setOrNot (number, n):
    if number & (1 << (n - 1)):
        print ("set")
    else:
        print ("not a set")

number = int(input("enter the number: "))
n = int(input("enter the bit position: "))
setOrNot(number, n)
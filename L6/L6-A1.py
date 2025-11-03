# write a program to find the power set of a set
import math

def printPowerSet(set, setsize):

    # find total elements posssible in the power set
    powerSetSize = (int)(math.pow(2, setsize))

    for outer in range(0, powerSetSize):
        print("{", end="")
        for inner in range(0, setsize):
            # check if inner bit in the outer is set
            # if set then print inner element from set
            if ((outer & (1 << inner)) > 0):
                print(set[inner], end="")
        print("}")

size = int(input("enter sizze of array: "))

lst = []
for i in range(0, size):
    n = int(input(f"enter element number {i+1}: "))
    lst.append(n)

printPowerSet(lst, len(lst))
# finding which number in the array appears odd number of times
# assumption: only 2 numbers appear odd number of times

def twoOdd(arr, size):

    xorof2, x , y , setBit = arr[0], 0, 0, 0

    for i in range(1, size):
        xorof2 = xorof2 ^ arr[i]

    setBit = xorof2 & ~(xorof2 - 1)

    for i in range(size):
        if (arr[i] & setBit):
            x = x ^ arr[i] 
        else:
            y = y ^ arr[i] 

    return(x, y)

arr = []
arr_size = int(input("enter the size of the array: "))
for i in range(0, arr_size):
    z = int(input("enter element: "))
    arr.append(z)

x, y = twoOdd(arr, arr_size)
print("two odd elements are ", x, "& ", y)
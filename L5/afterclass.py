num = int(input("Enter a number: ")) # input number
og = num # to output og number
number = num # to change num into binary for output
count = 0 #to count 1s
max = 0 # to store the maximum number of 1s (max count)
binary = "" # to store the inary value of num for output
# just changing the number to binary
if num == 0:
    binary = 0
else:
    while number > 0:
        bit = number & 1
        binary = str(bit) + binary
        number >>= 1
# counting 1s
while num > 0:
    if num & 1:     
        count += 1
        if count > max:
            max = count
    else:
        count = 0 
    num >>= 1             
# printing
print("Origial number: ", og)
print("Binary representation:", binary)
print("Longest consecutive 1’s:", max)
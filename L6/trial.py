'''
def allSubstrings(s):
    substrings = []

    # generate all substrings
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])

    # remove duplicates
    substrings = list(set(substrings))

    return substrings

# Input
s = input("Enter a string: ")

result = allSubstrings(s)

print("all substrings formed (without duplicates):")
for sub in result:
    print(sub)
'''
# Program to print all substrings of a string
s = input("Enter a string: ")

print("All substrings are:")

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1): 
        print(s[i:j])

'''
def all_substrings_no_duplicates(s):
    substrings = []

    # Generate all substrings
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])

    # Remove duplicates by converting list → set → back to list
    substrings = list(set(substrings))

    return substrings

while True:
# Input from user
    s = input("Enter a string: ")

    result = all_substrings_no_duplicates(s)

    print("Substrings without duplicates:")
    print(result)
    '''
'''
def all_subsequences(s):
    n = len(s)
    subsequences = []

    for mask in range(1, 1 << n):  # 1 to 2^n - 1
        sub = ""
        for i in range(n):
            if mask & (1 << i):  # check if i-th bit is set
                sub += s[i]
        subsequences.append(sub)

    return subsequences

# Input
s = input("Enter a string: ")
result = all_subsequences(s)

print("All subsequences (non-continuous substrings):")
for sub in result:
    print(sub)
'''
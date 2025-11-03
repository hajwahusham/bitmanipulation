# substrings of a string
def allsubstrings(s):
    substrings = []
    seen = set()

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if sub not in seen:
                substrings.append(sub)
                seen.add(sub)

    return substrings


s = input("enter a string: ")
result = allsubstrings(s)

print("substrings (without duplicates): ")
for sub in result:
    print(sub)   

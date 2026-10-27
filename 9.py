def permutations(s, current=""):
    if len(s) == 0:
        print(current)
        return

    for i in range(len(s)):
        permutations(s[:i] + s[i + 1:], current + s[i])

s = input("Enter string: ")
permutations(s)
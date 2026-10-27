def subsequences(s, i, current):
    if i == len(s):
        print(current)
        return

    subsequences(s, i + 1, current)
    subsequences(s, i + 1, current + s[i])

s = input("Enter string: ")
subsequences(s, 0, "")
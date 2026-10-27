def merge_arrays(a, b):
    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[i:])

    return result

a = list(map(int, input("Enter first sorted array: ").split()))
b = list(map(int, input("Enter second sorted array: ").split()))

print(merge_arrays(a, b))
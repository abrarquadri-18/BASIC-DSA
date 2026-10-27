def next_greater(arr):
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            result[index] = arr[i]

        stack.append(i)

    return result

arr = list(map(int, input("Enter array: ").split()))
print(next_greater(arr))
def search_insert(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

print(search_insert(arr, target))
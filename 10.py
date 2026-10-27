def subset_sum(arr, i, target):
    if target == 0:
        return True
    if i == len(arr):
        return False

    include = subset_sum(arr, i + 1, target - arr[i])
    exclude = subset_sum(arr, i + 1, target)

    return include or exclude

arr = list(map(int, input("Enter array: ").split()))
target = int(input("Enter target sum: "))

print(subset_sum(arr, 0, target))
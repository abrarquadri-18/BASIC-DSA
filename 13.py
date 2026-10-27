def floor_ceil(arr, target):
    floor_value = None
    ceil_value = None

    for x in arr:
        if x <= target:
            floor_value = x
        if x >= target:
            ceil_value = x
            break

    return floor_value, ceil_value

arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

print("Floor and Ceil:", floor_ceil(arr, target))
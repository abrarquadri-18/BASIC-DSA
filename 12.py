def count_occurrences(arr, target):
    def lower_bound():
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def upper_bound():
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

    return upper_bound() - lower_bound()

arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

print(count_occurrences(arr, target))
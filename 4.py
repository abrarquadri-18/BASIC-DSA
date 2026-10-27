def sum_digits(n):
    if n == 0:
        return 0
    return abs(n) % 10 + sum_digits(abs(n) // 10)

n = int(input("Enter number: "))
print(sum_digits(n))
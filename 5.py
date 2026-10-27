def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    return x * power(x, n - 1)

x = float(input("Enter base: "))
n = int(input("Enter exponent: "))
print(power(x, n))
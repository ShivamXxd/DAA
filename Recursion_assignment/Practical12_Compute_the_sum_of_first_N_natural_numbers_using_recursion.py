def sum_natural_numbers(n):
    if n == 0:
        return 0
    return n + sum_natural_numbers(n - 1)

print(sum_natural_numbers(5))

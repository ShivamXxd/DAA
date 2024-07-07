def count_zeros(n):
    if n == 0:
        return 0
    last_digit = n % 10
    if last_digit == 0:
        return 1 + count_zeros(n // 10)
    else:
        return count_zeros(n // 10)

print(count_zeros(102030))  

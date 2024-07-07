def reverse_number(n, reversed_num=0):
    if n == 0:
        return reversed_num
    reversed_num = reversed_num * 10 + n % 10
    return reverse_number(n // 10, reversed_num)

print(reverse_number(1234)) 

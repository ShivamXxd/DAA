def special_fibonacci(a, b, n):
    if n == 0:
        return a
    elif n == 1:
        return b
    
    prev1 = a
    prev2 = b
    
    for i in range(2, n + 1):
        current = prev1 ^ prev2
        prev1 = prev2
        prev2 = current
    
    return prev2

T = int(input().strip())

results = []
for _ in range(T):
    a, b, n = map(int, input().strip().split())
    result = special_fibonacci(a, b, n)
    results.append(result)

for result in results:
    print(result)

def geek_onacci(A, B, C, N):
    if N == 1:
        return A
    elif N == 2:
        return B
    elif N == 3:
        return C
    
    geek_series = [A, B, C]
    
    for i in range(3, N):
        next_number = sum(geek_series[-3:])
        geek_series.append(next_number)
    
    return geek_series[-1]

T = int(input().strip())

results = []
for _ in range(T):
    A, B, C, N = map(int, input().strip().split())
    result = geek_onacci(A, B, C, N)
    results.append(result)

for result in results:
    print(result)


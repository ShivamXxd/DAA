def assignMiceHoles(N , M , H):
    # code here
    N = len(M)
    M.sort()
    H.sort()
    max_time = 0
    for i in range(N):
        t = abs(M[i] - H[i])
        max_time = max(max_time, t)
    return max_time

N = 3
M = [4, -4, 2]
H = [4, 0, 5]
print(assignMiceHoles(N, M, H))
def minimumPlatform(n, arr, dep):
    arr.sort()
    dep.sort()
    i = 1
    j = 0
    m = len(arr)
    n = len(dep)
    platform = 1
    result = 1
    while i < m and j < n:
        if arr[i] > dep[j]:
            platform -= 1
            j += 1
        else:
            platform += 1
            i += 1
        if platform > result:
            result = platform
    return result

n = 3
arr = [1009, 1235, 1100]
dep = [1900, 1240, 1200]
print(minimumPlatform(n, arr, dep))
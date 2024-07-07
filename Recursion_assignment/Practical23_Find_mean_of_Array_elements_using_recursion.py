def mean_array(arr, n):
    if n == 0:
        return 0
    return (arr[n - 1] + n * mean_array(arr, n - 1)) / n

arr = [1, 2, 3, 4, 5]
print(mean_array(arr, len(arr)))
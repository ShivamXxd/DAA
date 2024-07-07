def find_max(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n - 1], find_max(arr, n - 1))

def find_min(arr, n):
    if n == 1:
        return arr[0]
    return min(arr[n - 1], find_min(arr, n - 1))

arr = [1, 3, 5, 2, 4]
print("Maximum:", find_max(arr, len(arr)))  # Output: 5
print("Minimum:", find_min(arr, len(arr)))  # Output: 1

def bubble_sort(arr, n):
    if n == 1:
        return arr
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return bubble_sort(arr, n - 1)

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort(arr, len(arr)))  
def find_target_indices(arr):

    indexed_arr = [(value, index) for index, value in enumerate(arr)]
    
    indexed_arr.sort(key=lambda x: x[0])
    
    sorted_indices = [index for value, index in indexed_arr]
    
    return sorted_indices

arr = [3, 1, 4, 2]
sorted_indices = find_target_indices(arr)
print("Original Array:", arr)
print("Sorted Indices:", sorted_indices)

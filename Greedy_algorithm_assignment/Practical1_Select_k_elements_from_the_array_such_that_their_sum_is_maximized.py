def max_sum_greedy(arr, k):
    
    sorted_arr = sorted(arr, reverse=True)

    selected_elements = sorted_arr[:k]

    max_sum = sum(selected_elements)
    return max_sum

arr = [3, 5, 1, 9, 2, 8, 4]
k = 3
print("Maximum sum of", k, "elements:", max_sum_greedy(arr, k))

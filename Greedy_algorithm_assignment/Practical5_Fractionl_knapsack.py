def knapsack(values:list[int], weight:list[int], capacity:int)->float:
    N = len(values)
    items = [[weight[i], values[i]] for i in range(N)]

    items.sort(reverse=True, key=lambda x:x[1]/x[0])
    total_values = 0.0
    current_w = 0
    for item in items:
        w, v = item[0], item[1]
        if current_w + w <= capacity:
            total_values += v
            current_w += w
        else:
            total_values += v*((capacity-current_w)/w)
            break
    return total_values

values = [100, 12*0, 60]
weights = [20, 30, 10]
C = 50

print(knapsack(values=values, weight=weights, capacity=C))
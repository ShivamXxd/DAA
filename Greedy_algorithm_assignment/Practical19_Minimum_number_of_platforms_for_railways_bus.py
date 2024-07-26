def findPlatform(arr, dep, n):
    plat_needed = 1
    result = 1

    for i in range(n):
        
        plat_needed = 1

        for j in range(n):
        
            if i != j:
                if (arr[i] >= arr[j] and dep[j] >= arr[i]):
                    plat_needed += 1

    
        result = max(result, plat_needed)

    return result

def main():
    arr = [100, 300, 500]
    dep = [900, 400, 600]

    n = len(arr)

    print("{}".format(
        findPlatform(arr, dep, n)))


if __name__ == '__main__':
    main()

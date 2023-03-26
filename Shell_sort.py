def Shell_sort(arr):
    g = len(arr) // 2
    while g > 0:
        for i in range(g, len(arr)):
            temp = arr[i]
            j = i
            while j >= g and arr[j-g] > temp:
                arr[j] = arr[j-g]
                j -= g
            arr[j] = temp
        g //= 2
        
    return arr
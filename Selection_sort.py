def Selection_sort(arr):
    for i in range(len(arr) - 1):
        idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[idx]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]   
         
    return arr


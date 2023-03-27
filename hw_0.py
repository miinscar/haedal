# Insertion Sort
def Insertion_sort(arr):
    for i in range(1, len(arr)):
      a = arr[i]
      j = i - 1
      while j >= 0 and arr[j] > a:
          arr[j+1] = arr[j]
          j -= 1
          arr[j+1] = a       
    return arr

# Selection Sort
def Selection_sort(arr):
    for i in range(len(arr) - 1):
        idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[idx]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]            
    return arr

# Bubble Sort
def Bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]           
    return arr

# Shell Sort
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

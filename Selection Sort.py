def selection(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr

def bubblesorting(arr):
  for i in range(len(arr)-1, -1, -1):
    for j in range(i):
      if arr[j]>arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

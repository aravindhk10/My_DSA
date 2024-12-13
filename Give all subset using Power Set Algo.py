def power_set(arr):
  n = len(arr)
  ans = []
  for i in range(1<<n):
    temp = []
    for j in range(n):
      if (i&(1<<j)):
        temp.append(arr[j])
    ans.append(temp[:])
  return ans

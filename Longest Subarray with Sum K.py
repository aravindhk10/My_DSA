def longestSubarray(self, arr, k):
  dicc= {}
  cnt = 0
  s = 0
  for i in range(len(arr)):
    s += arr[i]
    if s not in dicc:
      dicc[s] = i
    if s == k:
      cnt = max(cnt, i+1)
    if (s-k) in dicc:
      cnt = max(cnt, i-dicc[s-k])
  return cnt

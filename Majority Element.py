def majorityElement(self, nums: List[int]) -> int:
  cnt = 0
  candidate = None
  for i in nums:
    if cnt == 0:
      cnt += 1
      candidate = i
    elif i == candidate:
      cnt += 1
    else:
      cnt -= 1
  return candidate

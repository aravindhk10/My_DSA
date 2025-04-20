def maxSubArray(self, nums: List[int]) -> int:
  maxx = 0
  summ = nums[0]
  for i in nums:
    maxx += i
    summ = max(summ, maxx)
    if maxx<0:
      maxx = 0
  return summ

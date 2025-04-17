class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
      # its an inplce solution so nothing to return
      i = 0
      for j in range(1, len(nums)):
        if nums[i] != 0:
          i+=1
        else:
          if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

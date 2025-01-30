class Solution:
    def findMin(self, nums: List[int]) -> int:
        x = nums[0]
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if (nums[low]<=nums[high]):
                x = min(x,nums[low])
            if nums[mid]>=nums[low]: 
                x = min(x,nums[low])
                low = mid + 1
            else:
                x = min(x,nums[mid])
                high = mid - 1
        return x

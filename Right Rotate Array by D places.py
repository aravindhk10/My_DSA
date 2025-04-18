class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        n = (len(nums)-k)
        temp = nums[n:]
        for i in range(n-1,-1,-1):
            nums[i+k] = nums[i]
        for i in range(k):
            nums[i] = temp[i]

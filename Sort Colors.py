class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic = {0:0,1:0,2:0}
        for i in nums:
            dic[i] += 1
        indx = 0
        for x in [0,1,2]:
            for i in range(dic[x]):
                nums[indx] = x
                indx+=1

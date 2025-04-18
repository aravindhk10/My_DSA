class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        temp = 0
        for j in nums:
            if  j == 1:
                temp += 1
                cnt = max(cnt, temp)
            else:
                temp = 0
        return cnt

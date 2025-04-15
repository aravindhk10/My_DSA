class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        ans = []
        for i in range(len(nums)):
            di[nums[i]] = i
        for j in range(len(nums)):
            if (target - nums[j]) in di:
                if di[target - nums[j]] != j:
                    ans.append(j)
                    ans.append(di[target - nums[j]])
                    return ans

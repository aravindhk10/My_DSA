class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def permutations(indx, nums, ans):
            if indx == len(nums):
                ans.append(nums[:])
                return
            for i in range(indx, len(nums)):
                nums[indx], nums[i] = nums[i], nums[indx]
                permutations(indx+1, nums, ans)
                nums[indx], nums[i] = nums[i], nums[indx]
            return ans
        return permutations(0, nums, ans)

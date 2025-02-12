class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        st = []
        ans = [-1]*len(nums1)
        for i in range(len(nums1)):
            m[nums1[i]] = i
        for i in range(len(nums2)):
            while st and nums2[i]>st[-1]:
                ans[m[st.pop()]] = nums2[i]
            if nums2[i] in m:
                st.append(nums2[i])
        return ans

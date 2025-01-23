class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        a = n//2
        b = (n//2)-1
        x = 0
        y = 0
        cnt = 0
        i = 0
        j = 0
        while (i<len(nums1) and j<len(nums2)):
            if nums1[i]<nums2[j]:
                if cnt==a:
                    x = nums1[i]
                if cnt==b:
                    y = nums1[i]
                cnt += 1
                i+=1
            else:
                if cnt==a:
                    x = nums2[j]
                if cnt==b:
                    y = nums2[j]
                cnt+=1
                j+=1
        while i<len(nums1):
            if cnt==a:
                x = nums1[i]
            if cnt==b:
                y = nums1[i]
            cnt += 1
            i+=1
        while j<len(nums2):
            if cnt==a:
                x = nums2[j]
            if cnt==b:
                y = nums2[j]
            cnt+=1
            j+=1
        if n%2==1:
            return x
        return (x+y)/2



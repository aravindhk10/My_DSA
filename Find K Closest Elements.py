class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = self.floor(arr, x)
        j = i+1
        ans = []
        while (k>0 and i>=0 and j<len(arr)):
            if (( x - arr[i] ) <= abs( x - arr[j] )):
                ans.append(arr[i])
                i-=1
            else:
                ans.append(arr[j])
                j+=1
            k-=1
        while (k>0 and i>=0):
            ans.append(arr[i])
            i-=1
            k-=1
        while (k>0 and j<len(arr)):
            ans.append(arr[j])
            j+=1
            k-=1
        return sorted(ans)

    def floor(self, arr, x):
        l = 0
        h = len(arr)-1
        ans = -1
        while l<=h:
            m = (l+h)//2
            if arr[m]==x:
                return m
            elif arr[m]<x:
                ans = m
                l = m + 1
            else:
                h = m - 1
        return ans                

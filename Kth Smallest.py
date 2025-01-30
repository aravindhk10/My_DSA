import heapq
class Solution:
    def kthSmallest(self, arr,k):
        ans = []
        for i in arr:
            heapq.heappush(ans,(-i,i))
            if len(ans)>k:
                heapq.heappop(ans)
        return ans[0][1]

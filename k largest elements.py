import heapq
class Solution:
	def kLargest(self,arr, k):
	    ans = []
	    temp = []
	    for i in arr:
	        heapq.heappush(ans,i)
	        if len(ans)>k:
	            heapq.heappop(ans)
	    while ans:
	        temp.append(heapq.heappop(ans))
	    temp.reverse()
      return temp

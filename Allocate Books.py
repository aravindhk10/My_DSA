class Solution:
	def books(self, A, B):
        low = max(A)
        high = sum(A)
        if len(A) < B:
            return -1
        while low<=high:
            mid = (low + high)//2
            if ((self.alloc(mid,A))>B):
                low = mid + 1
            else:
                high = mid - 1
        return low
    def alloc(self, mid, arr):
        stdnt = 1
        pgs = 0
        for i in range(len(arr)):
            if arr[i]+pgs <= mid:
                pgs += arr[i]
            else:
                stdnt += 1
                pgs = arr[i]
        return stdnt

class Solution:
    def median(self, mat):
    	def upperbound(arr, x, n):
    	    low = 0
    	    high = n-1
    	    ans = n
    	    while low<=high:
    	        mid = (low+high)//2
    	        if arr[mid]>x:
    	            ans = mid
    	            high = mid - 1
    	        else:
    	            low = mid + 1
    	    return ans
    	def smaller(mat,mid, m , n):
    	    count = 0
    	    for i in range(m):
    	        count += upperbound(mat[i], mid, n)
    	    return count
                
    	m = len(mat)
    	n = len(mat[0])
    	req = (m*n)//2
    	low = mat[0][0]
    	high = mat[0][0]
    	for i in range(m):
    	    low = min(low, mat[i][0])
    	    high = max(high, mat[i][n-1])
        while low<= high:
            mid = (low + high)//2
            count = smaller(mat,mid,m,n)
            if count <= req:
                low = mid + 1
            else:
                high = mid - 1
        return low
        

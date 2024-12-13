class Solution:
	def subsetSums(self, arr):
        n = len(arr)-1
        res = []
        s = 0
        def cal(arr, i, n, res, s):
            if i>n:
                res.append(s)
                return
            s+=arr[i]
            cal(arr, i+1, n, res, s)
            s-=arr[i]
            cal(arr, i+1, n, res, s)
            return res
        return cal(arr,0,n,res,s)

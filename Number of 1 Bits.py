class Solution:
	def setBits(self, n):
		# code here
		count = 0
		while n:
		    if  n&1==1:
		        count+=1
        n = n>>1
	  return count

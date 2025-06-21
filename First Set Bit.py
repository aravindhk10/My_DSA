class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        #Your code here
        cnt = 1
        while n:
            if n&1==1:
                return cnt
            n = n>>1
            cnt+=1

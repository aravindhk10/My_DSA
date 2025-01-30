class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        h = n
        while l<=h:
            m = (l+h)//2
            x = (m*(m+1))/2
            if x==n:
                return m
            elif x>n:
                h = m - 1
            else:
                l = m + 1
        return h

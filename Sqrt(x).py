class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        low = 1
        high = x
        while low<=high:
            mid = (low+high)//2
            sq = mid * mid
            if sq==x:
                return mid
            elif sq<x:
                low = mid + 1
            else:
                high = mid - 1
        return high

class Solution:
    def myPow(self, x: float, n: int) -> float:
        temp_n = n
        if n<0:
            temp_n = -1 * n
        s = 1
        while temp_n>0:
            if (temp_n%2==1):
                s = s * x
                temp_n-=1
            else:
                temp_n = temp_n//2
                x = x * x
        if n<0:
            return 1/s 
        return s
                

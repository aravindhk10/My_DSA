def NthRoot(n: int, m: int) -> int:
    low = 1
    high = m
    def solve(n,mid,m):
        s = 1
        for i in range(n):
            s*=mid
            if s>m:
                return 2
        if s==m:
            return 0
        else:
            return 1
        return s
    while low<=high:
        mid = (low+high)//2
        if (solve(n,mid,m)==0):
            return mid
        elif (solve(n,mid,m)==1):
            low = mid+1
        else:
            high = mid-1
    return -1

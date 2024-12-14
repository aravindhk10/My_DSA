class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        temp = []
        def cal(ind):
            if ind==n:
                ans.append(temp[:])
                return
            for i in range(ind, n):
                if (ispal(s,ind,i)):
                    temp.append(s[ind:i+1])
                    cal(i+1)
                    temp.pop()
            return ans
        def ispal(s,ind,i):
            while ind<i:
                if s[ind]!=s[i]:
                    return False
                ind+=1
                i-=1
            return True
        return cal(0)

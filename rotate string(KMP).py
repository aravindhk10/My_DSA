class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False
        lps = self.lpsarr(goal)
        i,j = 0,0
        s = s + s
        while i<len(s):
            if s[i] == goal[j]:
                i, j = i+1, j+1
            else:
                if j == 0:
                    i+=1
                else:
                    j = lps[j - 1]
            if j == len(goal):
                return True
        return False

    def lpsarr(self, goal):
        lps = [0] * len(goal)
        curr = 1
        prv = 0
        while curr<len(goal):
            if goal[curr]==goal[prv]:
                prv += 1
                lps[curr] = prv
                curr += 1
            else:
                if prv == 0:
                    lps[curr] = 0
                    curr+=1
                else:
                    prv = lps[prv - 1]
        return lps


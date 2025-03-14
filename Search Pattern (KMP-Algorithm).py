class Solution:
    def search(self, pat, txt):
        # code here
        ans = []
        lps = self.lpsarr(pat)
        i, j = 0, 0
        while i<len(txt):
            if txt[i] == pat[j]:
                i,j = i+1, j+1
            else:
                if j == 0:
                    i+=1
                else:
                    j = lps[j-1]
            if j == len(pat):
                ans.append(i - len(pat))
                j = lps[j-1]
        return ans
    def lpsarr(self, pat):
        lps = [0] * len(pat)
        curr = 1
        prv = 0
        while curr<len(pat):
            if pat[curr] == pat[prv]:
                prv += 1
                lps[curr] = prv
                curr += 1
            else:
                if prv == 0:
                    lps[curr] = 0
                    curr+=1
                else:
                    prv = lps[prv-1]
        return lps

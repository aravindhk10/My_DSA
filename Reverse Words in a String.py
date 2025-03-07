class Solution:
    def reverseWords(self, s: str) -> str:
        splited = s.split()
        i = 0
        j = len(splited)-1
        while i<=j:
            splited[i], splited[j] = splited[j], splited[i]
            i += 1
            j -= 1
        return " ".join(splited)

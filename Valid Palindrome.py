class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s =s.replace(" ","")
        i = 0
        j = len(s)-1
        while i<j:
            while i<j and s[i].isalnum()==False:
                i+=1
            while i<j and s[j].isalnum()==False:
                j-=1
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True

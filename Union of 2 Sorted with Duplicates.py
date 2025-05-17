class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here
        i = 0
        j = 0
        union = []
        while i<len(a) and j<len(b):
            if a[i]<=b[j]:
                if len(union) == 0 or union[-1] != a[i]:
                    union.append(a[i])
                i+=1
            else:
                if len(union) == 0 or union[-1] != b[j]:
                    union.append(b[j])
                j+=1
        while i<len(a):
            if union[-1] != a[i]:
                union.append(a[i])
            i+=1
        while j<len(b):
            if union[-1] != b[j]:
                union.append(b[j])
            j+=1
        return union

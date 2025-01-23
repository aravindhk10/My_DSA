class Solution:
    def kthElement(self, a, b, k):
        i = 0
        j = 0
        cnt = 0
        k = k-1
        while(i<len(a) and j<len(b)):
            if(a[i]<b[j]):
                if (cnt == k):
                    return a[i]
                cnt+=1
                i+=1
            else:
                if (cnt == k):
                    return b[j]
                cnt+=1
                j+=1
        while(i<len(a)):
            if (cnt == k):
                return a[i]
            cnt+=1
            i+=1
        while(j<len(b)):
            if (cnt == k):
                return b[j]
            cnt+=1
            j+=1

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        d = d % len(arr)
        temp = arr[:d]
        for i in range(d, len(arr)):
            arr[i-d] = arr[i]
        for j in range(len(arr)-d,len(arr)):
            arr[j] = temp[j-(len(arr)-d)]
        return arr

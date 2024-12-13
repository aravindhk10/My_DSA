def mergesort(arr, low, high):
    if low>=high:
        return
    mid = (low+high)//2
    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)
    merge(arr, low,mid, high)
    return arr

def merge(arr, low, mid, high):
    l = low
    r = mid+1
    new = []
    while l<=mid and r<=high:
        if arr[l]<=arr[r]:
            new.append(arr[l])
            l+=1
        else:
            new.append(arr[r])
            r+=1
    while l<=mid:
        new.append(arr[l])
        l+=1
    while r<=high:
        new.append(arr[r])
        r+=1
    for i in range(low,high+1):
        arr[i] = new[i-low]
    return arr

def ma():
    arr= [7,9,3,8,56,1,2,5,6,1,2,3]
    n = len(arr)
    print(mergesort(arr,0,n-1))
ma()

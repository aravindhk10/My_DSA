def quick(arr, low, high):
    if low<high:
        p = part(arr, low , high)
        quick(arr, low, p-1)
        quick(arr, p+1, high)
    return arr
def part(arr, low, high):
    l = low
    r = high
    pivot = arr[low]
    while l<=r:
        while arr[l]<=pivot and l<=high-1:
            l+=1
        while arr[r]>pivot and r>=low+1:
            r-=1
        if l<r:
            arr[l], arr[r] = arr[r], arr[l]
    arr[r], arr[low] = arr[low], arr[r]
    return r

a = [7,2,9,8,2,3,0]
n = (len(a)-1)
print(quick(a,0,n))

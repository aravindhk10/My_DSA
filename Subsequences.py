def cnt(arr,new, i, n):
    if i==n:
        print(new)
        return
    new.append(arr[i])
    cnt(arr, new, i+1, n)
    new.pop()
    cnt(arr, new, i + 1, n)
def a ():
    arr = [2,3,6,7]
    new = []
    n = len(arr)-1
    cnt(arr,new, 0, n)
a()


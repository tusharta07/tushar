#find nth largest number
def l(arr):
    n = len(arr)
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return(max)

def nthl(arr):
    m = len(arr)
    nthmax = arr[0]
    for j in range(p-1):
        temp=l(arr)
        arr.remove(temp)

    nthmax=l(arr)
    return(nthmax)

arr= [int(k) for k in input().split()]
p=int(input("nth largest position: "))
ans=nthl(arr)
print("nth largest in given array is", ans)
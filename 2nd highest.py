def secondl(arr):
    n = len(arr)
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    arr.remove(max)
    max2 = arr[0]
    for j in range(n-1):
        if arr[j] > max2:
            max2 = arr[j]

    return(max2)


arr= [int(k) for k in input().split()]
ans=secondl(arr)
print("2nd largest in given array is", ans)
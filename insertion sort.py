def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr= [int(k) for k in input().split()]
selection_sort(arr)
print(arr)
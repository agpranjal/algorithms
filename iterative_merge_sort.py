def merge(arr, LB, mid, UB):
    C = [None]*(UB-LB+1)
    i = LB
    j = mid+1
    k = 0

    while i <= mid and j <= UB:
        if arr[i] < arr[j]:
            C[k] = arr[i]
            i += 1
        else:
            C[k] = arr[j]
            j += 1
        k += 1
    
    while i <= mid:
        C[k] = arr[i]
        i += 1
        k += 1

    while j <= UB:
        C[k] = arr[j]
        j += 1
        k += 1

    for i in range(len(C)):
        arr[LB+i] = C[i]

def merge_sort(arr, LB, UB):
    p = 2
    while p <= len(arr):
        i = 0
        while i+p-1 < len(arr):
            mid = (i+i+p-1)//2
            merge(arr, i, mid, i+p-1)
            i += p

        p *= 2
    
    if p//2 < len(arr):
        merge(arr, 0, p//2-1, len(arr)-1)

arr = [8, 3, 7, 4, 9, 2, 6, 5, 1, 2.5, 3.8, 2.5]
merge_sort(arr, 0, len(arr)-1)
print(arr)

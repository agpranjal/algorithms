def merge(arr, LB, UB):
    C = [None]*(UB-LB+1)
    mid = (LB+UB)//2
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
    if LB >= UB:
        return

    merge_sort(arr, LB, (LB+UB)//2)
    merge_sort(arr, (LB+UB)//2+1, UB)
    merge(arr, LB, UB)

arr = [8, 3, 7, 4, 9, 2, 6, 5, 1, 2.5, 3.8]
merge_sort(arr, 0, len(arr)-1)
print(arr)

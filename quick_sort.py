def partition(arr, i, j):
    pivot = i

    while i < j:
        while i < len(arr) and arr[i] <= arr[pivot]:
            i += 1
        while arr[j] > arr[pivot]:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[j], arr[pivot] = arr[pivot], arr[j]
    return j
    

def quick_sort(arr, LB, UB):
    if LB <= UB:
        j = partition(arr, LB, UB)
        quick_sort(arr, LB, j-1)
        quick_sort(arr, j+1, UB)

#arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]
arr = [-1, 2, -8, -10]
quick_sort(arr, 0, len(arr)-1)
print(arr)

def solve(arr, target, ls=[], SUM=0, index=0):
    if SUM == target:
        print(ls)
        return

    if index == len(arr):
        return

    if SUM+arr[index] <= target:
        solve(arr, target, ls+[arr[index]], SUM+arr[index], index+1)
        solve(arr, target, ls, SUM, index+1)

arr = [5, 10, 12, 13, 15, 18]
arr.sort()
solve(arr, 30)

def solve(arr):
    SUM = arr[0]
    ans = arr[0]

    for i in range(1, len(arr)):
        SUM = max(SUM+arr[i], arr[i])
        ans = max(SUM, ans)

    return ans

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(solve(arr))


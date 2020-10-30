def solve(profits, weights, W, N):
    # find the max profit we can get
    # with a max weight of W
    
    dp = []
    selected = [0]*N
    for i in range(N+1):
        dp.append([0]*(W+1))
    
    for i in range(1, N+1):
        for j in range(1, W+1):
            if j < weights[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
               # if j-weights[i-1] < 0:
               #     dp[i][j] = max(profits[i-1], dp[i-1][j])
               # else:
                dp[i][j] = max(profits[i-1]+dp[i-1][j-weights[i-1]], dp[i-1][j])

    for i in range(len(dp)):
        for j in range(len(dp[i])):
            print(dp[i][j], end=" ")
        print()

    i = N
    j = W
    while i > 0 and j > 0:
        if dp[i][j] > dp[i-1][j]:
            selected[i-1] = 1
            j -= weights[i-1]
            i -= 1
        else:
            i -= 1
    
    print(selected)
    
    return dp[N][W]

profits = [10, 15, 40]
weights = [1, 2, 3]
W = 6
print(solve(profits, weights, W, len(profits)))

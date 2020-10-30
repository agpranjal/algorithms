def solve(profits, weights, m):
    ratio = []
    ans = 0

    for i in range(len(profits)):
        ratio.append([profits[i]/weights[i], i])
    
    ratio.sort(reverse=True)

    for i in range(len(ratio)):
        index = ratio[i][1]
        p = profits[index]
        w = weights[index]
        
        if m-w < 0:
            ans += m/w*p
        else:
            m -= w
            ans += p

    return ans

profits = [10, 5, 15, 7, 6, 18, 3]
weights = [2, 3, 5, 7, 1, 4, 1]
m = 15

print(solve(profits, weights, m))

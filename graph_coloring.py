def solve(G, m, u):
    
    if u == len(G):
        print(colored)
        return

    for i in range(1, m+1):
        flag = True
        for j in range(len(G)):
            if G[u][j] == 1 and colored[j] == i:
                flag = False
                break

        if flag:
            colored[u] = i
            solve(G, m, u+1)
            colored[u] = -1

G = [
        [0,1,0,1],
        [1,0,1,0],
        [0,1,0,1],
        [1,0,1,0]
    ]

colored = [-1]*len(G)
solve(G, 3, 0)

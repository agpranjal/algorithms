inf = 2**31-1

def all_pairs_shortest_path():
    for k in range(len(G)):
        for i in range(len(G)):
            for j in range(len(G)):
                G[i][j] = min(G[i][j], G[i][k]+G[k][j])
    
    for i in range(len(G)):
        print(G[i])

def dijkstras(s, t):
    # find the shortest edge from source
    visited = set()
    cost = [inf]*len(G)
    path = [0]*len(G)

    MIN = inf
    for i in range(len(G)):
        if G[s][i] < MIN:
            MIN = G[s][i]
            u = i
    
    visited.add(s)
    path[u] = s
    
    # set the initial cost
    for i in range(len(G)):
        cost[i] = G[s][i]

    cost[s] = 0

    while len(visited) != len(G):
        # relaxation
        for i in range(len(G)):
            if G[u][i]+cost[u] < cost[i]:
                cost[i] = G[u][i]+cost[u]
                path[i] = u
        
        MIN = inf
        for i in range(len(cost)):
            if cost[i] < MIN and i not in visited:
                MIN = cost[i]
                v = i
        
        visited.add(u)
        u = v
    
    output = [t]

    while t != 0:
        output.append(path[t])
        t = path[t]

    print(output[::-1])

def weighted_union(s, u, v):
    if s[u] > s[v]:
        u, v = v, u

    s[u] += s[v]
    s[v] = u

def find(s, u):
    x = u
    while s[x] > 0:
        x = s[x]
    return x

def kruskalsMST():
    s = [-1]*len(G)
    t = []

    while len(t) < len(G)-1:
        MIN = 2**31-1

        # find the min cost edge
        for i in range(len(G)):
            for j in range(i, len(G)):
                if G[i][j] < MIN and [i,j] not in t:
                    x = find(s, i)
                    y = find(s, j)

                    if (x == -1 and y == -1) or (x != y):
                        MIN = G[i][j]
                        u = i
                        v = j
        
        # add the selected edge
        t.append([u,v])
        weighted_union(s, u, v)

    print(t)
    cost = 0
    for i in range(len(t)):
        cost += G[t[i][0]][t[i][1]]
    print(f"MST Total cost: {cost}")

def bfs(u):
    global visited
    queue = [u]

    while queue:
        u = queue.pop(0)

        for v in range(len(G)):
            if G[u][v] != inf and visited[v] != 1:
                print(v, end=" ")
                visited[v] = 1
                queue.append(v)


def dfs(u):
    global visited
    visited[u] = 1
    print(u, end=" ")

    for v in range(len(G)):
        if G[u][v] != inf and visited[v] != 1:
            dfs(v)

def display():
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != inf:
                print("{} -> {} | ".format(i,j), end=" ")
        
        print()

G = [[inf, 4, inf, inf, inf, inf, inf, 8, inf], 
        [4, inf, 8, inf, inf, inf, inf, 11, inf], 
        [inf, 8, inf, 7, inf, 4, inf, inf, 2], 
        [inf, inf, 7, inf, 9, 14, inf, inf, inf], 
        [inf, inf, inf, 9, inf, 10, inf, inf, inf], 
        [inf, inf, 4, 14, 10, inf, 2, inf, inf], 
        [inf, inf, inf, inf, inf, 2, inf, 1, 6], 
        [8, 11, inf, inf, inf, inf, 1, inf, 7], 
        [inf, inf, 2, inf, inf, inf, 6, 7, inf] 
        ] 

visited = [0]*len(G)

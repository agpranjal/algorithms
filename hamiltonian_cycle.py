def solve(G, index=1):
    global vertex
    
    if index == len(G):
        if G[vertex[index-1]][vertex[0]]:
            print(vertex)
        return

    for i in range(len(G)):
        if i not in vertex[:index+1] and G[vertex[index-1]][i]:
            vertex[index] = i
            solve(G, index+1)
    
G = [
        [0, 1, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0]
    ]

vertex = [-1]*len(G)
vertex[0] = 0
solve(G)

def dijkstra(G, source, target):
    real_source = source
    visited = set()
    visited.add(source)

    distance = [INFINITY]*len(G)
    distance[source] = 0

    paths = {}


    while len(visited) != len(G):

        # do relaxation
        for i in range(len(G)):
            if G[source][i] > 0 and i != source:
                if G[source][i]+distance[source] < distance[i]:
                    distance[i] = G[source][i]+distance[source]
                


        MIN = INFINITY
        u = real_source
        for i in range(len(distance)):
            if i != real_source and i not in visited:
                if distance[i] < MIN:
                    MIN = distance[i]
                    u = i

                    if i in paths:
                        paths[i].append(source)
                    else:
                        paths[i] = [source]

        visited.add(source)
        print(visited)
        source = u

    print(distance)
    print(paths[target])



G = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 

INFINITY = 2**31-1
dijkstra(G, 0, 3)

def is_safe(G, i, j, color, visited):
    return i >= 0 and i < len(G) and j >= 0 and j < len(G[0]) and (i,j) not in visited and G[i][j] == color

def solve(G, i, j, count, color, visited):

    hashmap[color] = max(hashmap[color], count)

    visited.add((i, j))

    if is_safe(G, i-1, j, color, visited):
        solve(G, i-1, j, count+1, color, visited)

    if is_safe(G, i+1, j, color, visited):
        solve(G, i+1, j, count+1, color, visited)

    if is_safe(G, i, j+1, color, visited):
        solve(G, i, j+1, count+1, color, visited)

    if is_safe(G, i, j-1, color, visited):
        solve(G, i, j-1, count+1, color, visited)

G = [
        ["G","G","B","R"],
        ["G","G","G","G"],
        ["R","R","G","G"]
    ]

hashmap = {}

for i in range(len(G)):
    for j in range(len(G[i])):
        hashmap[G[i][j]] = 0

for i in range(len(G)):
    for j in range(len(G[i])):
        solve(G, i, j, 1, G[i][j], set())

print(hashmap)

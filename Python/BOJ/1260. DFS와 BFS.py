def dfs(k):
    global dfs_visited
    dfs_visited.append(k)
    for i in range(len(check[k])):
        if check[k][i] == 1:
            if i not in dfs_visited:
                dfs(i)

def bfs(k):
    global bfs_visited
    queue = [k]
    while queue:
        start = queue.pop(0)
        if start not in bfs_visited:
            bfs_visited.append(start)
        for j in range(len(check[start])):
            if check[start][j] == 1:
                if j not in bfs_visited:
                    queue.append(j)

n, m, v = map(int, input().split())
check = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    check[a][b] = check[b][a] = 1

dfs_visited = []
bfs_visited = []

dfs(v)
bfs(v)

for i in range(len(dfs_visited)):
    print(dfs_visited[i], end=' ')
print()
for i in range(len(bfs_visited)):
    print(bfs_visited[i], end=' ')
print()
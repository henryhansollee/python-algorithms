def dfs(k):
    global visited_dfs
    visited_dfs.append(k)
    for i in range(len(check[k])):
        if check[k][i] == 1:
            if i not in visited_dfs:
                dfs(i)

def bfs(k):
    global visited_bfs
    queue = [k]
    while queue:
        start = queue.pop(0)
        if start not in visited_bfs:
            visited_bfs.append(start)
        for i in range(len(check[k])):
            if check[start][i] == 1:
                if i not in visited_bfs:
                    queue.append(i)

n = int(input())
m = int(input())
check = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    check[a][b] = check[b][a] = 1

visited_dfs = []
visited_bfs = []

dfs(1)
bfs(1)

ans_dfs = 0
for computer in visited_dfs:
    if computer != 1:
        ans_dfs += 1
print(ans_dfs)

ans_bfs = 0
for computer in visited_bfs:
    if computer != 1:
        ans_bfs += 1
print(ans_bfs)
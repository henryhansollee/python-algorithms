dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start):
    global lists, check, cnt, n, m , k
    queue = [start]
    check[start[0]][start[1]] = cnt
    while queue:
        r, c = queue.pop(0)
        for z in range(4):
            nr, nc = r + dr[z], c + dc[z]
            if 0 <= nr < n and 0 <= nc < m:
                if check[nr][nc] == 0:
                    if lists[nr][nc] == 1:
                        queue.append((nr, nc))
                        check[nr][nc] = cnt

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    lists = [[0] * m for _ in range(n)]
    check = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        lists[b][a] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if lists[i][j] == 1:
                if check[i][j] == 0:
                    cnt += 1
                    bfs((i, j))

    print(cnt)
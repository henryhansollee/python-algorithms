dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start):
    global check, lists, n, cnt
    queue = [start]
    check[start[0]][start[1]] = cnt
    while queue:
        r, c = queue.pop(0)
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if check[nr][nc] == 0:
                    if lists[nr][nc] == 1:
                        queue.append((nr, nc))
                        check[nr][nc] = cnt

n = int(input())
lists = [list(map(int, input())) for _ in range(n)]
check = [[0] * n for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if lists[i][j] == 1:
            if check[i][j] == 0:
                cnt += 1
                bfs((i, j))

ans_list = [0] * (cnt+1)
for i in range(1, cnt+1):
    for a in range(n):
        for b in range(n):
            if check[a][b] == i:
                ans_list[i] += 1

ans_list.sort()
ans_list[0] = cnt
for ans in ans_list:
    print(ans)
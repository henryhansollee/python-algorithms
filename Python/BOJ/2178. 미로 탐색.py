dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start):
    global n, m, lists, check, end_r, end_c, ans
    queue = [start]
    while queue:
        r, c = queue.pop(0)
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < m:
                if check[nr][nc] == 0:
                    if lists[nr][nc] == 1:
                        check[nr][nc] += check[r][c] + 1
                        queue.append((nr, nc))

n, m = map(int, input().split())
lists = [list(map(int, input())) for _ in range(n)]
check = [[0] * m for _ in range(n)]
start_r, start_c = 0, 0
end_r, end_c = n-1, m-1

check[start_r][start_c] = 1

bfs((start_r, start_c))

print(check[end_r][end_c])
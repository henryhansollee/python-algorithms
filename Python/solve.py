import sys
sys.stdin = open('input.txt', 'r')

# 1: 사람
# 2이상: 계단의 입구이자 계단의 길이

# 계단의 입구는 반드시 2개이며 서로 겹치지 않음
# 초기 입력으로 주어지는 사람의 위치와 계단 입구의 위치는 겹치지 않음

# 1. 계단 입구까지 이동 시간
# 이동 시간(분) = | PR - SR | + | PC - SC |
# PR, PC : 사람 P의 세로위치, 가로위치, SR, SC : 계단 입구 S의 세로위치, 가로위치

# 2. 계단을 내려가는 시간
# 계단을 내려가는 시간은 계단 입구에 도착한 후부터 계단을 완전히 내려갈 때까지의 시간이다.
# 계단 입구에 도착하면, 1분 후 아래칸으로 내려 갈 수 있다.
# 계단 위에는 동시에 최대 3명까지만 올라가 있을 수 있다.
# 이미 계단을 3명이 내려가고 있는 경우, 그 중 한 명이 계단을 완전히 내려갈 때까지 계단 입구에서 대기해야 한다.
# 계단마다 길이 K가 주어지며, 계단에 올라간 후 완전히 내려가는데 K 분이 걸린다.

# 모든 사람들이 계단을 내려가 이동이 완료되는 시간이 최소가 되는 경우를 찾고,
# 그 때의 소요시간을 출력하는 프로그램을 작성하라.

# ----------

# Brute force
# Queue

# 1. 계단의 위치와 길이를 파악(계단의 입구는 반드시 2개)
# 2. 사람의 위치 파악
# 3. 계단과 사람 순열로 짝짓기

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    # 1. 계단의 위치와 길이를 파악(계단의 입구는 반드시 2개)
    # 2. 사람의 위치 파악
    stairs = []     # (x, y, 길이)
    people = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                people.append((i, j))
            elif board[i][j] >= 2:
                stairs.append((i, j, board[i][j]))
    print(stairs)
    print(people)

    # 3. 계단과 사람 순열로 짝짓기






    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
    print()
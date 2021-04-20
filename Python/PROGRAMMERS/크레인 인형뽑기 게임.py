def solution(board, moves):
    answer = 0

    stack = [-1]

    cnt = 0

    for m in moves:
        for j in range(len(board)):
            if board[j][m - 1] > 0:
                if stack[-1] != board[j][m - 1]:
                    stack.append(board[j][m - 1])
                else:
                    stack.pop()
                    cnt += 1
                board[j][m - 1] = 0
                break

    answer = cnt * 2

    return answer
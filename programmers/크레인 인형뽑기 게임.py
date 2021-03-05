board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0

    #####

    # print(board, moves)
    temp = []
    for i in range(len(moves)):
        # print(moves[i])
        for j in range(len(board)):
            if board[j][moves[i]-1]:
                board[j][moves[i] - 1] = 0
                if temp:
                    if temp[-1] == board[j][moves[i]-1]:
                        temp.pop()
                    else:
                        temp.append(board[j][moves[i]-1])

                else:
                    temp.append(board[j][moves[i]-1])
            else:
                break
    print(temp)

    #####

    return answer

solution(board, moves)
import sys
input = sys.stdin.readline
def chess_board(x, y, standard_board):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if board[x+i][y+j] != standard_board[x+i][y+j]:
                cnt += 1
    return cnt




N, M = map(int, input().split())

board = [list(map(str, input().strip())) for _ in range(N)]

w_board = [['W' if (i + j) % 2 == 0 else 'B' for j in range(M)] for i in range(N)]
b_board = [['B' if (i + j) % 2 == 0 else 'W' for j in range(M)] for i in range(N)]

ans = 9999
for i in range(N-7):
    for j in range(M-7):
        ans = min(ans, chess_board(i, j, b_board), chess_board(i, j, w_board))

print(ans)

# 일단 B로 시작하는, W로 시작하는 보드판을 하나씩 만들고
# 제작한 보드판과 입력받은 보드판을 비교해서 다른 만큼 카운팅 더 작은 보드 카운트를 리턴
move_dict = {
    "R": (1,0),
    "L": (-1,0),
    "B": (0,-1),
    "T": (0,1),
    "RT": (1, 1),
    "LT": (-1, 1),
    "RB": (1, -1),
    "LB": (-1, -1)
}

def to_xy(pos): #문자열을 좌표값으로 변환
    x, y = pos.strip()
    x2 = ord(x) - ord('A') + 1
    y2 = int(y)
    return x2, y2

def to_pos(x, y): #좌표값을 반환용 문자열로 변환
    return chr(x + ord('A') - 1) + str(y)

def king_pos(king_x, king_y, stone_x, stone_y, pos):
    dx, dy = move_dict[pos]
    nx, ny =  king_x + dx, king_y + dy
    if not (1 <= nx <= 8 and 1 <= ny <= 8):
        return king_x, king_y, stone_x, stone_y

    # 돌과 부딪히면
    if nx == stone_x and ny == stone_y:
        sx, sy = stone_x + dx, stone_y + dy
        if not (1 <= sx <= 8 and 1 <= sy <= 8):
            return king_x, king_y, stone_x, stone_y  # 돌이 밖으로 나가면 무시
        return nx, ny, sx, sy
    else:
        return nx, ny, stone_x, stone_y



king, stone, N = map(str, input().split())


king_x, king_y = to_xy(king)
stone_x, stone_y = to_xy(stone)

pos = []
N = int(N)
for _ in range(N):
    t = input()
    pos.append(t)

for i in range(N):
    king_x, king_y, stone_x, stone_y = king_pos(king_x, king_y, stone_x, stone_y, pos[i])

k = to_pos(king_x, king_y)
s = to_pos(stone_x, stone_y)

print(k)
print(s)





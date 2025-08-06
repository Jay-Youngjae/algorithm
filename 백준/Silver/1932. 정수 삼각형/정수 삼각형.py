import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = []
dp = []

for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
    dp.append([-1] * (i + 1))


def go(i, j):
    if i == n - 1:
        return graph[i][j]

    if dp[i][j] != -1:
        return dp[i][j]

    left = go(i + 1, j)
    right = go(i + 1, j + 1)

    dp[i][j] = graph[i][j] + max(left, right)
    return dp[i][j]


print(go(0, 0))

# n = int(input())
# 
# triangle = [list(map(int, input().split())) for _ in range(n)]
# 
# # triangle을 dp로 바로 씀 (in-place)
# for i in range(n-2, -1, -1):
#     for j in range(len(triangle[i])):
#         triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
# 
# print(triangle[0][0])

import sys
input = sys.stdin.readline

N = int(input())
score = list(map(int, input().split()))

max_score = max(score)

for i in range(N):
    score[i] = (score[i] * 100) /max_score

avg_score = sum(score) / N
print(avg_score)

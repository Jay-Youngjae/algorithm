N = int(input())
scores = []
for _ in range(N):
    t = int(input())
    scores.append(t)

cnt = 0
for i in range(N-1, 0, -1):
    if scores[i-1] >= scores[i]:
        cnt += scores[i-1] - (scores[i] -1)
        scores[i-1] = scores[i]-1
print(cnt)
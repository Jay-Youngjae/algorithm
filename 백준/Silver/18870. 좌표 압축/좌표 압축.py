N = int(input())
X = list(map(int, input().split()))

Xi = []
sorted_X = sorted(X)
set_X = list(set(sorted_X))
set_X.sort()
for i in range(len(set_X)):
    Xi.append(i)
    
mapping = dict(zip(set_X, Xi)) #zip은 두 쌍을 튜플로 묶는다 여기선 (set_X, Xi)꼴의 튜플이 된다
ans = []
for i in X:
    ans.append(mapping[i])

print(*ans)
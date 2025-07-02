n, k = map(int, input().split())

arr = list(map(int, input().split())) #3 -2 -4 -9 0 3 7 13 8 -3

prefix = [0 for _ in range(n+1)]

for i in range(n):
    prefix[i+1] = prefix[i]+arr[i]  #0 3 1 -3 -12 -12 -9 -2 11 19 16

answer=[]
for i in range(k, n+1):
    answer.append(prefix[i]-prefix[i-k])
print(max(answer))
    


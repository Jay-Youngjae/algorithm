N = int(input())
M = int(input())

numbers = list(map(int, input().split()))

numbers.sort()

start = 0
end = N - 1
cnt = 0
# 1 2 3 4 5 7
while numbers[end] > numbers[start]:
    if numbers[start] + numbers[end] == M:
        cnt += 1
        start += 1
        end -= 1
    elif numbers[start] + numbers[end] > M:
        end -= 1
    elif numbers[start] + numbers[end] < M:
        start += 1

print(cnt)
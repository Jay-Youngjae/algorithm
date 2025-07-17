import sys
input = sys.stdin.readline

N = int(input())

people = [list(map(str, input().split())) for _ in range(N)]


for i in range(N):
    people[i][0] = int(people[i][0])
    people[i].append(i)

people.sort(key = lambda x:(x[0], x[2]))

for i in range(N):
    people[i].pop()


for i in range(N):
    print(*people[i])
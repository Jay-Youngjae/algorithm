import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())

cards = list(map(int, input().split()))

max_combi = 0
for i in combinations(cards, 3):
    s=sum(i)
    if s <= M:
        max_combi = max(max_combi, s)

print(max_combi)
N = int(input())
lst = []

for i in range(N):
    s = input()
    lst.append(s)
    
lst=list(set(lst))
lst.sort(key = lambda x:(len(x),x))


for i in lst:
    print(i)

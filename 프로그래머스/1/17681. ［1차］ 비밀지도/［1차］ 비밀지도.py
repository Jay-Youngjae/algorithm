def solution(n, arr1, arr2):
    def to_bin(arr, n, m):
        for i in range(n):
            s = bin(arr[i])[2:]
            if len(s) < n:
                padding = n - len(s)
                s = "0" * padding + s
            m.append(s)
        return m
    
    map1 = []
    map2 = []
    answer = []
    m1 = to_bin(arr1, n, map1)
    m2 = to_bin(arr2, n, map2)
    print(m1)
    for i in range(n):
        row = ""
        for j in range(n):
            if int(m1[i][j])|int(m2[i][j]) == 1:
                row += "#"
            else:
                row += " "
        answer.append(row)
    
    return answer
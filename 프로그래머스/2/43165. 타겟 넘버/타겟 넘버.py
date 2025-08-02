def solution(numbers, target):
    def dfs(idx, number_sum, numbers, target):
        if idx == len(numbers): #인덱스가 재귀의 끝까지 도달했다면
            if number_sum == target: # 목표 점수 도달 => +1
                return 1
            else:
                return 0 #아니면 + 0
        return (dfs(idx + 1, number_sum + numbers[idx], numbers, target) + dfs(idx + 1, number_sum - numbers[idx], numbers, target))
        #트리 구조를 떠올렸을 때 각 노드로부터 각각의 number가 +였을 때의 결과와 -였을 때의 결과를 합쳐서 return해야 되기 때문에 +
    
    answer = dfs(0, 0, numbers, target)
    return answer

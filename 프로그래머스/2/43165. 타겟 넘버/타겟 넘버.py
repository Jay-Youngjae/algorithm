def solution(numbers, target):
    def dfs(idx, number_sum, numbers, target):
        if idx == len(numbers): #인덱스가 재귀의 끝까지 도달했다면
            if number_sum == target: 
                return 1
            else:
                return 0
        return (dfs(idx + 1, number_sum + numbers[idx], numbers, target) + dfs(idx + 1, number_sum - numbers[idx], numbers, target))
        
    
    answer = dfs(0, 0, numbers, target)
    return answer

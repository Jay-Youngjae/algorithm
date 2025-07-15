from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque(progresses) 
    s_queue = deque(speeds)
    cnt = 0
    while (len(queue) > 0):
        for i in range(len(queue)):
            queue[i] += s_queue[i]
        cnt = 0
        while queue and queue[0] >= 100:
            queue.popleft()
            s_queue.popleft()
            cnt += 1
        if cnt > 0:
            answer.append(cnt)
    return answer



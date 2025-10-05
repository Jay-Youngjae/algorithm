from collections import deque
def solution(s):
    n = len(s)
    result = 0
    # 길이가 홀수면 애초에 불가능
    if n % 2 != 0:
        return 0

    s = deque(s)

    for _ in range(n):
        stack = []
        ok = True
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack:
                    ok = False
                    break
                top = stack[-1]
                if (top == '(' and ch == ')') or (top == '[' and ch == ']') or (top == '{' and ch == '}'):
                    stack.pop()
                else:
                    ok = False
                    break

        if ok and not stack:
            result += 1

        tmp = s.popleft()
        s.append(tmp)

    return result

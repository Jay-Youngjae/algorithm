def _gcd(a, b):
    while a%b!=0:
        tmp = a%b
        a = b
        b = tmp
    return b

def _lcm(a, b):
    return a*b//_gcd(a, b)

def find_numbers(a, b):
    target = a * b
    result = (0, 0)
    min_sum = float('inf')
    for x in range(a, int(target**0.5)+1, a):
        if target % x == 0:
            y = target // x
            if _gcd(x, y) == a:
                if x + y < min_sum:
                    min_sum = x + y
                    result = (x, y)
    print(result[0], result[1])

a, b = map(int, input().split())
find_numbers(a, b)

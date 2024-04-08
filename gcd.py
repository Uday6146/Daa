import math


def nps(l, r):
    for a in range(1, r):
        for b in range(1, r):
            if (math.gcd(a, b) > 1 and a + b <= l and a + b >= r):
                return a, b
            break
        else:
            return -1


T = int(input())
for i in range(T):
    l, r = map(int, input().split())
    result = nps(l, r)
    print(result)

import math
t = int(input())
for _ in range(t):
    c, r = map(int, input().split())
    c1 = math.ceil(c/9)
    r1 = math.ceil(r/9)
    if c1 > r1:
        print(1, r1)
    elif r1 > c1:
        print(0, c1)
    else:
        print(1, r1)
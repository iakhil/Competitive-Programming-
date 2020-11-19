t = int(input())
for _ in range(t):
    
    def count_time(n, k, tim, l):
        if l != 1:
            tim += min(n, k)
            diff = abs(n - k)
            return diff, tim
        else:
            tim += max(n, k)
            diff = abs(n - k)
            return diff, tim

    n = int(input())
    C = list(map(int, input().split()))
    if n == 1:
        print(C[0])
    
    elif(all(ele == C[0] for ele in C)):
        if n % 2 == 0:
            print(int(C[0] * n/2))
        else:
            k = n // 2 
            print(int(C[0] * k + C[1]))
    else:
        
        C.sort(reverse = True)
        diff = C[0]
        tim = 0
        C.pop(0)
        while len(C) != 0:
            m = len(C)
            diff, tim = count_time(diff, C[0], tim, m)
            m = C[0]
            C.pop(0)
            count_time(diff, m, tim, m)
        print(tim)   
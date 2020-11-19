t = int(input())
for _ in range(t):
    n, k, x, y = map(int, input().split())
    affected = [x]
    if(x == y):
        print("YES")
    else:
        curr = x
        while True:
            city = (curr + k) % n 
            if(city in affected):
                print("NO")
                break
            elif city == y:
                print("YES")
                break
            else:
                affected.append(city)
                curr = city
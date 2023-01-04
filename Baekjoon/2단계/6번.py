H, M = map(int, input().split())
T = int(input())

if (M + T) > 60:
    if (M+T-60) >= 60:
        print(H+2, M+T-120)
    else:
        print(H+1, M+T-60)
else:
    print(H, M+T)

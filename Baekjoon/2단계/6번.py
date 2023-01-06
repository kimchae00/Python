H, M = map(int, input().split())
T = int(input())

hour = (M+T)//60
min = (M+T)%60

if hour < 0:
    print(H, min)
else:
    if H+hour >= 24:
        print((H+hour)%24, min)
    else:    
        print(H+hour, min)
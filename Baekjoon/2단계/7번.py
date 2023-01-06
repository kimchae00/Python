a, b, c = map(int, input().split())

list = [a, b, c]
n = max(list)

if a == b == c:
    print((a*1000)+10000)
elif a == b and b != c:
    print((a*100)+1000)
elif b == c and b != a:
    print((b*100)+1000)
elif a == c and a != b:
    print((a*100)+1000)
else:
    print(n*100)
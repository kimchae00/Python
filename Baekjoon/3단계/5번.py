import sys
t = int(sys.stdin.readline()) # input 대신 sys.stdin.readlined을 사용하면 시간 단축

for i in range(t):
    a, b = map(int, input().split())
    print(a + b)
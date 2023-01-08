n = int(input())

if n >= 1 and n <= 9:
    for i in range(1, 10):
        print(n, '*', i, '=', n*i)
        
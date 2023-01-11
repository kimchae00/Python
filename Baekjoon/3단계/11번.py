while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except EOFError: # 런타임에러 예외처리
        break
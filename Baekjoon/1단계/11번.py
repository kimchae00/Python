# n1, n2 = map(int, input().split())을 사용하니 런타임에러(ValueError)가 떴음.
n1 = int(input())
n2 = int(input())

n3 = n1*(n2%10)
n4 = n1*(((n2%100)-(n2%10))//10)
n5 = n1*(n2//100)
n6 = n1*n2

print(n3)
print(n4)
print(n5)
print(n6)
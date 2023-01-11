"""  
날짜 : 2023/01/11
이름 : 김채영
내용 : 파이썬 클래스 실습하기
"""
from sub1.Car import Car
from sub1.Account import Account

# 객체 실습
bmw = Car('BMW', '검정색', 5000)
bmw.speedUp()
bmw.speedDown()
bmw.show()

sonata = Car('소나타', '흰색', 3000)
sonata.speedUp()
sonata.speedDown()
sonata.show()

kb = Account('국민은행', '111-11-111', '김유신', 10000)
kb.deposit(20000)
kb.withdraw(5000)
# 캡슐화
# kb.__balance += 1 // private 속성으로 참조 못함
kb.show()

wr = Account('우리은행', '101-11-2222' , '김춘추', 20000)
wr.deposit(10000)
wr.withdraw(7000)
wr.show()



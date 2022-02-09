'''
oop(객체지향 프로그램)
- class(변수 + 함수) - instance 생성 가능
-- 클래스에 정의된 구성요소(변수와 함수)는 클래스의 소유가 아닌 인스턴스의 소유로 봐야함
-- initializer(초기화 함수, 생성자)
-- magic function
- object vs instance (실세계에 존재하는 객채 == object)
- object - 명사적(변수), 동사적(함수) 특징으로 분류 가능
- 함수 < 클래스 < 모듈(클래스(변수+함수)) < 패키지
- self <- 인스턴스를 대표하는 키워드
'''

# 강사의 정보를 저장하려고 한다....
# 만약에 여러명의 강사의 정보를 저장한다면?
# [{}, {}, {}]

tea_name = '임정섭'
tea_subject = 'python'
tea_mail = 'jslim9413@naver.com'

def printTea():
    print(tea_name,tea_subject,tea_mail)

class Teacher:
    # 변수 + 함수
    cls_var = 3.5

    def doing(self):
        print("인스턴스 소유의 함수입니다. ^*^")

# printTea()
# doing 함수를 호출하기 위해서는
# 1. 클래스로부터 인스턴스 생성이 필요
# 2. instance.함수()
tea = Teacher()  # 인스턴스 생성
print('instance address -',tea)
print('instance function - ',end = '')
tea.doing()
print('instance variable - ',tea.cls_var)

class Person:
    # 인스턴스 소유가 아닌 클래스 소유의 변수로 봄
    # 모든 인스턴스가 공유하는 변수
    cls_var = 3.5  #인스턴스 소유가 아님

    # initializer(magic function- __로 시작해서 __로 끝나는 함수, 생성자)
    # 객체 생성시 자동으로 호출되는 함수
    # 명시적으로 호출이 불가
    def __init__(self,name,subject,email):
        self.name = name
        self.subject = subject
        self.email = email

    def perInfo(self):
        return '이름 {}, 과목 {}, 메일 {}'.format(self.name,self.subject,self.email)

    def isScholarShip(self, grade):
        if grade >= Person.cls_var:
            return True
        else:
            return False

per01 = Person('임섭순','파이썬','jslim9413@naver.com')
per01.cls_var = 4.5
per02 = Person('노희명','파이썬','jslim9413@naver.com')
per03 = Person('정민수','파이썬','jslim9413@naver.com')
lst = list()
lst.append(per01)
lst.append(per02)
lst.append(per03)
print('정보 출력 - ')
for instance in lst:
    print(instance.name)
    print(instance.subject)
    print(instance.email)
    print(instance.isScholarShip(4.5))
    print(instance.cls_var)
    print(instance.perInfo())
print()

class Employee:
    raise_rate = 1.1
    def __init__(self, userName, userSalary):
        print('초기화 함수 자동 호출')
        self.userName = userName
        self.userSalary = userSalary

    def getSalary(self):
        return '{} 님의 급여는 {} 입니다.'.format(self.userName,self.userSalary)

    def incrementSalary(self):
        self.userSalary = self.userSalary * Employee.raise_rate


empobj01 = Employee('임섭순',1000)
empobj02 = Employee('이이슬',2000)
print(empobj01.getSalary())
print(empobj02.getSalary())
print('급여인상 - ')
empobj01.incrementSalary()
empobj02.incrementSalary()
print(empobj01.getSalary())
print(empobj02.getSalary())
print('급여 인상률 변경 - ')
Employee.raise_rate = 1.5
empobj01.incrementSalary()
empobj02.incrementSalary()
print(empobj01.getSalary())
print(empobj02.getSalary())

'''
[실습]
- 1. Account class 작성
- 2. 인스턴스 변수 - account, balance, interestRate
- 3. accountInfo() - 계좌정보 출력하는 함수
- 4. deposit(amount) - 매개변수 들어온 amount를 balance 누적
- 5. withDraw(amount) - 매개변수로 들어온 amount를 balnce 출금
- 5-1. 단) 잔고가 부족할 경우 '잔액이 부족하여 출금이 안돼요'
- 6. printInterestRate() - 현재 잔액에 이자율을 계산하여 소수점 2자리까지 출력
'''

class Account:
    def __init__(self,account, balance,interestRate):
        self.account = account
        self.balance = balance
        self.interestRate = interestRate

    def accountInfo(self):
        print('계좌번호: {} 잔액: {}'.format(self.account,self.balance))

    def deposit(self,amount):
        self.balance += amount

    def withDraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('잔고가 부족하여 줄금이 안돼요')

    def printInterestRate(self):
        self.balance = self.balance * self.interestRate
        print('%.2f' % self.balance)

account = Account('444-2919-1234',500000,0.073)
print("계좌 정보 출력 - ")
account.accountInfo()
account.withDraw(600000)
account.deposit(200000)
print('이자율')
account.printInterestRate()

class Car:
    def __init__(self, name, door, cc, price):
        self.utype = self.__class__.__name__
        self.name = name
        self.door = door
        self.cc = cc
        self.price = price

    def carInfo(self):
        if self.cc >= 5000:
            self.grade = '대형차'
        elif self.cc >= 3000:
            self.grade = '중형차'
        else:
            self.grade = '준소형차'
        self.display()

    def display(self):
        print('%s는 %d cc이고(%s) 문짝은 %d개 입니다.'% (self.name,self.cc,self.grade,self.door))

myDreamCar = Car('티코',5,800,350)
print('utype - ',myDreamCar.utype)
myDreamCar.carInfo()

# oop(Object Oriented Programing)
# - 은닉화, 상속, 다형성
# 상속(Inheritance), object(최상위 클래스)
# 부모 - 자식 관계 (is a ~ )
# A(A~Y) A+(Z)
# 구문형식 : class class_name(부모 클래스):

class Unit(object):
    pass

class Marine(Unit):
    pass

class Medic(Unit):
    pass

# 은닉화(encapsulation) - information hidding 외부에서 접근하지 못하도록 하는 것
# 구문형식 : __변수명
# 직접적으로 변수에 접근할 수 없지만, 함수를 통한 간접 허용
# setXXXX(), getXXXX()
class UserData(object):
    def __init__(self):
        self.__year = 2022
        self.month = 2
        self.day = 4

    def setYear(self,year):
        if year <=0 :
            self. __year = 2022
        else:
            self.__year = year

    def getYear(self):
        return self.__year

myDate = UserData()
myDate.setYear(1900)
print('year - ',myDate.getYear())
print('month - ',myDate.month)
print('day - ',myDate.day)

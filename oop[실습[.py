'''
[실습]
- 1. Account class 작성
- 2. 인스턴스 변수 - type(S|F), account, balance, interestRate
- 3. accountInfo() - 계좌정보를 줄력하는 함수
- 4. deposit(amount) - 매개변수 들어온  amount를 balance 입금
- 5. withDraw(amount) - 매개변수 들어온 amount를 balance 출금
- 5-1. 단) 잔고가 부족할 경우 '잔액이 부족하여 출금이 안돼요'
- 6. abstract로 만들것 printInterestRate() - 현재 잔액에 이자율을 계산하여 소수점 2자리로 출력
- 2-1. SavingAccount(Account), FundAccount(Account)
       overriding -- printInterestRate()
-- SavingAccount - printInterestRate()
   기본 이자율에 만기시 이자율을 0.1로 계산
-- FundAccount - printInterRate()
   기본 이자율에 잔액이 10만원 이상이면 10%
   기본 이자율에 잔액이 50만원 이상이면 15%
   기본 이자율에 잔약이 100만원 이상이면 20%
'''

# caller
class Account:
    def __init__(self,type,account, balance,interestRate):
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

class SavingAccount(Account):
    def __init__(self,account,balance,interestRate):
        super().__init__(account, balance,interestRate)
    def printInterestRate(self):
        self.interestRate = 0.1
        self.balance = self.balance * self.interestRate
        print('%.2f' % self.balance)

# class FundAccount(Account):
    # def __init__(self,account,balance,interestRate):
    #     super().__init__(account, balance,interestRate)
    # def printInterestRate(self):
    #     if self.balance >= 10 and self.balance < 50:
    #         self.interestRate = 0.1
    #         self.balance = self.balance * self.interestRate
    #         print('%.2f' % self.balance)
    #     elif self.balance >=50 and self.balance <100:
    #         self.balance = self.balance * self.interestRate
    #         print('%.2f' % self.balance)
'''
학습목표
- 예외처리
- 매직함수, 데코레이터, 제너레이터, 일급함수
- 파일 입출력
'''

# print('programming start - ')
# print("*" * 50)
# age = int(input('나이를 숫자로 입력해주세요 : '))
# print("your age is ",age, 'years old')
# print("*" * 50)
# print("programming end ")

'''
Exception - XXXXError
예외처리 구문
try     :
    예외가 발생할 가능성이 있는 코드를 정의하는 곳
    A
    B
excpet A :  다중으로 나오는 것 가틍
    발생한 예외를 잡기위한 객체를 정의하고 처리하는 곳
excpet B :
    발생한 예외를 잡기위한 객체를 정의하고 처리하는 곳
else    :
    예외가 발생되지 않을 때 실행되는 곳
finally :
    예외발생 여부와 상관없이 실행되는 곳
'''
# function define - worker
def smpInput():
    try:
        age = int(input('나이를 숫자로 입력해주세요 : '))
    except Exception as e :
        print(str(e))
        smpInput()
    else:
        print('your age is', age, 'years old')
    finally:
        print('** 예외발생여부와 상관없이 무조건 수행 **')

# caller
# smpInput()
# print('programming end - ')

'''
매개변수로 넘겨 받은 각 첨자번지의 값에 제곱한 결과를
출력하려고 한다.
예외 발생을 확인하고 예외처리 구문을 추가하여
정상적인 흐름의 함수 호출이 되도록 만들어 본다면?
'''
def exceptionFunc(lst):
    for e in lst:
        try:
            print('raw - ', e)
            sqrt = e ** 2
            print('squred - ',sqrt)
        except TypeError as t:
            pass
# caller
# usrlst = [10,20,25,'num',40,50]
# exceptionFunc(usrlst)

# 사용자 정의 예외클래스를 만들 수 있다.

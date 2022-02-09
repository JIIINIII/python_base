
'''
 파이썬 딕셔너리
- 범용적으로 가장 많이 사용
- [{key : value}, {}]
- 선언 : {key : value}, dict{}
- 순서 X, 키 중복 X, 수정 O, 삭제 O
'''
tmpDict = {
    'name' : 'shj',
    'phone' : '01088665157',
    'birth' : '000903'
}
print('type - ',type(tmpDict),tmpDict)

# in 연산자 - 키 유무를 확인하는 용도
print('key 검사 - ', 'name' in tmpDict)

tmpDict ={
    '메로나' : [300,20],
    '비비빅' : [400,20],
    '죠스바' : [100,50]
}
#메로나의 가격 정보를 확인하고 싶다면?
print('메로나의 가격은 {}원 입니다.'.format(tmpDict['메로나'][0]))
print('메로나의 수량은 {}개 입니다.'.format(tmpDict['메로나'][1]))

# 새로운 데이터를 추가하고 싶다면?
tmpDict['메로나'] = [500,50]
print('data-' , tmpDict)

# 메로나의 가격을 10% 인상하고자 한다면?
melonaLst = tmpDict['메로나']
print('melona value - ',type(melonaLst),melonaLst)
melonaLst[0] * 1.1
print('data - ',tmpDict)

tmpDict = {
    'Name'   : '섭섭해',
    'City'   : 'Seoul',
    'Age'    : 50,
    'Grade'  : 'A+',
    'Status' : True
}

# 수정
tmpDict['Name'] = '임정섭'
print('data - ',tmpDict)

# 확인
print('print - ',tmpDict['Name'])

tmpDict = dict([
    ('city','seoul'),('age','50')
])
print('type - ',type(tmpDict),tmpDict)

# case 03
tmpDict = dict(
    city = 'seoul',
    age = 50
)
print('type - ',type(tmpDict),tmpDict)
print('key를 이용한 값 출력 - ',tmpDict['city'])
print('key를 이용한 값 출력 - ',tmpDict.get('Age'))
# tmpDict['name'] = '임정섭'
tmpDict.update({'name' : '임섭순'}) # 위와 동일일
print('data - ',tmpDict)

# zip()
# case 04
keys = ('apple','pear','peach')
values = (1000,1500,2000)
#zipDict = dict(zip(keys,values)) # 딕셔너리 만드는 구문
#print('type - ',type(zipDict),zipDict)
print('len - ',len(keys),len(values))
zipDict = {}
for idx in range(len(keys)):
    zipDict[keys[idx]] = values[idx]

print('type - ',type(zipDict),zipDict)

# dict - keys(), values(), items() - 반복문 사용 가능
for key in zipDict.keys():
    print('{} : {}'.format(key,zipDict.get(key)))
for key in zipDict.values():
    print(values)
for key, values in zipDict.items():
    print('{} : {}'.format(key,values))

# pop
print('pop - ', zipDict.pop('apple'))
print('data - ',zipDict)

zipDict.clear()
print('clear - ',zipDict)

'''
set: 집합의 자료형
- 선언 : {}, set{}
- 순서 X, 중복 X
- index, sequence X
'''
tmpSet = {1,2,3,3,3,3,3,'shj'}
tmpSet = set({5,4,1,2,3,3,3,3,3,'shj'})
print('type - ',type(tmpSet),tmpSet)
print('dir - ',dir(tmpSet))
# print ('not indexing - ', tmpSet[0]) --- error
tmpT = tuple(tmpSet)
print('type - ', type(tmpT),tmpT)
tmpL = list(tmpSet)
print('type - ',type(tmpL),tmpL)

gender = ['남','남','여','남','남','여']
sgender = set(gender)
print('중복 제거 - ',type(sgender), sgender)

set01 = set('jslim')
print('set01 - ',set01)

set02 = set([1,2,3,4,5])
set03 = set([3,4,5,6,7])

print('intersection - ', set02.intersection(set03))
print('union        - ', set02.union(set03))
print('difference   - ', set02.difference(set03))

set02.add(6)
print('add - ',set02)

set02.update([7,8])
print('updaet - ', set02)

set02.remove(6)
print('remove - ',set02)

set02.clear()
print('clear - ',set02)

'''
boolean Type
- True | False
- 논리연산자(not, and, or)
- 비교연산자(~  , &  ,  |)
- "", [], (), {}, 0, None -> False
'''
print('boolean - ',bool(0))
print('boolean - ',type([]),bool([]))

trueFlag  = True
falseFlag = False
# 논리 곱
print('T and T - ',trueFlag & trueFlag)
print('T and F - ',trueFlag and falseFlag)
print('F and T - ',falseFlag and trueFlag)
print('F and F - ',falseFlag and falseFlag)
print()
# 논리 합
print('T and T - ',trueFlag | trueFlag)
print('T and F - ',trueFlag or falseFlag)
print('F and T - ',falseFlag or trueFlag)
print('F and F - ',falseFlag or falseFlag)
print()

print('not - ', not trueFlag)
print('int - ', int(trueFlag))
print('int - ', int(falseFlag))

'''
날짜
'''
from datetime import date, datetime ,timedelta
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

#timedelta -> week, day, hour, minute, second
#relativedelta -> year, month

today = date.today()
print('type -',type(today),today)
print(today.year,today.month, today.day)

day_time = datetime.today()
print('type - ',type(day_time),day_time)
print(day_time.hour,day_time.minute,day_time.second,day_time.microsecond)

today = date.today()
day = timedelta(days = -1)
print('하루 전 날짜 - ', type(today), type(day),today + day )

today = date.today()
day  = relativedelta(months = -2)
print('두달 전 날짜 - ', type(today), type(day), today + day)

myDate = parse("2021-01-27")
print('type - ', type(myDate), myDate)

myDate = datetime(2019,12,25)
print('type - ', type(myDate), myDate)

# 날짜타입을 문자열 포맷으로 지정할 수 있다 %m %d %y
# strftime(날짜 -> 문자), strptime(문자 -> 날짜)
print('format - ', myDate.strftime("%m-%d-%y"))
print('날짜 -> 문자 - ',type(myDate.strftime("%m-%d-%Y")),myDate.strftime("%m-%d-%Y"))
str = "2019-12-25"
print('문자 -> 날짜 - ',datetime.strptime(str, '%Y-%m-%d'))

'''
사용자 입력
 -input()
'''

name = input('Enter your Name : ')
age  = int(input('Enter your Age  : '))
height = float(input('Enter your Height : '))
marriage = bool(input('Enter your Marriage : '))
print('input name - ', type(name),name)
print('input age  - ', type(age),  age)
print('input height - ',type(height),height)
print('input marriage - ',type(marriage),marriage)
print('end-----------------------------')
# 파일 입출력
# xxxx.csv, xxx.xls
# 분석 - ndarray, DataFrame, Series
# AJAX - 비동기 통신 (RestFul, Service)
# jsop - { key : {key : value},
#          key : [{key : value}, {key : value}] }


# 회문(palindrome)
# madam, sos, level, rotator, nurses run
# 회문을 검사하는 로직을 생각해 본다면?
# word = 'madam'
# if word == word[::-1]:
#     pass
# if list(word) == list(reversed(word)):
#     pass
# print('len - ',len(word)//2)
# for i in range(len(word)//2):
#     if word[i] != word[-1-i]:
#         pass

# palindorme_words.txt 파일로부터 회문인 단어만 출력하고
# 카운팅 해본다면
# 주의) 단어사이의 줄바꿈이 두번 일어나면 안된다..

def palindorme_word_func():
    cnt = 0
    with open('C:/Users/sonhyeonjin/PycharmProjects/data/palindrome_words.txt', 'r', encoding='utf-8') as file:
        for line in file:
            isFlag = True
            line = line.strip('\n')
            for i in range(len(line)//2):
                if line[i] != line[-1-i]:
                    isFlag = False
                    break
            if isFlag:
                print(line)
                cnt+=1
    print('회문단어의 갯수는 {}개 입니다.'.format(cnt))

# def palindorme_word_func():
#     cnt = 0
#     with open('C:/Users/sonhyeonjin/PycharmProjects/data/palindrome_words.txt', 'r', encoding='utf-8') as file:
#         for line in file:
#             isFlag = True
#             line = line.strip('\n')
#             for i in range(len(line)//2):
#                 if line[i] == line[-1-i]:
#                     print(line)

# caller
palindorme_word_func()

import pandas as pd
# .csv, (.xls, .xlsx) , .txt
# pd.read_csv()  - DataFrame
# pd.ExcelFile() - DataFrame
# pd.read_excel()
def load_file(filePath):
    data = None
    if filePath.split('.')[-1] == 'csv':
        data = pd.read_csv(filePath,encoding = 'ms949')
    elif filePath.split('.')[-1] == 'xls' or filePath.split('.')[-1] == 'xlsx':
        data = pd.ExcelFile(filePath)
    else:
        with open(filePath,'r',encoding = 'utf-8') as file:
            lines = file.readlines()
            # print(type(lines[0]),lines[0])
            # print(type(j.loads(lines[0])))
            lines = [j.loads(line) for line in lines]
            # print(type(lines[0]))
            # print(lines[0]['c'])
            data = pd.DataFrame(lines)
    return data

# label 컬럼을 활용하여 빈도수를 출력하는 구문을 작성해 본다면?
def csv_file(filePath):
    data = load_file(filePath)
    # print('type - ', type(data))
    # print(data.head())
    # print(data.info())
    # print(data.height)
    # print(data['height'])
    # print(data.label)
    lblFreq = {}
    for key in data.label:
        lblFreq[key] = lblFreq.get(key,0) + 1
    print(lblFreq)

    print()
    print(dict(data['label'].value_counts()))


# caller
# csv_file('C:/Users/sonhyeonjin/PycharmProjects/data/service_bmi.csv')

def excel_file(filePath):
    data = load_file(filePath)
    print('type - ',type(data))
    data = data.parse('sam_kospi')
    print('type - ',type(data))
    print(data.info())
    print(data.describe())

# caller
# excel_file('C:/Users/sonhyeonjin/PycharmProjects/data/sam_kospi.xlsx')

# json
# 네트워크 상에서 표준프로토콜로 사용되는 파일 형식
# json -> python(dict, list) : decoding
# json <- python(dict, list) : encoding

import json as j

tmpDict = {'id' : 'jslim', 'pwd' : 'jslim'}
print('type - ',type(tmpDict),tmpDict)
# dict -> json
print('dict -> json - ')
jsonDict = j.dumps(tmpDict)
print('type - ',type(jsonDict),jsonDict)

# json -> dict
print('json -> dict -')
pyDict = j.loads(jsonDict)
print('type - ',type(jsonDict),jsonDict)
print(pyDict['id'])

def json_file(filePath):
    data = load_file(filePath)
    print('type - ',type(data))
    print(data.info())
    print()
    print(data.head())


# caller
json_file('C:/Users/sonhyeonjin/PycharmProjects/data/usagov_bitly.txt')
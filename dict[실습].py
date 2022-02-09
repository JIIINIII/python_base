
# 단어의 빈도수 구하기
# {'love' : 2, 'word' : 2, 'cat' : 2}
word_vec = ['love','word','love','cat','word']
print('len - ',len(word_vec))
'''
내가 쓴 코드
love_num = 0
word_num = 0
cat_num = 0
for word in word_vec:
    if word == 'love':
        love_num += 1
    if word == 'word':
        word_num += 1
    if word == 'cat':
        cat_num += 1
Dict = {'love': love_num, 'word':word_num,'cat':cat_num}
print(type(Dict),Dict)
'''

# 강사님이 쓴 코드
wc = {}
for word in word_vec:
    wc[word] = wc.get(word,0) + 1
print('wc - ',wc)

# case 02
wc = {}
for word in word_vec:
    wc[word] = word_vec.count(word)
print('wc - ',wc)

# case 03
wc = {}
for word in word_vec:
    if word in wc:
        wc[word] += 1
    else:
        wc[word] = 1
print('wc - ',wc)

# case 04
wc = dict(
    love = word_vec.count('love'),
    word = word_vec.count('word'),
    cat = word_vec.count('cat')
)

# case 05
# set, zip
result = dict(zip(set(word_vec),[word_vec.count(i) for i in set(word_vec)]))
print('wc - ',result)
# 영어 단어 저장하기

f = open("words.txt", 'w')
word = ['하늘','바다','땅','달','나무'
        ,'꽃','풀','열매','해','별']

for i in word:
    f.write(i+' ')
f.close()
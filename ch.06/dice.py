import random

# 주사위 10번 던지기
'''
for i in range(10):
    dice = random.randint(1,6)
    print(dice)

print('='*40)
'''
# 리스트에서 랜덤하게 단어 추출하기


for i in range(8):
    card=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    c = random.choice(card)
    print(c,end = ' ')


import time

input('엔터를 누르고 20초를 셈니다.')
start = time.time()

input('20초 후에 다시 엔터를 누름니다.')
end = time.time()

et=(end-start)


print('실제시간 : ', abs(et) , '초')
print('시간차이 : ', abs(et-20) , '초')


import time
'''
print(time.time())
print(time.localtime())
print(time.ctime())

print(time.strftime('%x',time.localtime()))
print(time.strftime('%X',time.localtime()))
'''

#time.sleep(1) : 1초간 대기
for i in range(1,11):
    print(i)
    time.sleep(1)

'''
#1번
국어 = 80
영어 = 75
수학 = 55

점수 = (국어 + 영어+ 수학)/3

print("평균 :", 점수)

#2번
자연수 = int(input("숫자를 입력하세요 : "))

if 자연수== 0:
    print("공의 숫자")
elif 자연수 % 2 == 0:
    print("짝수")
else:
    print("홀수")
    
#3번
pin = "881120-1068234"
yyymmdd = pin[0:6]
num = pin[7:14]
print(yyymmdd)
print(num)


#4번
pin = "881120-1068234"
gender = int(pin[7])

if gender % 2 ==0:
    print("여성")
else:
    print("남성")

#5번
a = "a:b:c:d"
b = a.replace(":","#")
print(b)


#6번
a=[5,2,3,1,4]
print(a)
a.sort()
print(a)
a.reverse()
print(a)


#7번
a = [ 'Life','is','too','short']
result = " ".join(a)
print(result)
'''

#split() 예제
msg = "Life is too short"
print(msg)
msg=msg.split()
print(msg)

s = "a:b:c:d"
s = s.split(':')
print(s)

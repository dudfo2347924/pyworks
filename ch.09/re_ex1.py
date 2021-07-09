import re
#'*'과 '+'의 차이 비교

pat = re.compile("ca*t") # '*'는 앞문자가 0개이상 반복
m1 = re.findall(pat, "caat")
print(m1)

m2 = re.findall(pat, "ct")
print(m2)

pat2 = re.compile("ca+t") # '+'는 앞문자가 1개이상 반복
m3 = re.findall(pat2, "caat")
print(m3)

m4 = re.findall(pat2, "cat")
print(m4)
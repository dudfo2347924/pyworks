import  re

str = "park 010-1234-4567"
pat = re.compile("(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)")
#m = re.search(pat,str)
#print(m.group(0))
#print(m.group(1))
#print(m.group(2))

#Sub 메소드 사용

#s = pat.sub("\g<name> \g<phone>", str)

pat = re.compile("(\w+)\s+(\d+[-]\d+[-]\d+)")
s = pat.sub("\g<1> \g<2>", str)

print(s)

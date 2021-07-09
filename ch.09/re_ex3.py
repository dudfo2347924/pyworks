import re

str = "abcd<hr>Thank you"
#pat = re.compile("<(.*)")>
pat = re.compile(("(<.*>)"))
m = re.findall(pat,str)
print(m)

#정규 표현식 예제

import re

p = re.compile('[A-z]+')
m = p.match("2021 incheon")
print(m)

s = p.search("2021 incheon")
print(s.group())

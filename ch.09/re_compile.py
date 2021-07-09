#정규 표현식 예제

import re

p = re.compile('a-o')
m = p.match('afternoon')
print(m)

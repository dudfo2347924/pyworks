import re

p = re.compile("(?P<name>(\w+))\s(?P<phone>(\d+[-]\d+[-]\d+))")
s = p.search("jang 010-1234-5678")
print(s.group("name"))
print(s.group("phone"))
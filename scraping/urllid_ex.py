# 웹 스크레핑(크롤링)
from urllib import request

#url = "http://www.naver.com"
content = request.urlopen("http://www.daum.net")
print(content.read())
#BeautifulSoup 모듈 사용하기

from bs4 import BeautifulSoup

html_str="""
<html>
<body>
    <ul class='item'>
        <li>인공지능</li>
        <li>빅데이터</li>
        <li>로보옷트</li>
    <ul>
</body>
</html>
"""
soup = BeautifulSoup(html_str,"html.parser")
#print(soup)
ul = soup.find('ul') # find()태그는 가장 먼저나온 태그만 검색
print(ul.text)

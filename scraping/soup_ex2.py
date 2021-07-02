#BeautifulSoup 모듈 사용하기

from bs4 import BeautifulSoup

html_str="""
<html>
<body>
    <ul class='item'>
        <li>인공지능</li>
        <li>빅데이터</li>
        <li>로보옷트</li>
    </ul>
    <ul class='lang'>
        <li>영어</li>
        <li>한국어</li>
        <li>일본어</li>
    </ul>
</body>
</html>
"""
contents = BeautifulSoup(html_str, "html.parser")
ul = contents.find('ul', {'class':'lang'})
#print(ul)
#li = ul.find('li')
#print(li)

lis = ul.find_all('li')
print(lis)
print(lis[2].text)


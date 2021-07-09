from urllib import request
from bs4 import BeautifulSoup

html = request.urlopen("https://finance.naver.com/marketindex/")
code = html.read().decode('euc-kr','replace') .encode('utf-8',"replace")
contents = BeautifulSoup(code, 'html.parser')
ul = contents.select("ul.data_lst li")

for li in ul:
    ex = li.select_one("span.blind")
    val = li.select_one("span.value")
    #print(ex)
    #print(val)
    print(ex.string.split(' ')[-1], ' : ', val.string)

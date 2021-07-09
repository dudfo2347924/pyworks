from urllib import request
from bs4 import BeautifulSoup

def getcontent(item_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + item_code
    html = request.urlopen(url)
    content = BeautifulSoup(html,'html.parser')
    return content

def getprice(item_code):
    content = getcontent(item_code)
    no_today = content.find('p', {'class':'no_today'})
    price = no_today.find('span', {'class':'blind'})
    return price

#005930-삼성 ,035720-카카오 ,035420-네이버
삼성전자 = getprice("005930")
카카오 = getprice("035720")
네이버 = getprice("035420")
print("삼성전자 : {}원".format(삼성전자.text))
print("카카오 : {}원".format(카카오.text))
print("네이버 : {}원".format(네이버.text))

'''
contents = getcontent(item_code)
no_today = contents.find('p', {'class':'no_today'})
#print(no_today)
price = no_today.find('span',{'class':'blind'})

print(price)
print("삼성전자 주가 : {}원".format(price.text))
'''


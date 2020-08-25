# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    mainpage = 'https://www.bxwx.io/book/121842/'

    url = 'https://www.bxwx.io/book/121842/43825227.html'

    req = requests.get(mainpage)
    print('req:',req)
    print("======================================")
    html = req.content.decode("GBK", "ignore")
    print('html:',html)
    print('=======================================')
    bf = BeautifulSoup(html,'html.parser')
    print('bf:',bf)
    print('===========================================')
    div = bf.find_all('div', class_ = 'zjbox')
    print('div:',div)
    print('==========================================')
    a_bf = BeautifulSoup(str(div[0]),'html.parser')
    print('a_bf:', a_bf)
    print('=========================================')
    a = a_bf.find_all('a')
    #print(div[0])
    #print(texts[0].text.replace('\xa0','\n\n'))
    for each in a:
        print(each.string, mainpage + each.get('href'))
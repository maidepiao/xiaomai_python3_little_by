import requests

url='http://bang.dangdang.com/books/bestsellers/' \
    '01.03.00.00.00.00-recent30-0-0-1-1'
htmlStr=requests.get(url)
#print(htmlStr.text)

from bs4 import BeautifulSoup
soup=BeautifulSoup(htmlStr.text,'lxml')
data=soup.select('body > div.bang_wrapper '
                 '> div.bang_content > div.bang_list_box > ul > li')
#print(data)

for item in data:
    for i in [0,2,4,5]:
        print(item.find_all('div')[i].getText(),end=' | ')
    print(item.find_all('div')[6].find_all('span')[0].getText()
          ,end='')
    print()





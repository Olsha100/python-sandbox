import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')

html_content = req.text

soup = BeautifulSoup(html_content, 'html.parser')

article_markups = soup.find_all("p", "paywall")

article_text = ''

for el in article_markups:
    if len(el.contents) == 1:
        article_text += '\n' + str(el.contents[0])
        print(str(el.contents[0]))
    else:
        for i in el:
            print(str(i))
            
print(article_text)

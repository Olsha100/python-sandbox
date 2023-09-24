from bs4 import BeautifulSoup
import requests

request = requests.get('https://conadrogach.pl')
html_doc = request.text

soup = BeautifulSoup(html_doc, 'html.parser')
publications = soup.css.select("[class*=publication] h1,h2,h3,h4,h5,h6")

for header in publications:
    print(header.contents[0])




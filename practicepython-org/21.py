import requests
import re
from bs4 import BeautifulSoup


html_content = article_markups = article_text = file_name = ''


def name_file():
    global file_name

    file_name = input('Type the name of the file that the article should be written to: ')
   
    while len(re.findall('[.,;:*]', file_name))  > 0:
        file_name = input('The file name cannot contain .,;:* characters. Try again: ')


def request_source():
    print('Downloading the URL resource...')

    req = requests.get('https://jakoszczedzacpieniadze.pl/wlasnie-peklo-50-lat-i-mam-pewne-plany')

    return req.text


def parse_source():
    print('Parsing the resource...')

    soup = BeautifulSoup(html_content, 'html.parser')
    post = soup.find("div", class_ = "format_text")

    return post.findAll("p")


def format_article():
    global article_text

    print('Extracting the article contents...')

    for el in article_markups:

        if el.find("a") == None:
          
            if len(el.contents) == 1:
                article_text += '\n\n' + str(el.get_text())
          
            else:
                for i in el:
                    article_text += str(i.get_text())


if __name__ == '__main__':

    name_file()
    html_content = request_source()
    article_markups = parse_source()
    format_article()

    with open(file_name + '.txt', 'w', encoding="utf-8") as file:
        file.write(str(article_text))

    print('------------------')
    print('Article saved')
    print('------------------')
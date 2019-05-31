
from bs4 import BeautifulSoup
from ptt import *

board = 'MacShop'
url = 'https://www.ptt.cc/bbs/' + board + '/index.html'

print(url)

title = Title(url).str()
author = Author(url).str()
date = Date(url).str()

print(title)
print(author)
print(date)

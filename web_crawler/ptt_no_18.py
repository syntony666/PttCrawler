from ptt import *
from ptt_print import pretty_print

board = 'iOS'
url = 'https://www.ptt.cc/bbs/' + board + '/index.html'
page = 5

try:

    for i in range(page):

        print("本頁為: " + url + '\n')

        push = Push(url).str()
        title = Title(url).str()
        author = Author(url).str()
        date = Date(url).str()

        for a, b, c, d in zip(push, title, date, author):
            pretty_print(a, b, c, d)
        print('------------------------------------------------------------------------------------------------------------------------'+'\n')

        url = previous(url)

except IndexError:
    print("無法通過18歲驗證")

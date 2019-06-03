from src.ptt import *

board = input("請輸入看板名稱: ")
page = int(input("請輸入頁數: "))
print('\n')
try:
    previous('https://www.ptt.cc/bbs/' + board + '/index.html')

except IndexError:

    ptt18(board, page)

else:
    ptt(board, page)

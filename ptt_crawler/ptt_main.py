from src.crawler import *


def main():
    try:
        board = input("請輸入看板名稱: ")
        page = int(input("請輸入頁數: "))
    except ValueError:
        print("輸入錯誤")
    else:
        print('\n')

    try:
        previous(BeautifulSoup(requests.get('https://www.ptt.cc/bbs/' + board + '/index.html').text, "html.parser"))
    except IndexError:
        ptt(board, page, True)
    else:
        ptt(board, page, False)


if __name__ == '__main__':
    main()

from crawler import *


def main():
    try:
        board = input("請輸入看板名稱: ")
        page = int(input("請輸入頁數: "))
    except ValueError:
        print("輸入錯誤")

    else:
        print('\n')
        try:
            previous('https://www.ptt.cc/bbs/' + board + '/index.html')

        except IndexError:

            ptt18(board, page)

        else:
            ptt(board, page)


if __name__ == '__main__':
    main()

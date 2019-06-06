from src.crawler import *


def ptt(board, page, is18):
    url = 'https://www.ptt.cc/bbs/' + board + '/index.html'
    try:
        for i in range(page):
            if is18 == True:
                res = ask18(board, url)
            else:
                res = BeautifulSoup(requests.get(url).text, 'html.parser')
            print('-'*100 + '\n\n'+'本頁為: ' + url + ' (第 ' + str(i + 1) + ' 頁)' + '\n')
            url = dataOutput(res)
        print('-'*100 + '\n')
    except IndexError:
        print('看板名稱不正確\n')


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

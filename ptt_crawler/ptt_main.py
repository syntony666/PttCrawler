from src.crawler import *

# the soul of this crawler


def ptt(board, page, is18):
    url = 'https://www.ptt.cc/bbs/' + board + '/index.html'  # generate the url
    try:
        for i in range(page):		# crawl by pages
            if is18 == True:		# the condition that if it has cookie to check is adult or not
                res = ask18(board, url)
            else:
                res = BeautifulSoup(requests.get(url).text, 'html.parser')  # get the resource of html
            print('-'*100 + '\n\n'+'本頁為: ' + url + ' (第 ' + str(i + 1) + ' 頁)' + '\n')
            url = dataOutput(res)  # print the result and crawl previous page
        print('-'*100 + '\n')
    # if we can't fint the index of the previous page means the name of the board is wrong
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

        # check that if it has cookie to check is adult or not
    try:
        previous(BeautifulSoup(requests.get('https://www.ptt.cc/bbs/' + board + '/index.html').text, "html.parser"))
    except IndexError:
        ptt(board, page, True)
    else:
        ptt(board, page, False)


if __name__ == '__main__':
    main()

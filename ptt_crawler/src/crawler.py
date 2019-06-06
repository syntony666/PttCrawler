from bs4 import BeautifulSoup
import requests

from src.data import *
from src.ptt_print import pretty_print


def previous(res):
    u = res.select('div.btn-group.btn-group-paging a')
    url = 'https://www.ptt.cc' + u[1]['href']
    return url


def crawler(res):
    m = Meta(res)
    for a, b, c, d, e in zip(m.push(), m.title(), m.date(), m.author(), m.link()):
        pretty_print(a, b, c, d)
        print(e+'\n')
    return previous(res)


def ask18(board, url):
    r = requests.Session()
    payload = {
        'from': '/bbs/'+board+'/index.html',
        'yes': 'yes'
    }
    r1 = r.post('https://www.ptt.cc/ask/over18?from=%2Fbbs%2F' +
                board + '%2Findex.html', payload)
    return BeautifulSoup(r.get(url).text, 'html.parser')


def ptt(board, page, is18):
    url = 'https://www.ptt.cc/bbs/' + board + '/index.html'
    try:
        for i in range(page):
            if is18 == True:
                res = ask18(board, url)
            else:
                res = BeautifulSoup(requests.get(url).text, 'html.parser')
            print('-'*100 + '\n\n'+'本頁為: ' + url + ' (第 ' + str(i + 1) + ' 頁)' + '\n')
            url = crawler(res)
        print('-'*100 + '\n')
    except IndexError:
        print('看板名稱不正確\n')

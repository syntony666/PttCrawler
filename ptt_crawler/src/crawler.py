from bs4 import BeautifulSoup
import requests

from data import *
from ptt_print import pretty_print


def previous(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    u = soup.select("div.btn-group.btn-group-paging a")
    url = "https://www.ptt.cc" + u[1]["href"]
    return url


def crawler(res):
    push = reversed(Push(res).str())
    title = reversed(Title(res).str())
    author = reversed(Author(res).str())
    date = reversed(Date(res).str())

    for a, b, c, d in zip(push, title, date, author):
        pretty_print(a, b, c, d)


def ask18(board, url):
    r = requests.Session()
    payload = {
        "from": "/bbs/"+board+"/index.html",
        "yes": "yes"
    }
    r1 = r.post("https://www.ptt.cc/ask/over18?from=%2Fbbs%2F" +
                board + "%2Findex.html", payload)
    return BeautifulSoup(r.get(url).text, 'html.parser')


def ptt(board, page):
    url = 'https://www.ptt.cc/bbs/' + board + '/index.html'
    for i in range(page):
        print('----------------------------------------------------------------------------------------------' + '\n')
        print("本頁為: " + url + '\n')
        res = BeautifulSoup(requests.get(url).text, "html.parser")
        crawler(res)
        url = previous(url)
    print('----------------------------------------------------------------------------------------------' + '\n')


def ptt18(board, page):
    url = 'https://www.ptt.cc/bbs/' + board + '/index.html'
    try:
        for i in range(page):
            print('----------------------------------------------------------------------------------------------'+'\n')
            print("本頁為: " + url + '\n')
            res = ask18(board, url)
            crawler(res)
            u = res.select("div.btn-group.btn-group-paging a")
            url = "https://www.ptt.cc" + u[1]["href"]
        print('----------------------------------------------------------------------------------------------'+'\n')
    except IndexError:
        print("看板名稱不正確\n")

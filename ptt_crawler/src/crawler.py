from bs4 import BeautifulSoup
import requests

from src.data import *
from src.ptt_print import pretty_print


def previous(res):		# crawl previous page that receive the origin page's resource
    u = res.select('div.btn-group.btn-group-paging a')
    url = 'https://www.ptt.cc' + u[1]['href']
    return url


def dataOutput(res):  # print the result
    m = Meta(res)
    for a, b, c, d, e in zip(m.push(), m.title(), m.date(), m.author(), m.link()):
        pretty_print(a, b, c, d)
        print(e+'\n')
    return previous(res)


def ask18(board, url):  # set cookie to access the broad
    r = requests.Session()
    payload = {
        'from': '/bbs/'+board+'/index.html',
        'yes': 'yes'
    }
    r1 = r.post('https://www.ptt.cc/ask/over18?from=%2Fbbs%2F' +
                board + '%2Findex.html', payload)
    return BeautifulSoup(r.get(url).text, 'html.parser')

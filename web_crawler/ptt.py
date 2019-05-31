from bs4 import BeautifulSoup
import requests


class Push():
    def __init__(self, url):
        res = BeautifulSoup(requests.get(url).text, 'html.parser')
        self.p = [x.string
                  for x in res.html.find_all(['div'], class_=['nrec'])]
        self.push = [x if (x != None) else '0' for x in self.p]

    def str(self):
        return self.push


class Title():
    def __init__(self, url):
        res = BeautifulSoup(requests.get(url).text, 'html.parser')
        self.a1 = [x.get_text().replace('\n', '').replace('\t', '')
                   for x in res.html.find_all(['div'], class_=['title'])]

    def str(self):
        return self.a1


class Author():
    def __init__(self, url):
        res = BeautifulSoup(requests.get(url).text, 'html.parser')
        self.author = [x.string
                       for x in res.html.find_all(['div'], class_=['author'])]

    def str(self):
        return self.author


class Date():
    def __init__(self, url):
        res = BeautifulSoup(requests.get(url).text, 'html.parser')
        self.date = [x.string
                     for x in res.html.find_all(['div'], class_=['date'])]

    def str(self):
        return self.date


def previous(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    u = soup.select("div.btn-group.btn-group-paging a")
    url = "https://www.ptt.cc" + u[1]["href"]
    return url

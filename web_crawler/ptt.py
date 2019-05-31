from bs4 import BeautifulSoup
import requests


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

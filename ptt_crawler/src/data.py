from bs4 import BeautifulSoup


class Push():
    def __init__(self, res):
        self.p = [x.string
                  for x in res.html.find_all(['div'], class_=['nrec'])]
        self.push = [x if (x != None) else '0' for x in self.p]

    def str(self):
        return self.push


class Title():
    def __init__(self, res):
        self.a1 = [x.get_text().replace('\n', '').replace('\t', '')
                   for x in res.html.find_all(['div'], class_=['title'])]

    def str(self):
        return self.a1


class Author():
    def __init__(self, res):
        self.author = [x.string
                       for x in res.html.find_all(['div'], class_=['author'])]

    def str(self):
        return self.author


class Date():
    def __init__(self, res):
        self.date = [x.string
                     for x in res.html.find_all(['div'], class_=['date'])]

    def str(self):
        return self.date

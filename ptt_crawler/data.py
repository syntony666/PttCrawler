from bs4 import BeautifulSoup


class Meta():
    def __init__(self, res):
        self.res = res.html

    def link(self):
        link = ["https://www.ptt.cc" + x['href']
                for x in self.res.select("div.title a")]
        return reversed(link)

    def push(self):
        push = [x.string if (x.string != None) else '0'
                for x in self.res.select("div.nrec")]
        return reversed(push)

    def title(self):
        title = [x.get_text()
                 for x in self.res.select("div.title a")]
        return reversed(title)

    def author(self):
        author = [x.string
                  for x in self.res.select("div.author") if x.string != '-']
        return reversed(author)

    def date(self):
        date = [x.string
                for x in self.res.select("div.date")]
        return reversed(date)

import requests
from bs4 import BeautifulSoup
import urllib.parse
import json
import os.path

from sqlalchemy import create_engine

from sqlalchemy.orm import Session
from website import Website
from page import Page
from base import Base


class WebCrawler:
    def __init__(self, db):
        self.engine = create_engine("sqlite:///{}".format(db))
        # will create all tables
        Base.metadata.create_all(self.engine)
        self.session = Session(bind=self.engine)
        self.visited = []
        self.queue = []
        self.get_urls()

    def get_urls(self):
        pages = self.session.query(Page).all()
        for page in pages:
            #print(page.url)
            self.visited.append(page.url)

    def crawl(self, url):
        if url[len(url) - 1] == '/':
            url = url[:len(url)-1]
        if url in self.visited:
            return
        try:
            r = requests.get(url)
        except:
            return
        html = r.text
        soup = BeautifulSoup(html)
        self.visited.append(url)

        self.session.add_all([Page(url=url, title=soup.title.string if soup.title else "")])
        self.session.commit()
        #print(soup)
        for link in soup.find_all('a'):
            l = urllib.parse.urljoin(url, link.get("href"))
            self.queue.append(l)

    def BFS(self, url):
        i = 1
        if url in self.visited:
            if os.path.exists("queue.json"):
                with open("queue.json", 'r') as file:
                    s = file.read()
                    self.queue = json.loads(s)
        self.queue.append(url)
        while len(self.queue) > 0:
            url = self.queue.pop(0)
            if url is not None and 'javascript' not in url:
                print(url)
                i += 1
                self.crawl(url)

            if i % 100 == 0:
                with open("queue.json", 'w') as file:
                    s = json.dumps(self.queue[:50])
                    file.write(s)


crawler = WebCrawler("test.db")
crawler.BFS("http://dreal.net/wiki/index.php/%D0%9D%D0%B0%D1%87%D0%B0%D0%BB%D0%BD%D0%B0_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

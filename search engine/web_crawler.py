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
        if url in self.visited:
            return
        r = requests.get(url)
        html = r.text
        soup = BeautifulSoup(html)
        self.visited.append(url)

        self.session.add_all([Page(url=url, title=soup.title.string if soup.title else "")])
        self.session.commit()
        #print(soup)
        for link in soup.find_all('a'):
            l = urllib.parse.urljoin(url, link.get("href"))
            self.queue.append(l)

    def tmp(self, url):
        i = 1
        if os.path.exists("queue.json"):
            with open("queue.json", 'r') as file:
                s = file.read()
                self.queue = json.loads(s)
        self.queue.append(url)
        while len(self.queue) > 0:
            url = self.queue.pop(0)
            print(url)
            if url is not None and 'javascript' not in url:
                self.crawl(url)
                i += 1
            if i % 100 == 0:
                with open("queue.json", 'w') as file:
                    s = json.dumps(self.queue[:50])
                    file.write(s)


crawler = WebCrawler("test.db")
crawler.tmp("http://en.wikipedia.org/wiki/Breadth-first_search")

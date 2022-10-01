import requests
from bs4 import BeautifulSoup

class Scrapper(object):
    def __init__(self, url):
        self.url = url
        self.page_content = None

    def content(self):
        page = requests.get(self.url)
        self.page_content = page.content

    def __call__(self):
        content= BeautifulSoup(self.page_content, "html.text")
        return content
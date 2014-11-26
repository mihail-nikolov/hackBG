import sqlite3
import urllib.parse
from bs4 import BeautifulSoup


class Spider():

    def __init__(self, domain):
        self.scanned_urls = []
        self.looked_urls = []
        self.domain = domain

import urllib.parse
from bs4 import BeautifulSoup
import requests


class Spider():

    def __init__(self, domain):
        self.scanned_urls = []
        self.domain = domain


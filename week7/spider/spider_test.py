import sqlite3


class Spider():

    def __init__(self, db):
        self.scanned_urls = []

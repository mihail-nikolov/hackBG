from bs4 import BeautifulSoup
import urllib.request
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""


soup = BeautifulSoup(html_doc)
print(soup.get_text())


#proxies = {'http': 'http://proxy.example.com:8080/'}
#opener = urllib.FancyURLopener(proxies)
#f = opener.open("http://www.python.org/")
#f.read()

with urllib.request.urlopen("https://hackbulgaria.com/") as url:
    s = url.read()
#I'm guessing this would output the html source code?
print(s)

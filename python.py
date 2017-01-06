# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib

url = "https://www.python.org/"
url_oku = urllib.urlopen(url)
soup = BeautifulSoup(url_oku, 'html.parser')
icerik = soup.title.string
print(soup.head) #  <head>...</head>
print(soup.title) #  <title>...</title>
print(soup.body) #   <body>...</body>
print(soup.body.b) #  bold taglarını çeker.
print(soup.a) # linkleri çeker.
print(icerik)
import urllib.request
from bs4 import BeautifulSoup
req = urllib.request.urlopen('https://quality-start.in/company')
soup = BeautifulSoup(req, "html.parser")
print(soup.find('a', class_="btn").string)

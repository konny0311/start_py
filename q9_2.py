import urllib.request
from bs4 import BeautifulSoup
req = urllib.request.urlopen('https://quality-start.in/company')
soup = BeautifulSoup(req, "html.parser")
box = soup.find("div", class_="list-group")
for texts in box.find_all("a"):
    print(texts.string)

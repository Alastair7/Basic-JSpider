import requests
from bs4 import BeautifulSoup

data = requests.get("https://en.wikipedia.org/wiki/2018_in_anime")
soup = BeautifulSoup(data.text, 'html.parser')
print(soup.find_all('p'))
# print(soup.prettify())
# print(data.text)

import requests
import pandas as pd
from bs4 import BeautifulSoup

data = requests.get("https://en.wikipedia.org/wiki/2018_in_anime")
soup = BeautifulSoup(data.text, 'html.parser')
table = soup.find_all('table',{"class" : "wikitable sortable"})[0]
# print(table)

release_date = []
title = []
studio = []
director = []
run_time = []

for row in table.find_all('tr') :
    cells = row.findAll('td')
    if len(cells) == 7:
        release_date.append(cells[0].find(text=True))
        title.append(cells[1].find(text=True))
        studio.append(cells[2].find(text=True))
        director.append(cells[3].find(text=True))
        run_time.append(cells[4].find(text=True))

# print(str(release_date) + " " + str(title) + " " + str(studio) + " " + str(director) + " " + str(run_time) )

dataframe = pd.DataFrame(release_date,columns=['Release Date'])
dataframe['Title'] = title
dataframe['Studio'] = studio
dataframe['Director'] = director
dataframe['Run Time'] = run_time
print(dataframe)

# for in range
# print(soup.find_all('h3')[0].get_text())
# print(soup.prettify())
# print(data.text)
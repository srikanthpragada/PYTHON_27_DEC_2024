import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.tiobe.com/tiobe-index/")
contents = resp.text

soup = BeautifulSoup(contents, 'html.parser')
# get table with id top20
table = soup.find(id="top20")
body = table.find("tbody")
rows = body.find_all("tr")
for row in rows[:10]:
    cols = row.find_all("td")
    name = cols[4].text
    rating = cols[5].text
    print(f"{name:20}   {rating}")

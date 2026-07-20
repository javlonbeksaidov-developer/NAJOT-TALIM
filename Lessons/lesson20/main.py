import requests
import json
from bs4 import BeautifulSoup

url = "https://www.fcbarcelona.com/en/football/first-team/players"
page = requests.get(url=url)

soup = BeautifulSoup(page.text, "html.parser")

with open("players.json", "r", encoding="utf-8") as file:
    players = json.load(file)

blocks = soup.find_all("figcaption")

for player in blocks:
    first_name = player.find("span", attrs={"class": "team-person__first-name"})

    last_name = player.find("span", attrs={"class": "team-person__last-name"})

    position = player.find("li", attrs={"class": "team-person__position-meta"})

    number = player.find("span", attrs={"class": "team-person__number"})

    data = {
        "name": first_name.text.strip() if first_name else "",
        "lname": last_name.text.strip() if last_name else "",
        "position": position.text.strip() if position else "",
        "number": number.text.strip() if number else "",
    }
    players.append(data)

with open("players.json", "w", encoding="utf-8") as file:
    json.dump(players, file, indent=4, ensure_ascii=False)

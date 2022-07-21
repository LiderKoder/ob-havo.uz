import requests
from bs4 import BeautifulSoup

resp = requests.get(f"https://obhavo.uz/ferghana")
soup = BeautifulSoup(resp.text, features="lxml")
hudud = soup.find('div', class_='padd-block').find('h2').text
bugun = soup.find('div', class_='current-day').text
holat = soup.find('div', class_="current-forecast-desc").text
respons = soup.find("div", class_="current-forecast")
kunduzi = respons.find('strong').text
kechasi = respons.find_all('span')[2].text
namlik = soup.find('div', class_='col-1').find_all('p')
oy = soup.find('div', class_='col-2').find_all('p')

text = f"""{bugun}
{hudud} ob havo ma'lumoti:
Holat: {holat}
Kunduzi: {kunduzi}
Kechasi: {kechasi}
{namlik[0].text}
{namlik[1].text}
{namlik[2].text}
{oy[0].text}
{oy[1].text}
{oy[2].text}

© LIDERKODER 21.07.2022
"""
print(text)

# Shaharlar ro'yhatini https://obhavo.uz/ saytidan ko'rib istalgan shaxar uchun moslab olishingiz mumkin :)


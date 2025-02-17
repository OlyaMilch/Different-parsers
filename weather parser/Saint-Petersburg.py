import requests
from bs4 import BeautifulSoup

# URL with city weather
URL = "https://yandex.ru/pogoda/saint-petersburg"

# Request sent
response = requests.get(URL)
response.raise_for_status()  # Response check. 200 - it's ok!

# Here is the entire html code of the page
soup = BeautifulSoup(response.text, "html.parser")

# Take the required line of code
weather = soup.find("div", {"class": "fact__temp"})  # "fact__temp" - this is where weather information on the site is stored
if weather:
    print(f"В Санкт-Петербурге сегодня {weather.get_text()} градусов.")
else:
    print("Не удалось найти информацию о температуре.")
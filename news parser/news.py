import requests
from bs4 import BeautifulSoup

# URL with news
URL = "https://lenta.ru/"

# Request sent
response = requests.get(URL)
response.raise_for_status()  # Response check. 200 - it's ok!

# Here is the entire html code of the page
soup = BeautifulSoup(response.text, "html.parser")

"""
Find all the links on the main page
"a" is the <a> tag, which is responsible for links on a web page.
href=True is a filter that only looks for <a>s that have an href attribute (i.e. links).
Without href=True, find_all("a") would find all <a> tags, even those that don't have an href (for example simple text)
"""

news_items = soup.find_all("a", href=True)

# Filtering news that mentions “USA”
usa_news = []

for item in news_items:
    title = item.get_text(strip=True)  # Title text
    link = item["href"]  # Link

    # Checking if there is "USA" in the title
    if "США" in title:
        full_link = f"https://lenta.ru{link}" if link.startswith("/") else link  # If the link is not complete, then we supplement it using the f-string
        usa_news.append(f"{title} - {full_link}")

# Write the results to a file
with open("usa_news.txt", "w", encoding="utf-8") as file:
    for news in usa_news:
        file.write(news + "\n")

print(f"Найдено {len(usa_news)} новостей про США. Результаты сохранены в usa_news.txt")
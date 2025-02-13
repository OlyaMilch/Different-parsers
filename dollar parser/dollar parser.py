import requests
from bs4 import BeautifulSoup

# URL with exchange rates
URL = "https://www.cbr.ru/currency_base/daily/"

# Request sent
response = requests.get(URL)
response.raise_for_status()  # Response check. 200 - it's ok!

# Here is the entire html code of the page
soup = BeautifulSoup(response.text, "html.parser")

# We are looking for a table with exchange rates
table = soup.find("table", {"class": "data"})

# Looking for the dollar exchange rate (USD)
for row in table.find_all("tr"):  # Gets all rows of the table
    columns = row.find_all("td")  # Gets all cells (columns) inside the current row.
    if columns and columns[1].text.strip() == "USD":
        usd_rate = columns[4].text.strip()  # Strip just removes spaces
        print(f"Курс доллара: {usd_rate} руб.")
        break

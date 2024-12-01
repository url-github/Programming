import numpy as np
arr = np.array([1, 2, 3])
print(arr.mean())  # Wynik: 2.0

import pandas as pd
df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
print(df.describe())

import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()

import requests # Zastosowanie: HTTP API i pobieranie danych z internetu.
response = requests.get("https://example.com")
print(response.text)

from selenium import webdriver # Zastosowanie: Automatyzacja przeglądarek internetowych.
driver = webdriver.Chrome()
driver.get('https://www.example.com')

from bs4 import BeautifulSoup # Zastosowanie: Web scraping.
import requests
url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
titles = soup.find_all('h1')
for title in titles:
    print(title.text)

from datetime import datetime # Zastosowanie: Standardowa biblioteka do manipulacji datami i czasem.
now = datetime.now()
print(now)

from datetime import datetime, timedelta # Zastosowanie: Zawiera funkcje pomocnicze do obliczania różnicy między datami (czas, dni, godziny, minuty).
now = datetime.now()
future = now + timedelta(days=5)
print(future)
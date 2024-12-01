import numpy as np
arr = np.array([1, 2, 3])
print(arr.mean())  # Wynik: 2.0

import pandas as pd
df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
print(df.describe())

# requests: HTTP API i pobieranie danych z internetu
import requests
response = requests.get("https://example.com")
print(response.text)

# selenium: Automatyzacja przeglądarek internetowych
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.example.com')

# bs4: Web scraping
from bs4 import BeautifulSoup
import requests
url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
titles = soup.find_all('h1')
for title in titles:
    print(title.text)

# datetime: Standardowa biblioteka do manipulacji datami i czasem
from datetime import datetime
now = datetime.now()
print(now)

# timedelta: Zawiera funkcje pomocnicze do obliczania różnicy między datami (czas, dni, godziny, minuty)
from datetime import datetime, timedelta
now = datetime.now()
future = now + timedelta(days=5)
print(future)

# pytest: Testy jednostkowe, funkcyjne i integracyjne
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# mypy: Statyczne typowanie
def greet(name: str) -> str:
    return f"Hello, {name}!"
greet(123)  # Błąd typowania
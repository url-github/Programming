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

# time:

import time

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

# typing: Statyczne typowanie
# Moduł standardowy w Pythonie, służący do dodawania adnotacji typów w kodzie.
from typing import List

def add_numbers(numbers: List[int]) -> int:
    return sum(numbers)

print(add_numbers([1, 2, 3]))  # Poprawne
# print(add_numbers(["a", "b"]))  # Błąd wykrywany przez narzędzia analizy statycznej

# mypy: Statyczne typowanie
# Narzędzie zewnętrzne do analizy statycznej kodu Pythona. Wykorzystuje adnotacje typów (dodane np. za pomocą modułu typing) i sprawdza, czy kod jest zgodny z zadeklarowanymi typami.
def greet(name: str) -> str:
    return f"Hello, {name}!"
greet(123)  # Błąd typowania

# os: zapewnia funkcje do interakcji z systemem operacyjnym
import os
print(os.listdir(r"/Users/p/Documents/Scripts/Programming/040-recursively-listing-the-contents-of-a-directory/testowy"))
# ['b.txt', 'a.txt', 'zagniezdzony']
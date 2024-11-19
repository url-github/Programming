import os

webaddresses = []
line = input('Enter web address like "www.python.org" or press ENTER to stop: ')

# Pętla do wprowadzania adresów
while line != '':
    webaddresses.append(line)  # Dodaj adres do listy
    line = input('Enter web address like "www.python.org" or press ENTER to stop: ')

print(webaddresses)  # Wyświetlenie listy wprowadzonych adresów

dirname = os.getcwd()  # Pobranie aktualnego katalogu roboczego
filename = input("Enter the file name (without directory): ")
filepath = os.path.join(dirname, filename)  # Utworzenie pełnej ścieżki do pliku

# Otwieranie pliku w trybie zapisu z możliwością odczytu (w+)
file = open(filepath, 'w+')
for webaddress in webaddresses:
    file.write(webaddress + "\n")  # Zapis adresów do pliku
file.close()  # Zamknięcie pliku
# Pytanie 6 - jakiej struktury danych użyłbyś do zapisania numerów telefonów
# wszystkich klientów firmy i odpowiadających im nazwisk. Wybierz strukturę tak,
# aby sprawdzenie właściciela numeru telefonu nie zajmowało dużo czasu.

D = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5} # O(1)

L = [1, 2, 3, 4, 5] # O(N)

if 4 in L:
	print("tak")
else:
	print('nie')

D = {123456789:'Jan Kot', 999888777:'Anna Lis', 111222333:'Jan Kot'}

print(D[123456789]) # odczytanie elementu słownika D znajdującego się pod kluczem 123456789

# złożoność obliczeniowa wyszukania elementu w liście N-elementowej: O(N)
# złożoność obliczeniowa wyszukania elementu w słowniku N-elementowym: O(1) - lepsza!
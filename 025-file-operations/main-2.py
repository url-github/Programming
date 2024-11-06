# Otwórz, przeczytaj i wydrukuj zawartość pliku "przeczytaj_mnie.txt"
# Aby rozkodować polskie znaki w funkcji open(), po parametrze 'r' należy dodać jeszcze jeden parametr: 'encoding=utf-8'.


with open('przeczytaj_mnie.txt','r', encoding='utf-8') as f:
    print(f.read())
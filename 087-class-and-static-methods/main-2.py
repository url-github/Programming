import pickle  # Do zapisu i odczytu obiektów na dysk
import glob    # Do wyszukiwania plików o określonym rozszerzeniu

class Cake:
    bakery_offer = []  # Lista przechowująca wszystkie obiekty Cake

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.gluten_free = gluten_free
        self.text = text
        Cake.bakery_offer.append(self)

    def show_info(self):
        """Wyświetla szczegółowe informacje o cieście."""
        print(f"Name: {self.name.upper()}")
        print(f"Kind: {self.kind}")
        print(f"Taste: {self.taste}")
        print(f"Additives: {', '.join(self.additives) if self.additives else 'None'}")
        print(f"Filling: {self.filling if self.filling else 'None'}")
        print(f"Gluten-free: {self.gluten_free}")
        print(f"Text: {self.text if self.text else 'None'}")
        print('-' * 20)

    def save_to_file(self, path):
        """Zapisuje obiekt instancji Cake do pliku."""
        with open(path, 'wb') as f:
            pickle.dump(self, f)
        print(f"Object {self.name} saved to {path}")

    @classmethod
    def read_from_file(cls, path):
        """Wczytuje obiekt Cake z pliku i dodaje go do bakery_offer."""
        with open(path, 'rb') as f:
            cake = pickle.load(f)
        cls.bakery_offer.append(cake)
        print(f"Object {cake.name} loaded from {path}")
        return cake

    @staticmethod
    def get_bakery_files(directory):
        """Zwraca listę plików z rozszerzeniem .bakery w podanym katalogu."""
        return glob.glob(f"{directory}/*.bakery")


# Tworzenie obiektów
cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate chips'], 'cream', False, 'Happy Birthday')
cake02 = Cake('Chocolate Muffin', 'muffin', 'chocolate', [], None, True, '')

# Testowanie zapisu do plików
cake01.save_to_file('vanilla_cake.bakery')
cake02.save_to_file('chocolate_muffin.bakery')

# Testowanie odczytu z pliku
cake05 = Cake.read_from_file('vanilla_cake.bakery')
cake05.show_info()

# Testowanie funkcji statycznej do pobierania plików
bakery_files = Cake.get_bakery_files('.')
print("Bakery files:", bakery_files)
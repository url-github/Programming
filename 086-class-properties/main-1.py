'''Getter i Setter to metody w programowaniu obiektowym używane do:
- uzyskiwania dostępu do prywatnych atrybutów klasy (getter)
- oraz zmiany ich wartości (setter).
Są one stosowane, aby lepiej kontrolować dostęp do atrybutów obiektów i zapewnić enkapsulację.'''

markaNaSprzedaz = 'Opel'

class Samochod:
    liczbaSamochodow = 0  # Atrybuty klasy
    listaSamochodow = []  # Atrybuty klasy

    def __init__(self, marka, model, czyPoduszkaOK, czyLakierOK, czyMechanikaOK, czyNaSprzedaz):
        # Metoda inicjalizująca obiekt klasy Samochod
        self.marka = marka  # Atrybuty lub właściwości klasy Samochod
        self.model = model
        self.czyPoduszkaOK = czyPoduszkaOK
        self.czyLakierOK = czyLakierOK
        self.czyMechanikaOK = czyMechanikaOK
        self.__czyNaSprzedaz = czyNaSprzedaz  # Ukryty atrybut
        Samochod.liczbaSamochodow += 1
        Samochod.listaSamochodow.append(self)

    def czyUszkodzony(self):
        # Metoda sprawdzająca, czy samochód jest uszkodzony
        return not (self.czyPoduszkaOK and self.czyMechanikaOK and self.czyLakierOK)

    def pokazInformacje(self):
        # Metoda wyświetlająca informacje o samochodzie
        print("{} {}".format(self.marka, self.model).upper())
        print("Poduszka powietrzna - OK - {}".format(self.czyPoduszkaOK))
        print("Lakier - OK - {}".format(self.czyLakierOK))
        print("Mechanika - OK - {}".format(self.czyMechanikaOK))
        print("NA SPRZEDAŻ - {}".format(self.__czyNaSprzedaz))
        print("-------------------")

    def GetIsOnSale(self):
        # Getter dla atrybutu __czyNaSprzedaz
        return self.__czyNaSprzedaz

    def SetIsOnSale(self, newIsOnSaleStatus):
        # Setter dla atrybutu __czyNaSprzedaz
        if self.marka == markaNaSprzedaz:
            self.__czyNaSprzedaz = newIsOnSaleStatus
            print("Changing status IsOnSale to {} for {}".format(newIsOnSaleStatus, self.marka))
        else:
            print("Cannot change status IsOnSale. Sale valid only for {}".format(markaNaSprzedaz))


# Tworzenie instancji klasy Samochod
samochod_01 = Samochod('Seat', 'Ibiza', True, True, True, False)
samochod_02 = Samochod('Opel', 'Astra', True, False, True, True)

# Wyświetlenie początkowego statusu
print("Status of cars:", samochod_01.GetIsOnSale(), samochod_02.GetIsOnSale())
samochod_01.SetIsOnSale(True)
samochod_02.SetIsOnSale(False)
# Wyświetlenie końcowego statusu
print("Status of cars:", samochod_01.GetIsOnSale(), samochod_02.GetIsOnSale())



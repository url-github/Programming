class Ciasto:

    znane_typy = ['ciasto', 'muffin', 'beza', 'biszkopt', 'eclair', 'świąteczne', 'precel', 'inne']
    oferta_cukierni = []

    def __init__(self, nazwa, typ, smak, dodatki, nadzienie, bezglutenowe):
        self.nazwa = nazwa
        if typ in self.znane_typy:
            self.typ = typ
        else:
            self.typ = 'inne'
        self.smak = smak
        self.dodatki = dodatki.copy()
        self.nadzienie = nadzienie
        self.oferta_cukierni.append(self)
        self.__bezglutenowe = bezglutenowe

    def pokaz_informacje(self):
        print("{}".format(self.nazwa.upper()))
        print("Typ:          {}".format(self.typ))
        print("Smak:         {}".format(self.smak))
        if len(self.dodatki) > 0:
            print("Dodatki:")
            for d in self.dodatki:
                print("\t\t{}".format(d))
        if len(self.nadzienie) > 0:
            print("Nadzienie:    {}".format(self.nadzienie))
        print("Bezglutenowe: {}".format(self.__bezglutenowe))
        print('-'*20)

    def ustaw_nadzienie(self, nadzienie):
        self.nadzienie = nadzienie

    def dodaj_dodatki(self, dodatki):
        self.dodatki.extend(dodatki)


ciasto01 = Ciasto('Ciasto Waniliowe', 'ciasto', 'wanilia', ['czekolada', 'orzechy'], 'krem', False)
ciasto02 = Ciasto('Muffin Czekoladowy', 'muffin', 'czekolada', ['czekolada'], '', False)
ciasto03 = Ciasto('Super Słodka Beza', 'beza', 'bardzo słodka', [], '', True)
ciasto04 = Ciasto('Gofr Kakaowy', 'inne', 'kakao', [], 'kakao', False)

print("Dzisiaj w naszej ofercie:")
for c in Ciasto.oferta_cukierni:
    c.pokaz_informacje()

ciasto03.__bezglutenowe = False
print(dir(ciasto03))
ciasto03._Ciasto__bezglutenowe = False
ciasto03.pokaz_informacje()
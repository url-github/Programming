class Ciasto:

    def __init__(self, nazwa, rodzaj, smak, dodatki, nadzienie):
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.smak = smak
        self.dodatki = dodatki.copy()
        self.nadzienie = nadzienie

ciasto01 = Ciasto('Tort Waniliowy', 'tort', 'wanilia', ['czekolada', 'orzechy'], 'krem')
ciasto02 = Ciasto('Muffinka Czekoladowa', 'muffinka', 'czekolada', ['czekolada'], '')
ciasto03 = Ciasto('Super Słodka Beza', 'beza', 'bardzo słodka', [], '')

oferta_cukierni = []
oferta_cukierni.append(ciasto01)
oferta_cukierni.append(ciasto02)
oferta_cukierni.append(ciasto03)

print("Dziś w naszej ofercie:")
for c in oferta_cukierni:
    print("{} - ({}) główny smak: {} z dodatkami: {}, nadziane: {}".format(
        c.nazwa, c.rodzaj, c.smak, c.dodatki, c.nadzienie))

# Dziś w naszej ofercie:
# Tort Waniliowy - (tort) główny smak: wanilia z dodatkami: ['czekolada', 'orzechy'], nadziane: krem
# Muffinka Czekoladowa - (muffinka) główny smak: czekolada z dodatkami: ['czekolada'], nadziane:
# Super Słodka Beza - (beza) główny smak: bardzo słodka z dodatkami: [], nadziane:
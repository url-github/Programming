class Zwierze:
    def przedstaw_sie(self):
        print("Jestem jakimś zwierzeciem.")
    def daj_glos(self):
        print("Nie wiem czym jestem i jaki dźwięk wydaję.")

class Gawron(Zwierze):
    def daj_glos(self):
        print("Kraaa kraaa!")

g = Gawron()
g.przedstaw_sie()
g.daj_glos()
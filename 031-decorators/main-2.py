def wypisz_efekt_dzialania(funkcja):
    def funkcja_udekorowana():
        a = funkcja()
        print(a)
        print(a)
    return funkcja_udekorowana

@wypisz_efekt_dzialania
def zwroc_czesc():
    return "cześć"

zwroc_czesc()







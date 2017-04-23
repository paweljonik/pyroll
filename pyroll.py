from decimal import getcontext, Decimal, ROUND_HALF_UP
getcontext().prec = 5
getcontext().rounding = ROUND_HALF_UP


# Input base value for calculations:
kwota = Decimal(input("\n Podaj kwote brutto (w PLN): "))

# Calculate variables based on input:
UbezpieczenieEmerytalne = Decimal(0.0976) * Decimal(kwota)
UbezpieczenieRentowe = Decimal(0.0150) * kwota
UbezpieczenieChorobowe = Decimal(0.0245) * kwota
WynagrodzenieZasadnicze = kwota - UbezpieczenieEmerytalne - UbezpieczenieRentowe - UbezpieczenieChorobowe
KosztyUzyskaniaPrzychodu = Decimal(111.2500)    # 1)
if (WynagrodzenieZasadnicze - KosztyUzyskaniaPrzychodu) > 0:
    Dochod = round(Decimal(WynagrodzenieZasadnicze) - KosztyUzyskaniaPrzychodu,0)
else:
    Dochod = round(Decimal(0),0)
ZaliczkaNaPodatek = Decimal(0.18) * Dochod    # 2)
MiesiecznaUlgaNaPodatek = 46.33
if MiesiecznaUlgaNaPodatek < ZaliczkaNaPodatek:
    ZaliczkaNaPodatekPoOdjeciuUlgi = Decimal(ZaliczkaNaPodatek) - Decimal(MiesiecznaUlgaNaPodatek)
else:
    ZaliczkaNaPodatekPoOdjeciuUlgi = Decimal(0)
UbezpieczenieZdrowotne = Decimal(0.09) * Decimal(WynagrodzenieZasadnicze)
UbezpieczenieZdrowotneDoZUS	= Decimal(0.09) * Decimal(WynagrodzenieZasadnicze)
UbezpieczenieZdrowotneDoOdliczeniaCale = Decimal(0.0775) * Decimal(WynagrodzenieZasadnicze)
if UbezpieczenieZdrowotneDoOdliczeniaCale < ZaliczkaNaPodatekPoOdjeciuUlgi:
    UbezpieczenieZdrowotnePodlegajaceOdliczeniu = Decimal(UbezpieczenieZdrowotneDoOdliczeniaCale)    # 7.75%
else:
    UbezpieczenieZdrowotnePodlegajaceOdliczeniu = Decimal(ZaliczkaNaPodatekPoOdjeciuUlgi)
ZaliczkaNaPodatekDochodowyDoZaplaty = Decimal(ZaliczkaNaPodatekPoOdjeciuUlgi) - UbezpieczenieZdrowotnePodlegajaceOdliczeniu    # 2)
KwotaDoWyplatyPracownikowi = kwota - UbezpieczenieEmerytalne - UbezpieczenieRentowe - UbezpieczenieChorobowe - UbezpieczenieZdrowotneDoZUS - ZaliczkaNaPodatekDochodowyDoZaplaty
# # KwotyUbezpieczeniaPlaconePrzezPracodawce = Decimal()
UbezpieczenieEmerytalne_PlaconePrzezPracodawce = Decimal(0.0976) * kwota    # 9.76%
UbezpieczenieRentowe_PlaconePrzezPracodawce = Decimal(0.045) * kwota    # 4.50%
UbezpieczenieWypadkowe_PlaconePrzezPracodawce = Decimal(0.0167) * kwota    # 1.67%     3)
SkladkaNaFP_PlaconePrzezPracodawce = Decimal(0.0245) * kwota  # 2.45%
SkladkaNaFGSP_PlaconePrzezPracodawce = Decimal(0) * kwota      #   4)

SumaWszystkichSkladekZUS = UbezpieczenieEmerytalne + UbezpieczenieRentowe + UbezpieczenieChorobowe + UbezpieczenieZdrowotneDoZUS + UbezpieczenieEmerytalne_PlaconePrzezPracodawce + UbezpieczenieRentowe_PlaconePrzezPracodawce + UbezpieczenieWypadkowe_PlaconePrzezPracodawce + SkladkaNaFP_PlaconePrzezPracodawce + SkladkaNaFGSP_PlaconePrzezPracodawce
# w tym:
SumaWszystkichSkladekZUSZeSrodkowPracownika = UbezpieczenieEmerytalne + UbezpieczenieRentowe + UbezpieczenieChorobowe + UbezpieczenieZdrowotneDoZUS
SumaWszystkichSkladekZUSZeSrodkowPracodawcy	= UbezpieczenieEmerytalne_PlaconePrzezPracodawce + UbezpieczenieRentowe_PlaconePrzezPracodawce + UbezpieczenieWypadkowe_PlaconePrzezPracodawce + SkladkaNaFP_PlaconePrzezPracodawce + SkladkaNaFGSP_PlaconePrzezPracodawce

CalkowityKosztWyplaty = kwota + UbezpieczenieEmerytalne_PlaconePrzezPracodawce + UbezpieczenieRentowe_PlaconePrzezPracodawce + UbezpieczenieWypadkowe_PlaconePrzezPracodawce + SkladkaNaFP_PlaconePrzezPracodawce + SkladkaNaFGSP_PlaconePrzezPracodawce

# Output calculations:
print(" ")
print(' Ubezpieczenie Emerytalne: ' + str(UbezpieczenieEmerytalne)+ ' PLN')
print(' Ubezpieczenie Rentowe: ' + str(UbezpieczenieRentowe)+ ' PLN')
print(' Ubezpieczenie Chorobowe: ' + str(UbezpieczenieChorobowe)+ ' PLN')
print(' Wynagrodzenie Zasadnicze: ' + str(WynagrodzenieZasadnicze)+ ' PLN')
print(' Koszty Uzyskania Przychodu: ' + str(KosztyUzyskaniaPrzychodu)+ ' PLN')
print(' Dochod: ' + str(Dochod)+ ' PLN')
print(' Zaliczka Na Podatek: ' + str(ZaliczkaNaPodatek)+ ' PLN')
print(' Miesieczna Ulga Na Podatek: ' + str(MiesiecznaUlgaNaPodatek)+ ' PLN')
print(' Zaliczka Na Podatek Po Odjeciu Ulgi: ' + str(ZaliczkaNaPodatekPoOdjeciuUlgi)+ ' PLN')
print(' Ubezpieczenie Zdrowotne: ' + str(UbezpieczenieZdrowotne)+ ' PLN')
print(' Ubezpieczenie Zdrowotne Do ZUS: ' + str(UbezpieczenieZdrowotneDoZUS)+ ' PLN')
print(' Ubezpieczenie Zdrowotne Do Odliczenia Cale: ' + str(UbezpieczenieZdrowotneDoOdliczeniaCale)+ ' PLN')
print(' Ubezpieczenie Zdrowotne Podlegajace Odliczeniu: ' + str(UbezpieczenieZdrowotnePodlegajaceOdliczeniu)+ ' PLN')
print(' Zaliczka Na Podatek Dochodowy Do Zaplaty: ' + str(ZaliczkaNaPodatekDochodowyDoZaplaty)+ ' PLN')
print(' Kwota Do Wyplaty Pracownikowi: ' + str(KwotaDoWyplatyPracownikowi)+ ' PLN')
print("\nKwoty Ubezpieczenia Placone Przez Pracodawce:")
print(' - Ubezpieczenie Emerytalne: ' + str(UbezpieczenieEmerytalne_PlaconePrzezPracodawce)+ ' PLN')
print(' - Ubezpieczenie Rentowe: ' + str(UbezpieczenieRentowe_PlaconePrzezPracodawce)+ ' PLN')
print(' - Ubezpieczenie Wypadkowe: ' + str(UbezpieczenieWypadkowe_PlaconePrzezPracodawce)+ ' PLN')
print(' - Skladka Na FP Placone: ' + str(SkladkaNaFP_PlaconePrzezPracodawce)+ ' PLN')
print(' - Skladka Na FGSP: ' + str(SkladkaNaFGSP_PlaconePrzezPracodawce)+ ' PLN')
print("\n" + 'Suma Wszystkich Skladek ZUS: ' + str(SumaWszystkichSkladekZUS)+ ' PLN')
print(' - Suma Wszystkich Skladek ZUS Ze Srodkow Pracownika: ' + str(SumaWszystkichSkladekZUSZeSrodkowPracownika)+ ' PLN')
print(' - Suma Wszystkich Skladek ZUS Ze Srodkow Pracodawcy: ' + str(SumaWszystkichSkladekZUSZeSrodkowPracodawcy)+ ' PLN')
print("\n")
print('Calkowity Koszt Wyplaty: ' + str(CalkowityKosztWyplaty)+ ' PLN')

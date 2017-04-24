#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module calculates all the money you won't see after your pay-check."""

from decimal import getcontext, Decimal, ROUND_HALF_UP
getcontext().prec = 5
getcontext().rounding = ROUND_HALF_UP

# Input base value for calculations:
KWOTA = Decimal(input("\n Podaj kwote brutto (w PLN): "))

# Calculate variables based on input:
UbezpieczenieEmerytalne = Decimal(0.0976) * Decimal(KWOTA)
UbezpieczenieRentowe = Decimal(0.0150) * KWOTA
UbezpieczenieChorobowe = Decimal(0.0245) * KWOTA
WynagrodzenieZasadnicze = \
    KWOTA \
    - UbezpieczenieEmerytalne \
    - UbezpieczenieRentowe \
    - UbezpieczenieChorobowe
KosztyUzyskaniaPrzychodu = Decimal(111.2500)    # 1)
if (WynagrodzenieZasadnicze - KosztyUzyskaniaPrzychodu) > 0:
    Dochod = \
        round(Decimal(WynagrodzenieZasadnicze) \
        - KosztyUzyskaniaPrzychodu, 0)
else:
    Dochod = round(Decimal(0), 0)
ZaliczkaNaPodatek = Decimal(0.18) * Decimal(Dochod)    # 2)
MiesiecznaUlgaNaPodatek = 46.33
if MiesiecznaUlgaNaPodatek < ZaliczkaNaPodatek:
    ZaliczkaNaPodatekPoOdjeciuUlgi = \
        Decimal(ZaliczkaNaPodatek) \
        - Decimal(MiesiecznaUlgaNaPodatek)
else:
    ZaliczkaNaPodatekPoOdjeciuUlgi = Decimal(0)
UbezpieczenieZdrowotne = Decimal(0.09) * Decimal(WynagrodzenieZasadnicze)
UbezpieczenieZdrowotneDoZUS	= Decimal(0.09) * Decimal(WynagrodzenieZasadnicze)
UbezpieczenieZdrowotneDoOdliczeniaCale = Decimal(0.0775) * Decimal(WynagrodzenieZasadnicze)
if UbezpieczenieZdrowotneDoOdliczeniaCale < ZaliczkaNaPodatekPoOdjeciuUlgi:
    UbezpieczenieZdrowotnePodlegajaceOdliczeniu = \
        Decimal(UbezpieczenieZdrowotneDoOdliczeniaCale)    # 7.75%
else:
    UbezpieczenieZdrowotnePodlegajaceOdliczeniu = Decimal(ZaliczkaNaPodatekPoOdjeciuUlgi)
ZaliczkaNaPodatekDochodowyDoZaplaty = Decimal(ZaliczkaNaPodatekPoOdjeciuUlgi) - \
    UbezpieczenieZdrowotnePodlegajaceOdliczeniu    # 2)
KWOTADoWyplatyPracownikowi = KWOTA - UbezpieczenieEmerytalne - UbezpieczenieRentowe - \
    UbezpieczenieChorobowe - UbezpieczenieZdrowotneDoZUS - ZaliczkaNaPodatekDochodowyDoZaplaty
# # KwotyUbezpieczeniaPlaconePrzezPracodawce = Decimal()
UbezpieczenieEmerytalne_PlaconePrzezPracodawce = Decimal(0.0976) * KWOTA    # 9.76%
UbezpieczenieRentowe_PlaconePrzezPracodawce = Decimal(0.045) * KWOTA    # 4.50%
UbezpieczenieWypadkowe_PlaconePrzezPracodawce = Decimal(0.0167) * KWOTA    # 1.67%     3)
SkladkaNaFP_PlaconePrzezPracodawce = Decimal(0.0245) * KWOTA  # 2.45%
SkladkaNaFGSP_PlaconePrzezPracodawce = Decimal(0) * KWOTA      #   4)

SumaWszystkichSkladekZUS = \
    UbezpieczenieEmerytalne \
    + UbezpieczenieRentowe \
    + UbezpieczenieChorobowe \
    + UbezpieczenieZdrowotneDoZUS \
    + UbezpieczenieEmerytalne_PlaconePrzezPracodawce \
    + UbezpieczenieRentowe_PlaconePrzezPracodawce \
    + UbezpieczenieWypadkowe_PlaconePrzezPracodawce \
    + SkladkaNaFP_PlaconePrzezPracodawce \
    + SkladkaNaFGSP_PlaconePrzezPracodawce
# w tym:
SumaWszystkichSkladekZUSZeSrodkowPracownika = UbezpieczenieEmerytalne + UbezpieczenieRentowe + \
    UbezpieczenieChorobowe + UbezpieczenieZdrowotneDoZUS
SumaWszystkichSkladekZUSZeSrodkowPracodawcy	= \
    UbezpieczenieEmerytalne_PlaconePrzezPracodawce \
    + UbezpieczenieRentowe_PlaconePrzezPracodawce \
    + UbezpieczenieWypadkowe_PlaconePrzezPracodawce \
    + SkladkaNaFP_PlaconePrzezPracodawce \
    + SkladkaNaFGSP_PlaconePrzezPracodawce

CalkowityKosztWyplaty = \
    KWOTA \
    + UbezpieczenieEmerytalne_PlaconePrzezPracodawce \
    + UbezpieczenieRentowe_PlaconePrzezPracodawce \
    + UbezpieczenieWypadkowe_PlaconePrzezPracodawce \
    + SkladkaNaFP_PlaconePrzezPracodawce \
    + SkladkaNaFGSP_PlaconePrzezPracodawce

# Output calculations:
print(" ")
print(' Ubezpieczenie emerytalne: ' + str(UbezpieczenieEmerytalne)+ ' PLN')
print(' Ubezpieczenie rentowe: ' + str(UbezpieczenieRentowe)+ ' PLN')
print(' Ubezpieczenie chorobowe: ' + str(UbezpieczenieChorobowe)+ ' PLN')
print(' Wynagrodzenie zasadnicze: ' + str(WynagrodzenieZasadnicze)+ ' PLN')
print(' Koszty uzyskania przychodu: ' + str(KosztyUzyskaniaPrzychodu)+ ' PLN')
print(' Dochód: ' + str(Dochod)+ ' PLN')
print(' Zaliczka na podatek: ' + str(ZaliczkaNaPodatek)+ ' PLN')
print(' Miesięczna ulga na podatek: ' + str(MiesiecznaUlgaNaPodatek)+ ' PLN')
print(' Zaliczka na podatek po odjęciu ulgi: ' + str(ZaliczkaNaPodatekPoOdjeciuUlgi)+ ' PLN')
print(' Ubezpieczenie zdrowotne: ' + str(UbezpieczenieZdrowotne)+ ' PLN')
print(' Ubezpieczenie zdrowotne do ZUS: ' + str(UbezpieczenieZdrowotneDoZUS)+ ' PLN')
print(' Ubezpieczenie zdrowotne do odliczenia całe: ' + str(UbezpieczenieZdrowotneDoOdliczeniaCale)+ ' PLN')
print(' Ubezpieczenie zdrowotne podlegajace odliczeniu: ' + str(UbezpieczenieZdrowotnePodlegajaceOdliczeniu)+ ' PLN')
print(' Zaliczka na podatek dochodowy do zapłaty: ' + str(ZaliczkaNaPodatekDochodowyDoZaplaty)+ ' PLN')
print(' Kwota do wypłaty pracownikowi: ' + str(KWOTADoWyplatyPracownikowi)+ ' PLN')
print("\nKwoty ubezpieczenia płacone przez pracodawcę:")
print(' - Ubezpieczenie emerytalne: ' + str(UbezpieczenieEmerytalne_PlaconePrzezPracodawce)+ ' PLN')
print(' - Ubezpieczenie rentowe: ' + str(UbezpieczenieRentowe_PlaconePrzezPracodawce)+ ' PLN')
print(' - Ubezpieczenie wypadkowe: ' + str(UbezpieczenieWypadkowe_PlaconePrzezPracodawce)+ ' PLN')
print(' - Składka na FP płacone: ' + str(SkladkaNaFP_PlaconePrzezPracodawce)+ ' PLN')
print(' - Składka na FGSP: ' + str(SkladkaNaFGSP_PlaconePrzezPracodawce)+ ' PLN')
print("\n" + 'Suma wszystkich składek ZUS: ' + str(SumaWszystkichSkladekZUS)+ ' PLN')
print(' - Suma wszystkich składek ZUS ze środków pracownika: ' + str(SumaWszystkichSkladekZUSZeSrodkowPracownika)+ ' PLN')
print(' - Suma wszystkich składek ZUS ze środków pracodawcy: ' + str(SumaWszystkichSkladekZUSZeSrodkowPracodawcy)+ ' PLN')
print("\n")
print('Całkowity koszt wypłaty: ' + str(CalkowityKosztWyplaty)+ ' PLN')
print("\n")
print("Aktualna wersja bazuje na nie koniecznie aktualnych danych. Trust no one ;-). It's just a test.")

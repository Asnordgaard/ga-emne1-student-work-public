# 13. Bygg en setning
# Hensikt: Kombinere flere tekstverdier.
# Oppgave: Be brukeren skrive inn to adjektiv, ett substantiv og ett verb. Lag deretter en grammatisk fullstendig setning som inneholder alle fire svarene. Du bestemmer rekkefølgen, men setningen skal ha stor bokstav og punktum.
# Leveranse: Et program som bruker alle fire svar.
# Hint: Bruk én variabel per svar og en f-streng.
# Kontrollpunkt: Inneholder outputen alle fire ordene?

adjektiv1 = input("Skriv inn et adjektiv: ")
adjektiv2 = input("Skriv inn et nytt adjektiv: ")
substantiv = input("Skriv in et substantiv: ")
verb = input("Skriv inn et verb: ")

print(f"{substantiv.capitalize()} er {adjektiv1} og {adjektiv2} å {verb}.")
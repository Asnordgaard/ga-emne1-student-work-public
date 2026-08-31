# 12. Beregn ukelønn
# Hensikt: Modellere en praktisk beregning.
# Oppgave: Les inn timepris og arbeidede timer, og beregn ukelønnen.
# Leveranse: Tre tester med kontrollregninger.
# Hint: Bruk en egen resultatvariabel.
# Kontrollpunkt: Dobles lønnen hvis timene dobles?


hourly_rate = float(input("Skriv inn timepris i NOK: "))
hours_worked = float(input("Antall timer jobbet: "))
payout = hourly_rate * hours_worked

print(f"Ukelønn denne uka er kr. {payout:.2f}!")

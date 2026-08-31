# 10. Tips og totalpris
# Hensikt: Bruke prosentregning.
# Oppgave: Les inn en pris, beregn 15 prosent tips og skriv ut tips og totalpris.
# Leveranse: Tre tester med kontrollregninger.
# Hint: Regn ut tipsbeløpet først.
# Kontrollpunkt: Er totalen lik pris pluss tips?

price = float(input("Pris: "))
tip = price * 0.15
total = price + tip

print(f"Total pris, inkludert 15% tips (NOK {tip:.2f}), er NOK {total:.2f}")


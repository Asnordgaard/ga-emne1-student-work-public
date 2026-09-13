# Oppgave: Les inn kjørelengde i kilometer, drivstofforbruk per 100 kilometer og drivstoffpris per liter. Beregn drivstoffmengden med kjørelengde / 100 * forbruk per 100 kilometer, og beregn deretter kostnaden. Bruk engelske variabelnavn, for eksempel distance, fuel_per_100_km og fuel_price.
# Forventet leveranse: Ett program som skriver ut drivstoffmengde og kostnad med forklarende tekst.
# Hint: Konverter input før du regner, og lagre mellomresultatet.
# Kontrollpunkt: Test minst to kjørelengder og kontroller beregningen manuelt.

distance_in_km = int(input("Skriv inn kjørelengde i kilometer: "))
fuel_per_100_km = float(input("Forbruk i liter per 100 km: "))
fuel_price = float(input("Drivstoffpris: "))

fuel_consumption = distance_in_km / 100 * fuel_per_100_km
cost = fuel_consumption * fuel_price

print(f"Drivstoffmengde forbrukt: {fuel_consumption:.2f}")
print(f"Total kostnad: {cost:.2f}")

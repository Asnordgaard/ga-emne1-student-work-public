# 9. Minutter til timer og minutter
# Hensikt: Dele en verdi i to resultater.
# Oppgave: Be brukeren skrive inn et helt antall minutter. Beregn hvor mange hele timer dette tilsvarer, og hvor mange minutter som blir igjen. Skriv ut begge resultatene.
# Leveranse: Test med 60, 95 og 135 minutter.
# Hint: Bruk // for å finne hele timer og % for å finne resterende minutter.
# Kontrollpunkt: Gir 60 minutter 1 time og 0 minutter?

minutes = int(input("Skriv antall minutter (uten komma): "))
hours = minutes // 60
rest_minutes = minutes % 60

print(f"{minutes} minutter er: {hours} timer og {rest_minutes} minutter")

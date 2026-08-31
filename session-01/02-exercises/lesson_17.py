# 17. Sekunder til timer, minutter og sekunder
# Hensikt: Dele en beregning i flere trinn.
# Oppgave: Be brukeren skrive inn et helt antall sekunder. Beregn først hele timer. Bruk deretter sekunder som er igjen til å beregne hele minutter og resterende sekunder. Skriv ut alle tre verdiene.
# Leveranse: Fire tester, inkludert 0 og 3661.
# Hint: Bruk // for hele enheter og % for resten etter hvert trinn.
# Kontrollpunkt: Gir 3661 sekunder 1 time, 1 minutt og 1 sekund?


seconds = int(input("Skriv antall sekunder: "))
hours = seconds // 3600
minutes = hours % 60
seconds_remaining = seconds % 60

print(f"{seconds} sekunder tilsvarer {hours} time(r), {minutes} minutt(er) og {seconds_remaining} sekund(er).")
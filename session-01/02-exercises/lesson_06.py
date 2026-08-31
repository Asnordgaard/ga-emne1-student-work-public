# 6. Finn gjennomsnittet
# Hensikt: Kombinere addisjon, divisjon og desimaltall.
# Oppgave: Be om to tall, finn gjennomsnittet og skriv ut resultatet.
# Leveranse: Et program testet med heltall og desimaltall.
# Hint: Del summen på antallet tall.
# Kontrollpunkt: Ligger gjennomsnittet mellom tallene?

number_1 = float(input("Skriv et hvilket som helst tall: "))
number_2 = float(input("Skriv et hvilket som helst annet tall: "))
average = (number_1 + number_2) / 2

print(f"Gjennomsnittet av de to tallene er: {average:.2f}")
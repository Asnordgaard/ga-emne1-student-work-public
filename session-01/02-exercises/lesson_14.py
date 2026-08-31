# 14. Enkel valutaomregning
# Hensikt: Bruke en kurs i en beregning.
# Oppgave: Be brukeren skrive inn et beløp og en kurs. La kursen bety hvor mange enheter av målvalutaen én enhet av startvalutaen er verdt. Beregn målbeløpet som beløp * kurs, og skriv ut resultatet.
# Leveranse: Et program testet med tre oppdiktede kurser. Oppgi tydelig at kursene bare er testdata.
# Hint: Les begge verdiene som float().
# Kontrollpunkt: Gir kursen 1 samme beløp?


amount = float(input("Skriv inn beløp: "))
exchange_rate = float(input("Skriv inn valutakurs for én enhet: "))
exchanged_value = amount * exchange_rate

print(f"{amount} tilsvarer {exchanged_value:.2f} når kursen er {exchange_rate:.2f}. Merk at dette ikke er en reell kurs!")


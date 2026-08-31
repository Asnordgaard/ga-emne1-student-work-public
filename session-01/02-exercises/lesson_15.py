# 15. Mini-prosjekt: totalpris
# Hensikt: Kombinere input, typekonvertering, beregning og f-streng.
# Oppgave: Les inn produktnavn, enhetspris og antall. Beregn totalprisen og skriv ut produktnavn og totalpris.
# Leveranse: Et program med tre dokumenterte tester.
# Hint: Bruk float() for pris og int() for antall.
# Kontrollpunkt: Stemmer resultatene med kontrollregningene?

product_name = input("Produktnavn: ")
price = float(input("Pris per enhet: "))
number_of_items = int(input("Antall enheter: "))
total = price * number_of_items

print(f"Totalpris for {number_of_items} stk. {product_name.capitalize()} er kr. {total:.2f}.")
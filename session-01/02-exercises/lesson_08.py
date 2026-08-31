# 8. Fahrenheit til Celsius
# Hensikt: Tilpasse en beregning og kontrollere den.
# Oppgave: Les inn Fahrenheit og beregn Celsius med (fahrenheit - 32) * 5 / 9.
# Leveranse: Et program med tre testverdier.
# Hint: Behold parentesene.
# Kontrollpunkt: Gir 32 °F resultatet 0 °C?


degrees_fahrenheit = int(input("Skriv inn antall grader Fahrenheit: "))
convert_from_fahrenheit_to_celsius = (degrees_fahrenheit -32) * 5 / 9

print(f"Det tilsvarer {convert_from_fahrenheit_to_celsius:.0f} grader Celsius")
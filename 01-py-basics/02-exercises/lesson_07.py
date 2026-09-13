# 7. Celsius til Fahrenheit
# Hensikt: Bruke en oppgitt formel med desimaltall.
# Oppgave: Les inn Celsius og beregn Fahrenheit med celsius * 9 / 5 + 32.
# Leveranse: Et program med tre testverdier.
# Hint: Bruk float().
# Kontrollpunkt: Gir 0 °C resultatet 32 °F?

degrees_celsius = int(input("Hvor mange grader celsius er det? "))
convert_celsius_to_fahrenheit = degrees_celsius * 9 / 5 + 32

print(f"Det tilsvarer {convert_celsius_to_fahrenheit:.0f} grader Fahrenheit")
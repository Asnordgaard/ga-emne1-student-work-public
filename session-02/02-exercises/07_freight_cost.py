weight = 10.1 # float(input("Skriv inn vekt på pakken: "))

if weight <= 2:
    print(f"Pris for å sende pakken blir {weight * 79:.2f}")
elif weight <= 5:
    print(f"Pris for å sende pakken blir {weight * 129:.2f}")
elif weight <= 10:
    print(f"Pris for å sende pakken blir {weight * 199:.2f}")
else:
    print(f"Pakken er for tung til å kunne sendes")
# 11. Centimeter til fot
# Hensikt: Konvertere med en oppgitt faktor.
# Oppgave: Les inn høyde i centimeter og konverter til fot. Bruk at 1 fot er 30,48 centimeter.
# Leveranse: Et program med tre testverdier.
# Hint: Bruk float() og divisjon.
# Kontrollpunkt: Gir 30,48 centimeter omtrent 1 fot?


height = float(input("Sriv inn høyde i centometer: "))
convert_to_foot = height / 30.48

print(f"{height} cm ttilsvarer {convert_to_foot:.2f} fot.")

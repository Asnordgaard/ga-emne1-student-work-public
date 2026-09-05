number = int(input("Skriv inn et heltall: "))

if number < 0:
    print("Tallet er negativt")
elif number > 0:
    print("Tallet er positivt")
else:
    print("Tallet er 0")

if number != 0 and number % 2 == 0:
    print("Tallet er et partall")
elif number != 0:
    print("Tallet er oddetall")
else:
    print("Siden tallet er 0, er det hverken partall eller oddetall :)")

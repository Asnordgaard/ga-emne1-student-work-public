choice = 0

while choice != 5:
    print("Velg en operasjon fra menyen nedenfor:")
    print("1. Addisjon (+)")
    print("2. Subtraksjon (-)")
    print("3. Divisjon (/)")
    print("4. Multiplikasjon (*)")
    print("5. Avslutt")

    choice = int(input("Velg operasjon: "))

    if choice == 5:
        print("Programmet avsluttes.")
    elif choice >= 1 and choice <= 4:
        first_number = float(input("Skriv inn første tall: "))
        second_number = float(input("Skriv inn tall nummer to: "))

        if choice == 1:
            answer = first_number + second_number
            print(f"{first_number} + {second_number} = {answer:.2f}")
        elif choice == 2:
            answer = first_number - second_number
            print(f"{first_number} - {second_number} = {answer:.2f}")
        elif choice == 3:
            answer = first_number / second_number
            print(f"{first_number} / {second_number} = {answer:.2f}")
        elif choice == 4:
            answer = first_number * second_number
            print(f"{first_number} * {second_number} = {answer:.2f}")
    else:
        print("Ugyldig valg")
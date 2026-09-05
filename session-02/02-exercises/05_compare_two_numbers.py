first_number = int(input("Skriv inn et tall: "))
second_number = int(input("Skriv et nytt tall: "))

if first_number < second_number:
    print("Det første tallet er mindre enn det andre tallet")
elif first_number > second_number:
    print("Det første tallet er større enn det andre tallet")
else:
    print("Det første tallet er likt det andre tallet")
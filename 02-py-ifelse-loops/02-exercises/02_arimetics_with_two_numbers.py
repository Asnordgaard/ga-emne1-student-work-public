first_number = 4
second_number = 20

sum = first_number + second_number
difference = second_number - first_number
product = first_number * second_number
division_one = first_number / second_number
division_two = second_number / first_number
whole_division_one = first_number // second_number
whole_division_two = second_number // first_number
rest_one = first_number % second_number
rest_two = second_number % first_number


print(f"Første tall: {first_number}")
print(f"Andre tall: {second_number}")
print(f"sum: {sum}")
print(f"Differanse: {difference}")
print(f"Produkt: {product}")
print(f"Divisjon av {first_number} / {second_number}: {division_one}")
print(f"Divisjon av {second_number} / {first_number}: {division_two}")
print(f"Heltallsdivisjon av {first_number} / {second_number}: {whole_division_one}")
print(f"Heltallsdivisjon av {second_number} / {first_number}: {whole_division_two}")
print(f"Rest etter divisjon av {first_number} / {second_number}: {rest_one}")
print(f"Rest etter divisjon av {second_number} / {first_number}: {rest_two}")

if difference % first_number == 0:
    print("Differansen mellom tall 1 og tall 2 er et partall")
else:
    print("Differansen mellom tall 1 og tall 2 er et oddetall")
counter = 0

for number in range(1, 101):
    if number % 3 == 0 and number > 20 and number < 80:
        print(number)
        counter += 1
print(f"Antall tall delelig med 3 er: {counter}")

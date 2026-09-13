print("Summerer sammen alle tall kumulativt i en løkke fra 1 - 10:")
total = 0
for numbers in range(1, 11):
    print(numbers)
    total += numbers
    print(f"Summen så langt er: {total}")


number = int(input("Skriv inn et heltall: "))
is_prime_number = True

if number <= 1:
    is_prime_number = False
else:
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime_number = False

if is_prime_number:
    print(f"{number} er et primtall")
else:
    print(f"{number} er ikke et primtall")
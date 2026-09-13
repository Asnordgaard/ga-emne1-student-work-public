number = int(input("Skriv inn et heltall: "))

power_of_two = number ** 2
power_of_three = number ** 3
rest_power_of_two = power_of_two % 2
rest_power_of_three = power_of_three % 2

print(f"{number} opphøyd i andre er lik: {power_of_two}. Rest når tallet deles på to er: {rest_power_of_two}")
print(f"{number} opphøyd i tredje er lik: {power_of_three}. Rest når tallet deles på 2 er: {rest_power_of_three}")
if number % 2 == 0:
    print(f"{number} er et partall")
else:
    print(f"{number} er et oddetall")
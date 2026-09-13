number = int(input("Skriv inn et heltall: "))

for steps in range(1, 11):
    sum = number * steps
    print(f"{number} x {steps} = {sum}: ")
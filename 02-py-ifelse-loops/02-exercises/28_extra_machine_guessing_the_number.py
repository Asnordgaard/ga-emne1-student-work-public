start_number = 1
end_number = 30
attempts = 0

while start_number <= end_number:
    guess = (start_number + end_number) // 2
    attempts += 1

    print(f"Jeg gjetter tallet {guess}")
    answer = input("Er tallet riktig, for høyt, eller for lavt? ")

    if answer == "for høyt":
        end_number = guess - 1
    elif answer == "for lavt":
        start_number = guess + 1
    elif answer == "riktig":
        print(f"Hurray. I made it in {attempts} attempts!")
        break
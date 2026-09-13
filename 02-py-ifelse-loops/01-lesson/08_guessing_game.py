# secret_number = 30
# attempts_left = 5
# first_attempt = int(input("Skriv et tall mellom 1 og 100: "))
# while attempts_left > 0:
#     attempt = int(input("Forsøk igjen: "))
#     if attempt == secret_number:
#         print("Du gjettet riktig")
#     elif attempt > 30:
#         print("Du gjettet for høyt tall")
#     else:
#         print("Du gjettet for lavt tall")
#     attempts_left -= 1
# print("Game over!")

secret_number = 30
attempts_left = 5
guessed_correctly = False

# While loop
while attempts_left > 0 and guessed_correctly != True:
    guess = int(input("Guess the number: (1 - 50) "))

    if guess == secret_number:
        print("Correct")
        guessed_correctly = True
    elif guess < secret_number:
        print("The number is to low")
    else:
        print("The number is too high")

    attempts_left -= 1

if not guessed_correctly:
    print(f"The number was {secret_number}")
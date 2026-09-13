secret_pin = 0
attempts_left = 3
is_authenticated = False

while secret_pin != 2468 and attempts_left > 0 and is_authenticated == False:
    secret_pin = int(input("Skriv in PIN kode: "))
    attempts_left -= 1
    if attempts_left == 0:
        print("Access denied!")
    elif secret_pin == 2468:
        is_authenticated = True
        print("Access granted")

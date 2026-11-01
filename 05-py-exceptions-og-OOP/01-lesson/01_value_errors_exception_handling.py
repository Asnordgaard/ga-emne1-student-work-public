input_ok = False
age = 0

while not input_ok:
    try:
        age = int(input("Age: "))
    except ValueError: # ValueError er hentet fra terminalens feiltype. Man kan ha så mange except linjer man vil.
        print("Du må skrive heltall")
    else:
        input_ok = True
print(f"Next year: {age + 1}")




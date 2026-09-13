amount = float(input("Kjøpsbeløp: "))
if amount >= 1000:
    discount = 0.20
elif amount >= 500:
    discount = 0.10
else:
    discount = 0

paying_price = amount * (1 - discount)

print(f"Du skal betale {paying_price:.2f}")

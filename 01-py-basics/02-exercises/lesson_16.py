# 16. Pris med rabatt
# Hensikt: Bruke prosentregning med tydelig output.
# Oppgave: Les inn varepris og rabattprosent, beregn rabattbeløpet og den rabatterte prisen.
# Leveranse: Tre kontrollerte testtilfeller.
# Hint: Finn rabattbeløpet først.
# Kontrollpunkt: Blir sluttprisen lavere når rabatten er over null?


price = float(input("Varepris: "))
discount_in_percentage = int(input("Rabbatt i hele prosenter: "))
discount_as_amount = price * discount_in_percentage / 100
final_amount = price - discount_as_amount

print(f"Pris med {discount_in_percentage}% rabatt (kr. {discount_as_amount:.2f}) blir kr. {final_amount:.2f}.")
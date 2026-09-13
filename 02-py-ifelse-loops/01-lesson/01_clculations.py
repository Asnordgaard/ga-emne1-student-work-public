number_of_tickets = int(input("How many tickets? "))
ticket_price = 180
service_fee = 35

subtotal = number_of_tickets * ticket_price
total = subtotal + service_fee
price_per_person = total / number_of_tickets

print(total)
print(round(price_per_person)) #round runder av
print(round(price_per_person, 2)) # tallet andgir antall desimaler


sum = sum + 1
sum += 1 # Dette betyr det samme som linje 14


total_cost = 180
number_of_persons = int(input("Antall personer: "))

cost_per_person = number_of_persons / total_cost

print(f"Kostnad per person er {cost_per_person:.2f}")

from os.path import exists

guests = ["Kermit", "Miss Piggy", "Gonzo"]
print(guests)

print("\n---\n")

mixed_list = ["Tomas", 52, True]
print(mixed_list)

print(guests[0])
print(guests[1])
print(guests[-1]) # siste element i lista
print(guests[-2]) # nest siste element i lista. -3, -4 osv. teller bakfra

print("\n---\n")

guests.append("Animal") # Kommer på slutten
guests.insert(2, "Camilla") # Settes inn der man angir index og forskyver resten bakover
print(guests)

print("\n---\n")

guests.remove("Miss Piggy")
print(guests)

print(len(guests))

for guest in guests:
    print(f"Welcome {guest}")

print("\n---\n")

scores = [72, 88, 91, 65]
print(len(scores))
print(sum(scores))

average = sum(scores) / len(scores)
print(f"Average: {average}")

print(min(scores))
print(max(scores))
# Testing user input

name = input("What is your name? ")

print(f"Hei, {name}!") # f == format string
print("Hei " + name)
print("Hello,", name,"!")

age = int(input("How old are you? ")) # int == caster (omgjør) fra string til int
next_year = age + 1

print(f"Next year you'll be {next_year}")
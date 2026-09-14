characters = {
    "name": "Robin",
    "special_skill": "Flying",
    "good_guy": True
}

print(characters["special_skill"])
print(characters["good_guy"])

characters["universe"] = "DC Comics"
# characters.update({"universe": "DC"})

characters["special_skill"] = "Running"


print(characters)
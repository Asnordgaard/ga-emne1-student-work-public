# Lists: made with []
# guests = ["Kermit", "Miss Piggy", "Gonzo"]

# Tuplet
coordinates = (59.91, 10.75)
print(coordinates[0])
print(coordinates[1])

mixed_tuple = ("Tomas", 52, True)

print("\n---\n")

# Dictionary {"Key": "Value"}
muppet = {"name": "Kermit", "species": "Frog", "job": "Host"  }

# Bør skrives slik:

muppet = {
    "name": "Kermit",
    "species": "Frog",
    "job": "Host"
}

print(muppet["name"])
print(muppet["job"])

# Kombinere

persons = [{
    "name": "Anne"
},
{
    "name": "Per"
    }]

print(persons)

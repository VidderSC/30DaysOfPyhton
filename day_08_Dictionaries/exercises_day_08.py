print("# Exercises: Day 8")
print()
print("01. Create an empty dictionary called cat")
cat = {}
print(cat)

print()
print("02. Add name, color, breed, legs, age to the cat dictionary")
cat["name"] = "Luna"
cat["color"] = "Tricolor"
cat["breed"] = "Callejero"
cat["legs"] = 4
cat["age"] = 15
print(cat)

print()
print("""03. Create a sibling dictionary and add 
      first_name, last_name, gender, age, marital status, 
      skills, country, city and address as keys for the dictionary""")
sibling = {
    "first_name": "wlll",
    "last_name": "lam",
    "gender": "Male",
    "age": 65,
    "is_married": False,
    "skills": ["Some", "Skilled", "Things"],
    "country": "Spain",
    "city": "Malaga",
    "address": "Some street name"
}
print(sibling)

print()
print("04. Get the length of the sibling dictionary")
print(len(sibling))

print()
print("05. Get the value of skills and check the data type, it should be a list")
print(sibling.get("skills"))
print(type(sibling["skills"]))

print()
print("06. Modify the skills values by adding one or two skills")
sibling["skills"].append("skill one")
sibling["skills"].append("skill two")
print(sibling["skills"])

print()
print("07. Get the dictionary keys as a list")
keys = sibling.keys()
print(keys)

print()
print("08. Get the dictionary values as a list")
values = sibling.values()

print()
print("09. Change the dictionary to a list of tuples using items() method")
print(sibling.items())

print()
print("10. Delete one of the items in the dictionary")
print(cat)
del cat["color"]
print(cat)

print()
print("11. Delete one of the dictionaries")
print("del cat")
del cat

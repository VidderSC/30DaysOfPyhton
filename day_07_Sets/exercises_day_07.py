# Sets:
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(f"it_companies = {it_companies}")
print(f"A = {A}")
print(f"B = {B}")
print(f"age = {age}")

print()
print()
print("Exercises: Level 1")
print()

print("01. Find the length of the set it_companies")
print(f"length = {len(it_companies)}")

print()
print("02. Add 'Twitter' to it_companies")
it_companies.add("Twitter")
print(it_companies)

print()
print("03. Insert multiple IT companies at once to the set it_companies")
it_companies.update({"IT company 1", "IT company 2"})
print(it_companies)

print()
print("04. Remove one of the companies from the set it_companies")
if "IT company 2" in it_companies:
    it_companies.remove("IT company 2")
print(it_companies)

print()
print("05. What is the difference between remove and discard")
it_companies.discard("IT company 2")
print(it_companies)
print("""
it_companies.remove("IT company 2")  # KeyError: 'IT company 2'
    Remove will raise an error if the item does not exist in the Set
      
it_companies.discard("IT company 2")  # Nothing happens.
    Discard will not raise an error if the item is not in the set.""")

print()
print()
print("Exercises: Level 2")

print()
print("01. Join A and B")
print(f"A = {A}")
print(f"B = {B}")
A_B = A.union(B)
print(f"A.union(B) = {A_B}")

print()
print("02. Find A intersection B")
print(A.intersection(B))

print()
print("03. Is A subset of B")
print(A.issubset(B))

print()
print("04. Are A and B disjoint sets")
print(A.isdisjoint(B))

print()
print("05. Join A with B and B with A")
print(A.union(B))
print(B.union(A))

print()
print("06. What is the symmetric difference between A and B")
print(A.symmetric_difference(B))

print()
print("07. Delete the sets completely")
print("""del A
del B
del A_B
del it_companies""")
del A
del B
del A_B
del it_companies

print()
print()
print("Exercises: Level 3")
print()
print("01. Convert the ages to a set and compare the length of")
print("the list and the set, which one is bigger?")
print(f"age = {age}")
print(len(age))
age_set = set(age)
print(f"age_set = {age_set}")
print(len(age_set))
print("The list is bigger than the set, because there are no duplicates in the set.")


print()
print("02. Explain the difference between the following data types:")
print("""- string: It's an ordered collection of chars that it's mutable.
- list: It's an ordered collection of objects that it's mutable.
- tuple: It's an ordered collection of objects that it's inmutable and no new items can be added to it.
- set: It's an unordered collection of objects that it's inmutable but, new items can be added to it.""")

print()
print("03. I am a teacher and I love to inspire and teach people.")
print("How many unique words have been used in the sentence?")
print("Use the split methods and set to get the unique words.")
sentence = "I am a teacher and I love to inspire and teach people."
print(f"{len(set(sentence.split()))} unique words")

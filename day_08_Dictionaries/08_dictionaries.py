# Day 8 - 30DaysOfPython Challenge

# Dictionaries
"""
A dictionary is a collection of unordered, modifiable(mutable) 
paired (key: value) data types, that cannot contain duplicate keys.
"""
empty_dict = {}
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

person = {
    'first_name': 'Vidders',
    'last_name': "SC",
    "age": 69,
    'country': 'Spain',
    "is_married": True,
    "skills": ["Java", "Python"],
    'address': {
        "street": "Beverly Hills",
        "zipcode": '90210'
    }
}

# Dictionary Length
# It checks the number of "key:value" pairs in the dictionary.

print(len(person))

# Accessing Dictionary Items
# We can access Dictionary items by referring to its key name.

print(person["first_name"])
print(person["country"])
print(person["age"])
print(person["skills"])
print(person["skills"][0])
print(person["address"]["zipcode"])
print()
# Accessing an item by key name raises an error if the key does not exist.
# To avoid this error first we have to check if a key exist or
# we can use the get method. The get method returns None, which is a NoneType
# object data type, if the key does not exist.
# print(person["city"])  # KeyError: 'city', because that key doesn't exist

# with "in" we can check if a key exists in a dictionary, it returns a Boolean
if "city" in person:
    print(person["city"])
else:
    print("None from the IF")

print(person.get("city"))
print()

# Adding items to a dictionary
person["city"] = "Malaga"
person["skills"].append('HTML')
print(person.get("city"))
print(person)
print()

# We can modify items in a dictionary by reasigning the value
person["age"] = 250
print(person.get("age"))
print()

# Removing Key and Value Pairs from a Dictionary
"""
pop(key): removes the item with the specified key name:
popitem(): removes the last item
del: removes an item with specified key name
"""
print(dct)
dct.pop('key1')  # removes key1 item
print(dct)
dct.popitem()  # removes the last item
print(dct)
del dct['key2']  # removes key2 item
print(dct)
print()

# Changing Dictionary to a List of Items
# The items() method changes dictionary to a list of tuples.
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct.items())
print()

# Copying, clearing and deleting a Dictionary
dct_copy = dct.copy()
print(dct)
dct.clear()
print(dct)
del dct
print()

# Getting Dictionary Keys and Values as a List
# The .keys() method gives us all the keys of a a dictionary as a list
# The .values() method gives us all the values of a a dictionary as a list.
dictionary = {'key1': 'value1', 'key2': 'value2',
              'key3': 'value3', 'key4': 'value4'}
dictionary_keys = dictionary.keys()
dictionary_values = dictionary.values()
print(dictionary_keys)
print(dictionary_values)

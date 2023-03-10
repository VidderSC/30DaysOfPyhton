# 01. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print('Thirty', 'Days', 'Of', 'Python')

# 02. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('Coding', 'For', 'All')

# 03. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 04. Print the variable company using print().
print(company)

# 05. Print the length of the company string using len() method and print().
print(len(company))

# 06. Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 07. Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 08. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 09. Cut(slice) out the first word of Coding For All string.
print(company[1:])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print(company.find('Coding'))
print(company.rindex('Coding'))
print(company.startswith('Coding'))

# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
company = "Python for Everyone"
print(company.replace('Everyone', 'All'))
print(company.strip('Everyone'), "All")

# 13. Split the string 'Coding For All' using space as the separator (split()) .
company = "Coding For All"
print(company.split())

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
sentence = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(sentence.split(","))

# 15. What is the character at index 0 in the string Coding For All.
print(company[0])

# 16. What is the last index of the string Coding For All.
print(len(company) - 1)

# 17. What character is at index 10 in "Coding For All" string.
print(f'"{company[10]}"')  # Is a space

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
sentence = "Python For Everyone"
acronym = sentence[0]
length = len(sentence)-1
for i in range(length):
    if sentence[i] == " ":
        acronym += sentence[i+1]
print(acronym)

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
sentence = "Coding For All"
acronym = sentence[0]
length = len(sentence)-1
for i in range(length):
    if sentence[i] == " ":
        acronym += sentence[i+1]
print(acronym)

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print(sentence.index('C'))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print(sentence.index('F'))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
sentence = "Coding for All People"
print(sentence.rfind('l'))
print()
# 23. Use index or find to find the position of the first occurrence of the word 'because' in
# the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence)
print(sentence.find('because'))

# 24. Use rindex to find the position of the last occurrence of the word because
print(sentence.rindex('because'))

# 25. Slice out the phrase 'because because because'
print()
start = sentence.index('because')
end = start + len('because because because')
print(sentence[:start], sentence[end:])
print()

# 26. Find the position of the first occurrence of the word 'because'
print("This is duplicated. It's the same exercise as 23.")

# 27. Slice out the phrase 'because because because'
print("This is duplicated. It's the same exercise as 25.")

# 28. Does ''Coding For All' start with a substring Coding?
sentence = "Coding for All"
print(sentence.startswith("Coding"))

# 29. Does 'Coding For All' end with a substring coding?
print(sentence.startswith("coding"))
print()
# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
sentence = '   Coding For All      '
print(sentence)
print(sentence.strip())
print()

# 31. Which one of the following variables return True when we use the method isidentifier():
#       30DaysOfPython
#       thirty_days_of_python
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# 32. The following list contains the names of some of python libraries:
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'].
# Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(libraries)
print("# ".join(libraries))
print()
# 33. Use the new line escape sequence to separate the following sentences.
#       I am enjoying this challenge.
#       I just wonder what is next.
print("I am enjoying this challenge.\rI just wonder what is next.")

# 34. Use a tab escape sequence to write the following lines.
#       Name      Age     Country   City
#       Asabeneh  250     Finland   Helsinki
print("Name\tAge\t\tCountry\t\tCity")
print("Vidders\t69\t\tSpain\t\tMalaga")
print()

# 35. Use the string formatting method to display the following:
#       radius = 10
#       area = 3.14 * radius ** 2
#       The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print(
    f'The area of a circle with radius {radius} is {int(area)} meters square.')
print()

# 36. Make the following using string formatting methods:
#       8 + 6 = 14
#       8 - 6 = 2
#       8 * 6 = 48
#       8 / 6 = 1.33
#       8 % 6 = 2
#       8 // 6 = 1
#       8 ** 6 = 262144

num1 = 8
num2 = 6

print("%d + %d = %d" % (num1, num2, num1 + num2))
print("{} - {} = {}".format(num1, num2, num1 - num2))
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2:.2f}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")

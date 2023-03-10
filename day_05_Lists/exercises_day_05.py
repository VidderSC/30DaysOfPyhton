from countries import countries

# Exercises: Level 1
country = ["Spain", "Finland", "Denmark", "Sweden", "Norway", "Finland"]

# 04. Get the first item, the middle item and the last item of the list
length = len(country)-1
print(length)
print(country[0], country[length // 2], country[-1])
print()

# Exercises: Level 2
# 01. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(f'Ages: {ages}')
# - Sort the list and find the min and max age
ages.sort()
min = ages[0]
max = ages[-1]
print(f'min: {min}, max: {max}')
# - Add the min age and the max age again to the list
ages.append(min)
ages.append(max)

# - Find the median age (one middle item or two middle items divided by two)
len_ages = len(ages)
print(f"len_ages = {len_ages}")
ages.sort()

if len_ages % 2 == 0:  # if even length, we add the 2 middle items and divide by 2
    age1 = ages[len_ages // 2]
    age2 = ages[len_ages // 2 + 1]
    median = (age1 + age2) / 2
else:  # if odd length, we take the middle item.
    median = ages[len_ages // 2]

print(f"Median: {abs(median)}")

# - Find the average age (sum of all items divided by their number )
count = 0
for age in ages:
    count += age
average = count // len_ages
print(f'Average: {average}')

# - Find the range of the ages (max minus min)
range = max - min
print(f'Range: {range}')

# - Compare the value of (min - average) and (max - average), use abs() method
print(abs(min - average) == abs(max - average))
print()

# 02. Find the middle country(ies) in the countries list
print(countries)
print()
if len(countries) % 2 == 0:
    print(countries[len(countries)//2])
else:
    print(countries[len(countries)//2], countries[len(countries)//2+1])

# 03. Divide the countries list into two equal lists if it is even
# if not, one more country for the first half.
list_one = None
list_two = None

if len(countries) % 2 == 0:
    list_one = countries[:len(countries)//2]
    list_two = countries[len(countries)//2:]
else:
    list_one = countries[:len(countries)//2 + 1]
    list_two = countries[len(countries)//2 + 1:]

print(list_one)
print(len(list_one))
print(list_two)
print(len(list_two))
print()

# 04. ['China', 'Ukraine', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'].
#     Unpack the first three countries and the rest as scandic countries.
ch, ua, us, *scandic = ['China', 'Ukraine', 'USA',
                        'Finland', 'Sweden', 'Norway', 'Denmark']
print(ch)
print(ua)
print(us)
print(scandic)

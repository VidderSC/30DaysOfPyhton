from random import random, randint, sample
from string import ascii_letters as asc, digits as nums

print("### Exercises: Day 12")
print()

print("## Exercises: Level 1")
print()
print("""01. Write a function which generates a six digit/character random_user_id.

    print(random_user_id())  # '1ee33d'
    """)


# def random_user_id():
def random_user_id(x):
    user_id = ""
    chars = asc + nums
    length = len(chars) - 1
    # for i in range(6):
    for i in range(x):
        user_id += chars[randint(0, length)]
    return user_id


# print(random_user_id())
print(random_user_id(6))

print()
print("""02. Modify the previous task. Declare a function named user_id_gen_by_user. 
It doesn't take any parameters but it takes two inputs using input(). 
One of the inputs is the number of characters and the second input is 
the number of IDs which are supposed to be generated.

    print(user_id_gen_by_user()) # user input: 5 3
    #output:
    #kcsy2
    #SMFYb
    #bWmeq

    print(user_id_gen_by_user()) # 16 2
    #1GCSgPLMaBAVQZ26
    #YD7eFwNQKNs7qXaT
""")


def enter_number():
    while True:
        num_char = input()
        if num_char.isdigit():
            num_char = int(num_char)
            if num_char > 0:
                return num_char
            else:
                print("Number must be higher than 0.")
                continue
        else:
            print("You must enter a number")


def user_id_gen_by_user():
    print("Please enter the length of your id: ")
    length = enter_number()
    print("Please enter the quantity: ")
    quantity = enter_number()
    for i in range(quantity):
        print(random_user_id(length))


user_id_gen_by_user()

print()
print("""03. Write a function named rgb_color_gen. 
It will generate rgb colors (3 values ranging from 0 to 255 each).

    print(rgb_color_gen())
    rgb(125,244,255)  # The output should be in this form
""")


def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = "rgb("+str(r)+","+str(g)+","+str(b)+")"
    return rgb


print(rgb_color_gen())

print()
print()
print("## Exercises: Level 2")

print()
print("""01. Write a function list_of_hexa_colors which returns any 
number of hexadecimal colors in an array (six hexadecimal numbers 
written after #. Hexadecimal numeral system is made out of 16 symbols, 
0-9 and first 6 letters of the alphabet, a-f.""")
hexa = nums + asc[0:6]
length_hexa = len(hexa)-1


def list_of_hexa_colors(number):
    hexa_list = []
    for i in range(number):
        hexa_value = "#"
        for j in range(6):
            hexa_value += hexa[randint(0, length_hexa)]
        hexa_list.append(hexa_value)
    return hexa_list


print()
print("""02. Write a function list_of_rgb_colors which returns 
any number of RGB colors in an array.""")


def list_of_rgb_colors(number):
    rgb_list = []
    for i in range(number):
        rgb_list.append(rgb_color_gen())
    return rgb_list


print()
print("""03. Write a function generate_colors which can 
generate any number of hexa or rgb colors.
""")


def generate_colors(function, number):
    if function == "hexa":
        print(list_of_hexa_colors(number))
    elif function == "rgb":
        print(list_of_rgb_colors(number))


generate_colors('hexa', 3)
generate_colors('hexa', 1)
generate_colors('rgb', 3)
generate_colors('rgb', 1)

print()
print()
print("## Exercises: Level 3")

print()
print("""01. Call your function shuffle_list, 
it takes a list as a parameter and it returns a shuffled list
""")


def shuffle_list(lista):
    return sample(lista, len(lista))


mylist = ["apple", "banana", "cherry", "strawberry", "pear"]
print(mylist)
print(shuffle_list(mylist))

print()
print("""02. Write a function which returns an array of seven 
random numbers in a range of 0-9. All the numbers must be unique.
""")


def random_list_of_seven_unique():
    return sample(nums, 7)


print(random_list_of_seven_unique())

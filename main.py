import random

def vowels():
    vowels = ["a", "e", "i", "o", "u"]
    x = 0
    i = 0

    word_input = input("write a word: ").lower()

    while i < len(word_input):
        for y in range(len(vowels)):
            if word_input[i] == vowels[y]:
                x += 1
        i +=1
    print(word_input + "contains" + x + "vowels")

def prefectures():
    prefectures = ["hokkaido", "aomori", "akita", "iwate", "yamagata", "miyagi", "fukushima", "tochigi", "gunma", "ibaraki", "saitama", "chiba", "tokyo", "kanagawa", "nigata", "toyama", "ishikawa", "fukui", "gifu", "nagano", "yamanashi", "aichi", "shizouka", "shiga", "kyoto", "mie", "nara", "hyogo", "osaka", "wakayama", "tottori", "okayama", "shimane", "hiroshima", "yamaguchi", "kagawa", "tokushima", "ehime", "kochi", "fukuoka", "saga", "nagasaki", "oita", "kumamoto", "miyazaki", "kagoshima", "okinawa"]

    print()
    print("there are " + str(len(prefectures)) + " prefectures in Japan")
    print()
    for x in prefectures:
        print(x + " is " + str(len(x)) + " letters long")
        print()

def numbers():
    for x in range(9):
        y = ((x + 1) * 111111)
        print(y)

def math():
    n1 = int(input("write a number: "))
    n2 = int(input("write a number: "))
    if n1 == 9 and n2 == 10:
        print("they add up to " + str(21))
    else:
        print("they add up to " + str(n1 + n2))

def palendrom():
    word_input = input("write a word: ")
    word_input_reversed = ""

    for i in reversed(word_input):
        word_input_reversed += i

    if word_input == word_input_reversed:
        print("the word is a palendrome")
    else:
        print("the word is not a palendrome")

def random_generator():
    input_object = ""
    objects = []
    
    print()
    print("write a few fings to get a random one of them (write 'done' when you are done): ")
    while True:
        input_object = input(": ")
        if input_object != "done":
            objects.append(input_object)
        else:
            break
    print()    
    random_object = random.randint(0, len(objects) - 1)
    print("you got: " + objects[random_object])
    print()

def odd_even_numbers():
    numbers = [1, 7, 33, 6, 88, -7]

    odd_numbers = []
    even_numbers = []

    for x in numbers:
        if (x / 2).is_integer():
        # (x % 2 == 0) also works
            even_numbers.append(x)
        else:
            odd_numbers.append(x)

    print(odd_numbers)
    print(even_numbers)

def remove_letters():

    letters = ["a", "b", "h", "d", "o", "c", "e"]

    print(letters)
    word = input("write a word and the letters that are both in the word and in the list will be removed from the list: ").lower()
    print()

    for x in word:
        for y in letters:
            if x == y:
                letters.remove(x)

    print(letters)

x = 0
y = 0
def additon(x, y): 
    return(x + y)
def subtraction(x , y):
    return(x - y)
def multiplicaton(x, y):
    return(x * y)
def division(x, y):
    return(x / y)

def calculator():
    while True:
        
        print()
        print("welcome to the calculator")
        numbers_calculator_1 = int(input("Write a number: "))
        numbers_calculator_2 = int(input("Write an other number: "))

        question_calculator = input("what do you want to do (add, subtract, multiply, divide): ").lower()
        if question_calculator == "add":
            result = additon(numbers_calculator_1, numbers_calculator_2)
        elif question_calculator == "subtract":
            result = subtraction(numbers_calculator_1, numbers_calculator_2)
        elif question_calculator == "multiply":
            result = multiplicaton(numbers_calculator_1, numbers_calculator_2)
        elif question_calculator == "divide":
            result = division(numbers_calculator_1, numbers_calculator_2)
        else:
            print("unvalid input")

        print(result)

def magic_8ball():
    yes = ["yes", "yeess"]
    maybe = ["maybe", "idk"]
    no = ["no", "nooooo"]
    answer_types = [yes, maybe, no]

    answer_type = random.choice(answer_types)
    answer = random.choice(answer_type)

    print()
    print("the answer is: " + answer)
    print()

    

print()
question = input("pick a program (v, pr, n, m, pa, r, oen, rl, c, mb): ").lower()

if question == "v":
    vowels()
elif question == "pr":
    prefectures()
elif question == "n":
    numbers()
elif question == "m":
    math()
elif question == "pa":
    palendrom()
elif question == "r":
    random_generator()
elif question == "oen":
    odd_even_numbers()
elif question == "rl":
    remove_letters()
elif question == "c":
    calculator()
elif question == "mb":
    magic_8ball()
else:
    print("unvalid input")
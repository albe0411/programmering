import random
from datetime import date
import datetime

import matplotlib.pyplot as plt
import numpy as np

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
    print(str(word_input) + " contains " + str(x) + " vowels")

def prefectures():
    prefectures = ["hokkaido", "aomori", "akita", "iwate", "yamagata", "miyagi", "fukushima", "tochigi", "gunma", "ibaraki", "saitama", "chiba", "tokyo", "kanagawa", "nigata", "toyama", "ishikawa", "fukui", "gifu", "nagano", "yamanashi", "aichi", "shizouka", "shiga", "kyoto", "mie", "nara", "hyogo", "osaka", "wakayama", "tottori", "okayama", "shimane", "hiroshima", "yamaguchi", "kagawa", "tokushima", "ehime", "kochi", "fukuoka", "saga", "nagasaki", "oita", "kumamoto", "miyazaki", "kagoshima", "okinawa"]

    print()
    print("there are " + str(len(prefectures)) + " prefectures in Japan")
    print()
    for x in prefectures:
        print(str(x) + " is " + str(len(x)) + " letters long")
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
    print("the answer is: " + str(answer))
    print()

def rock_paper_scissors():

    computer_score = 0
    user_score = 0
    
    while user_score <= 2 and computer_score <= 2:
        user_choise = input("pick rock, paper or scissors (write break to end): ").lower()
        print()
        random_pick = random.choice(["rock", "paper", "scissors"])

        if user_choise == "break":
            break
        elif user_choise != "rock" and user_choise != "paper" and user_choise != "scissors":
            print("invalid")
        elif random_pick == user_choise:
            print("tie")
            print("user score: " + str(user_score))
            print("computer score: " + str(computer_score))
            print()
        elif random_pick == "rock" and user_choise == "paper":
            print("user won")
            user_score += 1
            print("user score: " + str(user_score))
            print("computer score: " + str(computer_score))
            print()
        elif random_pick == "paper" and user_choise == "scissors":
            print("user won")
            user_score += 1
            print("user score: " + str(user_score))
            print("computer score: " + str(computer_score))
            print()
        elif random_pick == "scissors" and user_choise == "rock":
            print("user won")
            user_score += 1
            print("user score: " + str(user_score))
            print("computer score: " + str(computer_score))
            print()
        else:
            print("computer won")
            computer_score += 1
            print("user score: " + str(user_score))
            print("computer score: " + str(computer_score))
            print()
        
    if user_score == 3:
        print("user won big")
    elif computer_score == 3:
        print("computer won big")

def compare_sum_of_numbers():
    sum1 = 0
    sum2 = 0

    print()
    number1 = input("write a number: ")
    number2 = input("write an other number: ")

    for i in str(number1): #changes the number to a string to be able to loop through it like a list
        sum1 += int(i) #adds all the numbers together
    for i in str(number2):
        sum2 += int(i)

    print()

    if sum1 == sum2: #compares the numbers
        print(str(sum1) + " = " + str(sum2))
    else:
        print(str(sum1) + " ≠ " + str(sum2))
    print()

def number_guess():
    random_number = random.randint(1, 100)
    guess_counter = 0
    print()

    while True:
        while True:
            user_guess = input("guess a number: ")
            try:
                user_guess = int(user_guess)
                break
            except:
                print("invalid input")

        if user_guess < random_number:
            print("the number is bigger")
            print()
            guess_counter += 1
        elif user_guess > random_number:
            print("the number is smaller")
            print()
            guess_counter += 1
        elif user_guess == random_number:
            print("you guessed right!")
            print("number of gusses: " + str(guess_counter))
            print()
            break

def cost_calculation(start_year, start_month, start_day, end_year, end_month, end_day, meter_setings_end, meter_setings_start, cost, standing_cost):

    start_date = datetime.datetime(start_year, start_month, start_day)
    end_date = datetime.datetime(end_year, end_month, end_day)

    date_dif = end_date - start_date

    day_dif = date_dif.days

    meter_setings_dif = meter_setings_end - meter_setings_start

    calculation = ((day_dif * standing_cost) + (meter_setings_dif * cost) * 1.25) / 100

    return calculation

def electricity_bill():
    while True:
        try:
            start_year = int(input("start year: "))
            start_month = int(input("start month: "))
            start_day = int(input("start day: "))
            print()

            end_year = int(input("end year: "))
            end_month = int(input("end month: "))
            end_day = int(input("end day: "))
            print()

            meter_setings_start = int(input("start meter setings: "))
            meter_setings_end = int(input("end meter setings: "))
            print()

            cost = int(input("electricity cost: "))
            standing_cost = int(input("standing cost: "))
            print()

            break
        except ValueError:
            print("invalid number")
        except KeyboardInterrupt:
            break

    print()
    print(str(cost_calculation(start_year, start_month, start_day, end_year, end_month, end_day, meter_setings_end, meter_setings_start, cost, standing_cost)) + " sek")
    print()

def mc_sales():
    total_sales = 0
    day_num = 0

    hamburgare_price = 50
    pommes_frites_price = 25
    läsk_price = 20
    milkshake_price = 30
    sallader_price = 45
    mcnuggets_price = 35

    ypoints_add = []

    sales_data = [
    {"Hamburgare": 150, "Pommes frites": 200, "Läsk": 180, "Milkshake": 40, "Sallader": 30, "McNuggets": 100},
    {"Hamburgare": 170, "Pommes frites": 220, "Läsk": 190, "Milkshake": 50, "Sallader": 35, "McNuggets": 105},
    {"Hamburgare": 160, "Pommes frites": 210, "Läsk": 185, "Milkshake": 45, "Sallader": 33, "McNuggets": 110},
    {"Hamburgare": 180, "Pommes frites": 230, "Läsk": 200, "Milkshake": 55, "Sallader": 40, "McNuggets": 115},
    {"Hamburgare": 170, "Pommes frites": 220, "Läsk": 195, "Milkshake": 50, "Sallader": 38, "McNuggets": 120},
    {"Hamburgare": 190, "Pommes frites": 240, "Läsk": 210, "Milkshake": 60, "Sallader": 42, "McNuggets": 125},
    {"Hamburgare": 185, "Pommes frites": 235, "Läsk": 205, "Milkshake": 58, "Sallader": 40, "McNuggets": 130},
    {"Hamburgare": 175, "Pommes frites": 225, "Läsk": 190, "Milkshake": 52, "Sallader": 36, "McNuggets": 120},
    {"Hamburgare": 165, "Pommes frites": 215, "Läsk": 185, "Milkshake": 48, "Sallader": 34, "McNuggets": 110},
    {"Hamburgare": 180, "Pommes frites": 230, "Läsk": 200, "Milkshake": 55, "Sallader": 39, "McNuggets": 115}
    ]

    print()
    for day in sales_data:
        day_sales = 0
        day_num += 1

        day_sales = day["Hamburgare"] * hamburgare_price
        day_sales += day["Pommes frites"] * pommes_frites_price
        day_sales += day["Läsk"] * läsk_price
        day_sales += day["Milkshake"] * milkshake_price
        day_sales += day["Sallader"] * sallader_price
        day_sales += day["McNuggets"] * mcnuggets_price

        print("day " + str(day_num) + ": " + str(day_sales) + " kr")
        ypoints_add.append(day_sales)

        total_sales += day_sales

    print()
    print("total: " + str(total_sales) + " kr")

    xpoints = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ypoints = np.array(ypoints_add)
    plt.plot(xpoints, ypoints, marker = 'o')
    plt.show()

def letter_count():
    letters = {}

    sentence = str(input("input sentence: ").lower())

    for i in range(len(sentence)):
        if sentence[i] in letters:
            letters[sentence[i]] += 1
        else:
            letters[sentence[i]] = 1

    for x in letters:
        print(str(x) + ": " + str(letters[x]))

print()
question = input("pick a program (v, pr, n, m, pa, r, oen, rl, c, mb, rps, cson, ng, eb, mc, lc): ").lower()

match question:
    case "v":
        vowels()
    case "pr":
        prefectures()
    case "n":
        numbers()
    case "m":
        math()
    case "pa":
        palendrom()
    case "r":
        random_generator()
    case "oen":
        odd_even_numbers()
    case "rl":
        remove_letters()
    case "c":
        calculator()
    case "mb":
        magic_8ball()
    case "rps":
        rock_paper_scissors()
    case "cson":
        compare_sum_of_numbers()
    case "ng":
        number_guess()
    case "eb":
        electricity_bill()
    case "mc":
        mc_sales()
    case "lc":
        letter_count()
    case _:
        print("invalid input")
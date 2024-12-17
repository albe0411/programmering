import random

special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '~', '`', '{', '}', '[', ']',
    '|', ';', ':', '\\', '"', '<', '>', ',', '.', '/', '?' ]
numbers = [
    '0','1','2','3','4','5','6','7','8','9'
]
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

list_choices = ["letters"]
password = ""

print("generate your password")
while True:
    try:
        while True:
            length_question = int(input("how long?: "))
            if length_question > 0:
                break
            else:
                print("invalid input")
        while True:
            capitals_question = input("include capital letters? (yes, no): ").lower()
            match capitals_question:
                case "yes":
                    list_choices.append("capital")
                    break
                case "no":
                    break
                case _:
                    print("invalid input")
        while True:
            numbers_question = input("include numbers? (yes, no): ").lower()
            match numbers_question:
                case "yes":
                    list_choices.append("numbers")
                    break
                case "no":
                    break
                case _:
                    print("invalid input")
        while True:
            special_characters_question = input("include special characters? (yes, no): ").lower()
            match special_characters_question:
                case "yes":
                    list_choices.append("special_characters")
                    break
                case "no":
                    break
                case _:
                    print("invalid input")

        for i in range(length_question):
            selected = random.choice(list_choices)
            match selected:
                case "letters":
                    password += letters[random.randrange(0, len(letters))]
                case "capital":
                    password += letters[random.randrange(0, len(letters))].upper()
                case "numbers":
                    password += numbers[random.randrange(0, len(numbers))]
                case "special_characters":
                    password += special_characters[random.randrange(0, len(special_characters))]
        print(password)
        break
    
    except ValueError:
        print("ValueError")
    except KeyboardInterrupt:
        print("KeyboardIterrupt")
        break
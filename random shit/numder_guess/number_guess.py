import random

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
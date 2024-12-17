import random

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

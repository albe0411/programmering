import random

deck = ['a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k',
        'a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k',
        'a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k',
        'a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']

player1_hand = []
player2_hand = []
player3_hand = []

player1_point = 0
player2_point = 0
player3_point = 0

player1_player_choice = ["2", "3"]
player2_player_choice = ["1", "3"]
player3_player_choice = ["1", "2"]

player_turn = random.randint(1, 3)

random.shuffle(deck)

for i in range(7):
    player1_hand.append(deck[0])
    deck.pop(0)
    player2_hand.append(deck[0])
    deck.pop(0)
    player3_hand.append(deck[0])
    deck.pop(0)

while True:
    print()
    print("player 1 score: ", player1_point)
    print("player 2 score: ", player2_point)
    print("player 3 score: ", player3_point)
    print()

    print("player's turn: ", player_turn)

    question_player = 0
    question_card = 0

    if eval(f"player{player_turn}_hand"):
        if player_turn == 1:
            while True:
                print(player1_hand)
                question_player = input(str(player1_player_choice) + ": ")
                question_card = input(str(player1_hand) + ": ").lower()

                if question_player in player1_player_choice and question_card in player1_hand:
                    break
                else:
                    print("invalid input")
        else:
            exec(f"question_player = random.choice(player{player_turn}_player_choice)")
            exec(f"question_card = random.choice(player{player_turn}_hand)")

    if question_player == 0 and question_card == 0:
        print("players hand is empty")
    else:
        print("player asked: ", question_player)
        print("card asked about: ", question_card)

    if question_player != 0 and question_card in eval(f"player{question_player}_hand"):
        amount_of_cards_taken = 0
        while eval(f"question_card in player{question_player}_hand"):
            exec(f"player{question_player}_hand.remove(question_card)")
            exec(f"player{player_turn}_hand.append(question_card)")
            amount_of_cards_taken += 1
        print("amount of cards taken: ", amount_of_cards_taken)
    elif len(deck) != 0:
        exec(f"player{player_turn}_hand.append(deck[0])")
        deck.pop(0)
        print("a card was taken from the deck")
    else:
        print("the deck is empty")

    cards_in_hand = {}

    for i in eval(f"range(len(player{player_turn}_hand))"):
        if eval(f"player{player_turn}_hand[i] in cards_in_hand"):
            exec(f"cards_in_hand[player{player_turn}_hand[i]] += 1")
        else:
            exec(f"cards_in_hand[player{player_turn}_hand[i]] = 1")

    for i in cards_in_hand:
        if cards_in_hand[i] == 4:
            for x in range(4):
                exec(f"player{player_turn}_hand.remove(str(i))")
            exec(f"player{player_turn}_point += 1")

    if not deck and not player1_hand and not player2_hand and not player3_hand:
        print()
        print("player 1 score: ", player1_point)
        print("player 2 score: ", player2_point)
        print("player 3 score: ", player3_point)
        print()
        break

    player_turn += 1
    if player_turn == 4:
        player_turn = 1
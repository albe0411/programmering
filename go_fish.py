import random

#add func
deck = ['a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k',
        'a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k',
        'a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k',
        'a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']

player1 = []
player2 = []
player3 = []

player1_point = 0
player2_point = 0
player3_point = 0

#add func
random.shuffle(deck)

for i in range(7):
    player1.append(deck[0])
    deck.pop(0)
    player2.append(deck[0])
    deck.pop(0)
    player3.append(deck[0])
    deck.pop(0)

print(player1)
print(player2)
print(player3)

print(deck)

#add func
while True:
    #add loop player turn (random order)
    #add if for player or computer
    #if computer > randomize

    question_player = input("2, 3: ")
    question_card = input("a, 2, 3, 4, 5, 6, 7, 8, 9, 10, j, q, k: ") #add try/catch


    if eval(f"question_card in player{question_player}"):
        while eval(f"question_card in player{question_player}"):
            exec(f"player{question_player}.remove(question_card)")
            player1.append(question_card) #add exac
    else:
        player1.append(deck[0]) #add exac

    print(player3)
    print(player2)
    print(player1)
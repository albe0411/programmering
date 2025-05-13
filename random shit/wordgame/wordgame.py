def game():
    word_list = []
    word_list.append(input(":"))

    while True:
        print(word_list[-1][-1])
        new_word = input(": ").lower()
        if new_word[0] != word_list[-1][-1]:
            break
        elif new_word in word_list:
            break
        else:
            word_list.append(new_word)

game()
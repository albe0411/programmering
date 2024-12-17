word_input = input("write a word: ")
word_input_reversed = ""

for i in reversed(word_input):
    word_input_reversed += i

if word_input == word_input_reversed:
    print("the word is a palendrome")
else:
    print("the word is not a palendrome")
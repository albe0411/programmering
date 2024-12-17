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
letters = {}

sentence = str(input("input sentence: ").lower())

for i in range(len(sentence)):
    if sentence[i] in letters:
        letters[sentence[i]] += 1
    else:
        letters[sentence[i]] = 1

for x in letters:
    print(str(x) + ": " + str(letters[x]))
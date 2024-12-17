letters = ["a", "b", "h", "d", "o", "c", "e"]

print(letters)
word = input("write a word and the letters that are both in the word and in the list will be removed from the list: ").lower()
print()

for x in word:
    for y in letters:
        if x == y:
            letters.remove(x)

print(letters)
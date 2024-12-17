outer_text = ""
user_input = input()

midle_text = "#  " + user_input + "  #"
for i in range(len(midle_text)):
    outer_text += "#"

print(outer_text)
print(midle_text)
print(outer_text)
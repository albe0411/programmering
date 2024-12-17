import random

input_object = ""
objects = []

print()
print("write a few fings to get a random one of them (write 'done' when you are done): ")
while True:
    input_object = input(": ")
    if input_object != "done":
        objects.append(input_object)
    else:
        break
print()    
random_object = random.randint(0, len(objects) - 1)
print("you got: " + objects[random_object])
print()
import random

yes = ["yes", "yeess"]
maybe = ["maybe", "idk"]
no = ["no", "nooooo"]
answer_types = [yes, maybe, no]

answer_type = random.choice(answer_types)
answer = random.choice(answer_type)

print()
print("the answer is: " + str(answer))
print()
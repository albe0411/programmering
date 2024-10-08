sum1 = 0
sum2 = 0

number1 = input("write a number: ")
number2 = input("write an other number: ")

for i in str(number1): #changes the number to a string to be able to loop through it like a list
    sum1 += int(i) #adds all the numbers together
for i in str(number2):
    sum2 += int(i)

if sum1 == sum2: #compares the numbers
    print(str(sum1) + " = " + str(sum2))
else:
    print(str(sum1) + " ≠ " + str(sum2))
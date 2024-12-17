x = 0
y = 0
def additon(x, y): 
    return(x + y)
def subtraction(x , y):
    return(x - y)
def multiplicaton(x, y):
    return(x * y)
def division(x, y):
    return(x / y)

while True:
    
    print()
    print("welcome to the calculator")
    numbers_calculator_1 = int(input("Write a number: "))
    numbers_calculator_2 = int(input("Write an other number: "))

    question_calculator = input("what do you want to do (add, subtract, multiply, divide): ").lower()
    if question_calculator == "add":
        result = additon(numbers_calculator_1, numbers_calculator_2)
    elif question_calculator == "subtract":
        result = subtraction(numbers_calculator_1, numbers_calculator_2)
    elif question_calculator == "multiply":
        result = multiplicaton(numbers_calculator_1, numbers_calculator_2)
    elif question_calculator == "divide":
        result = division(numbers_calculator_1, numbers_calculator_2)
    else:
        print("unvalid input")

    print(result)
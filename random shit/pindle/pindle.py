import random
from nicegui import ui

def generate_number():
    pincode = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
    return pincode

def check_number():
    user_guess = f"{num0.value}{num1.value}{num2.value}{num3.value}"
    for i in range(4):
        print(user_guess[i])
        if user_guess[i] == pincode[i]:
            num_list[i].props('center-color="green"')
        elif user_guess[i] in pincode:
            num_list[i].props('center-color="yellow"')
        else:
            num_list[i].props('center-color="red"')
        print(num_list[i])

pincode = generate_number()
num_list = []

with ui.row():
    num0 = ui.knob(value=0, max=9, step=1, track_color="gray", show_value=True)
    num1 = ui.knob(value=0, max=9, step=1, track_color="gray", show_value=True)
    num2 = ui.knob(value=0, max=9, step=1, track_color="gray", show_value=True)
    num3 = ui.knob(value=0, max=9, step=1, track_color="gray", show_value=True)
    num_list.append(num0)
    num_list.append(num1)
    num_list.append(num2)
    num_list.append(num3)
    ui.button("guess", on_click=lambda: check_number())

ui.run(native=True)
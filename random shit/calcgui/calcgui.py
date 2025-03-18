from nicegui import ui


def add():
    result_label.text = number1.value + number2.value

def sub():
    result_label.text = number1.value - number2.value

def mul():
    result_label.text = number1.value * number2.value

def div():
    try:
        result_label.text = number1.value / number2.value
    except ZeroDivisionError:
        result_label.text = ':('

with ui.row().classes('place-self-center'):
    number1 = ui.number()
    number2 = ui.number()

with ui.grid(columns=4).classes('place-self-center'):
    ui.button('+', on_click=lambda: add())
    ui.button('-', on_click=lambda: sub())
    ui.button('*', on_click=lambda: mul())
    ui.button('/', on_click=lambda: div())

result_label = ui.label().classes('place-self-center')

ui.run(native=True)
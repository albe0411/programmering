from nicegui import ui

def do_stuff():
    title.text = "im gay"

with ui.row():
    title = ui.label('Hello NiceGUI!')
    ui.button('Click me!', on_click=lambda: do_stuff())



ui.run(native=True)
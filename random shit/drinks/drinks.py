from nicegui import ui

class Drink:
    def __init__(self, ingredients : list):
        self.ingredients = sorted(ingredients)

    def get_cost(self):
        cost = 0
        for i in self.ingredients:
            cost += prices[i]
        return cost

    def get_price(self):
        price = self.get_cost() + self.get_cost() * 1.5
        return price

    def get_name(self):
        name = ""
        for i in self.ingredients:
            if i == "Milk":
                pass
            else:
                name += f"{i} "

        if "Milk" in self.ingredients:
            name += "milkshake"
        elif len(self.ingredients) > 1:
            name += "mixed smoothie"
        else:
            name += "smoothie"
        return name

ingredients = []

def add_ingredient(i):
    if i in ingredients:
        ingredients.remove(i)
    else:
        ingredients.append(i)
    print(ingredients)

def mix_drink():
    drink = Drink(ingredients)
    ui.label(f"{drink.get_cost()}")
    ui.label(f"{drink.get_price()}")
    ui.label(f"{drink.get_name()}")

prices = {
"Strawberries": 15.0,
"Banana": 5.0,
"Mango": 25.0,
"Blueberries": 10.0,
"Raspberries": 10.0,
"Apple": 17.5,
"Pineapple": 35.0,
"Milk": 10
}


"""
drink = Drink(["Strawberries", "Banana"])

print(drink.get_cost())
print(drink.get_price())
print(drink.get_name())
"""


for i in prices.keys():
    ui.button(i, on_click=lambda i = i:add_ingredient(i))

ui.button("mix drink", on_click=lambda: mix_drink())

ui.run(native=True)

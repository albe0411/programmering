import matplotlib.pyplot as plt
import numpy as np

total_sales = 0
day_num = 0

hamburgare_price = 50
pommes_frites_price = 25
läsk_price = 20
milkshake_price = 30
sallader_price = 45
mcnuggets_price = 35

ypoints_add = []

sales_data = [
{"Hamburgare": 150, "Pommes frites": 200, "Läsk": 180, "Milkshake": 40, "Sallader": 30, "McNuggets": 100},
{"Hamburgare": 170, "Pommes frites": 220, "Läsk": 190, "Milkshake": 50, "Sallader": 35, "McNuggets": 105},
{"Hamburgare": 160, "Pommes frites": 210, "Läsk": 185, "Milkshake": 45, "Sallader": 33, "McNuggets": 110},
{"Hamburgare": 180, "Pommes frites": 230, "Läsk": 200, "Milkshake": 55, "Sallader": 40, "McNuggets": 115},
{"Hamburgare": 170, "Pommes frites": 220, "Läsk": 195, "Milkshake": 50, "Sallader": 38, "McNuggets": 120},
{"Hamburgare": 190, "Pommes frites": 240, "Läsk": 210, "Milkshake": 60, "Sallader": 42, "McNuggets": 125},
{"Hamburgare": 185, "Pommes frites": 235, "Läsk": 205, "Milkshake": 58, "Sallader": 40, "McNuggets": 130},
{"Hamburgare": 175, "Pommes frites": 225, "Läsk": 190, "Milkshake": 52, "Sallader": 36, "McNuggets": 120},
{"Hamburgare": 165, "Pommes frites": 215, "Läsk": 185, "Milkshake": 48, "Sallader": 34, "McNuggets": 110},
{"Hamburgare": 180, "Pommes frites": 230, "Läsk": 200, "Milkshake": 55, "Sallader": 39, "McNuggets": 115}
]

for day in sales_data:
    day_sales = 0
    day_num += 1

    day_sales = day["Hamburgare"] * hamburgare_price
    day_sales += day["Pommes frites"] * pommes_frites_price
    day_sales += day["Läsk"] * läsk_price
    day_sales += day["Milkshake"] * milkshake_price
    day_sales += day["Sallader"] * sallader_price
    day_sales += day["McNuggets"] * mcnuggets_price

    print("day " + str(day_num) + ": " + str(day_sales) + " kr")
    ypoints_add.append(day_sales)

    total_sales += day_sales
    
print()
print("total: " + str(total_sales) + " kr")

xpoints = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ypoints = np.array(ypoints_add)
plt.plot(xpoints, ypoints, marker = 'o')
plt.show()
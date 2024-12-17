numbers = [1, 7, 33, 6, 88, -7]

odd_numbers = []
even_numbers = []

for x in numbers:
    if (x / 2).is_integer():
    # (x % 2 == 0) also works
        even_numbers.append(x)
    else:
        odd_numbers.append(x)

print(odd_numbers)
print(even_numbers)
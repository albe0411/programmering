prefectures = ["hokkaido", "aomori", "akita", "iwate", "yamagata", "miyagi", "fukushima", "tochigi", "gunma", "ibaraki", "saitama", "chiba", "tokyo", "kanagawa", "nigata", "toyama", "ishikawa", "fukui", "gifu", "nagano", "yamanashi", "aichi", "shizouka", "shiga", "kyoto", "mie", "nara", "hyogo", "osaka", "wakayama", "tottori", "okayama", "shimane", "hiroshima", "yamaguchi", "kagawa", "tokushima", "ehime", "kochi", "fukuoka", "saga", "nagasaki", "oita", "kumamoto", "miyazaki", "kagoshima", "okinawa"]

print()
print("there are " + str(len(prefectures)) + " prefectures in Japan")
print()
for x in prefectures:
    print(str(x) + " is " + str(len(x)) + " letters long")
    print()
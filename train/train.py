import random

class Passenger:
    def __init__(self, name : str, destination : int):
        self.name = name
        self.destination = destination

    def __repr__(self):
        return f"{self.name}, {self.destination}"

class Wagon:
    def __init__(self, passengers : list[Passenger]):
        self.passengers = passengers
    
    def __repr__(self):
        return f"{self.passengers}"

class Train:
    def __init__(self, wagons : list[Wagon], line : int, position : int):
        self.wagons = wagons
        self.line = line
        self.position = position

    def global_position(self):
        return lines[self.line].stops[self.position]

    def __str__(self):
        return f"{self.line}, {self.position}"

class Station:
    def __init__(self, name : str, passengers : list[Passenger]):
        self.name = name
        self.passengers = passengers

    def __repr__(self):
        return f"{self.name}: {self.passengers}"   

class Line:
    def __init__(self, name : str, stops : list[int]):
        self.name = name
        self.stops = stops

lines = [
    Line("to Shibuya", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), 
    Line("to Yoyogi-uehara", [17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])
]

trains = [
    Train([Wagon([]), Wagon([]), Wagon([])], 0, 0),
    Train([Wagon([]), Wagon([]), Wagon([])], 1, 0)
]

stations = [
    Station("Asakusa", []),
    Station("Tawari machi", []),
    Station("Inaricho", []),
    Station("Ueno", []),
    Station("Ueno-hirekoji", []),
    Station("Suehirocho", []),
    Station("Kanda", []),
    Station("Mitsukoshimae", []),
    Station("Nihombashi", []),
    Station("Kyobashi", []),
    Station("Ginza", []),
    Station("Shimbashi", []),
    Station("Toranomon", []),
    Station("Tameikesanno", []),
    Station("Akasakamutsuke", []),
    Station("Aoyamaitchome", []),
    Station("Gaiemmae", []),
    Station("Omotesando", []),
    Station("Shibuya", []),
    Station("Ayase", []),
    Station("Kita-senju", []), 
    Station("Machiya", []),
    Station("Nishi-nippori", []),
    Station("Sendagi", []), 
    Station("Nezu", []), 
    Station("Yushima", []), 
    Station("Shin-ochanomizu", []), 
    Station("Otemachi", []), 
    Station("Nijubashimae", []), 
    Station("Hibiya", []), 
    Station("Kasumigaseki", []), 
    Station("Kokkai-gijidomae", []), 
    Station("Akasaka", []), 
    Station("Nogizaka", []), 
    Station("Meiji-jingumae", []), 
    Station("Yoyogi-koen", []), 
    Station("Yoyogi-uehara", []), 
]

names = ["ときのそら", "ロボ子さん", "アキ・ローゼンタール", "赤井はあと", 
"白上フブキ", "夏色まつり", "紫咲シオン", "百鬼あやめ", "癒月ちょこ", 
"大空スバル", "AZKi", "大神ミオ", "さくらみこ", "猫又おかゆ", "戌神ころね", 
"星街すいせい", "兎田ぺこら", "不知火フレア", "白銀ノエル", "宝鐘マリン", 
"天音かなた", "角巻わため", "常闇トワ", "姫森ルーナ", "雪花ラミィ", 
"桃鈴ねね", "獅白ぼたん", "尾丸ポルカ", "ラプラス・ダークネス", "鷹嶺ルイ", 
"博衣こより", "沙花叉クロヱ", "風真いろは", "湊あくあ", "桐生ココ", "火威青", 
"音乃瀬奏", "一条莉々華", "儒烏風亭らでん", "轟はじめ", "響咲リオナ", 
"虎金妃笑虎", "水宮枢", "輪堂千速", "綺々羅々ヴィヴィ", "Ayunda Risu", 
"Moona Hoshinova", "Airani Iofifteen", "Kureiji Ollie", "Anya Melfissa", 
"Pavolia Reine", "Vestia Zeta", "Kaela Kovalskia", "Kobo Kanaeru", 
"Mori Calliope", "Takanashi Kiara", "Ninomae Ina’nis", "Gawr Gura", 
"Watson Amelia", "IRyS", "Ouro Kronii", "Nanashi Mumei", "Hakos Baelz", 
"Shiori Novella", "Koseki Bijou", "Nerissa Ravencroft", "Fuwawa Abyssgard", 
"Mococo Abyssgard", "Elizabeth Rose Bloodflame", "Gigi Murin", 
"Cecilia Immergreen", "Raora Panthera", "Tsukumo Sana", "Ceres Fauna", 
"春先のどか", "友人A", "花咲みやび", "奏手イヅル", "アルランディス", 
"律可", "アステル・レダ", "岸堂天真", "夕刻ロベル", "影山シエン", "荒咬オウガ", 
"夜十神封魔", "羽継烏有", "水無世燐央", "Regis Altare", "Axel Syrios", 
"Gavis Bettel", "Machina X Flayon", "Banzoin Hakka", "Josuiji Shinri", 
"Jurard T Rexford", "Goldbullet", "Octavio", "Crimzon Ruze", 
"Kagami Kira", "Magni Dezmond", "Noir Vesper"]


#generating passangers
for i in range(len(stations)):
    for x in range(random.randint(0, 3)):
        name = random.choice(names)
        names.remove(name)
        destination_options = []
        for line in lines:
            if i in line.stops:
                destination_options += line.stops
        passenger = Passenger(name, random.choice(list(dict.fromkeys(destination_options))))
        stations[i].passengers.append(passenger)


#game loop
for x in range(0, 60):

    #get on
    for train in trains:
        print(train)
        for passenger in stations[train.global_position()].passengers:
            print(passenger)
            for stop in lines[train.line].stops:
                if passenger.destination == stop:
                    train.wagons[random.randint(0, 2)].passengers.append(passenger)
                    stations[train.global_position()].passengers.remove(passenger)
        for i in train.wagons:
            print(i)

    #get off
        for wagon in train.wagons:
            for passenger in wagon.passengers:
                if passenger.destination == train.global_position():
                    stations.append(passenger)
                    wagon.passengers.remove(passenger)
    print()
    print()

    #next station
    for train in trains:
        train.position += 1
        if train.position == len(lines[train.line].stops):
            train.position = 0
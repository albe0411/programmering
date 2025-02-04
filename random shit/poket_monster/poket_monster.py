import random
import copy

class Action:
    def __init__(self, name : str, element : str, self_damage : int, target_damage : int):
        self.name = name
        self.element = element
        self.self_damage = self_damage
        self.target_damage = target_damage

    def __str__(self):
        return f"{self.name}; {self.element}; {self.self_damage}; {self.target_damage}"

class Monster:
    def __init__(self, name : str, element : str, health : int, attack : int, defence : int, actions : list):
        self.name = name
        self.element = element
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defence = defence
        self.actions = actions
        self.dead = False

    def health_check(self):
        if self.health > self.max_health:
            self.health = self.max_health
        elif self.health <= 0:
            self.health = 0
            self.dead = True

    def take_damage(self, attacker, action):
        effect = 1
        match action.element:
            case "fire":
                match self.element:
                    case "grass":
                        effect = 2
                        print("it was incredibly effective")
                    case "water":
                        effect = 0.5
                        print("it was somewhat effective")
                    case _:
                        effect = 1

            case "water":
                match self.element:
                    case "fire":
                        effect = 2
                        print("it was incredibly effective")
                    case "grass", "electric":
                        effect = 0.5
                        print("it was somewhat effective")
                    case _:
                        effect = 1

            case "grass":
                match self.element:
                    case "water":
                        effect = 2
                        print("it was incredibly effective")
                    case "fire":
                        effect = 0.5
                        print("it was somewhat effective")
                    case _:
                        effect = 1

            case "electric":
                match self.element:
                    case "water":
                        effect = 2
                        print("it was incredibly effective")
                    case _:
                        effect = 1 
            case _:
                pass      

        self.health -= round(50 * (attacker.attack/self.defence) * effect * (action.target_damage/50))
        self.health_check()

    def perform_action(self, target, action):
        if not self.dead:
            self.health -= action.self_damage
            target.take_damage(self, action)
            self.health_check()

    def get_health(self):
        return self.health

    def __str__(self):
        return f"health: {self.health}, {self.attack}, {self.defence}, moveset: {self.actions}"

def wild_battle():
    global score
    opponent = copy.copy(random.choice(monsters))
    print("the opposing monster turns out to be a", opponent.name)

    while not player_monster.dead and not opponent.dead:
        try:
            print()
            print("pick an action")
            counter = 0
            for i in player_monster.actions:
                counter += 1
                print(f"{counter}. {i.name}")
            player_input = int(input(": ")) - 1
            player_monster.perform_action(opponent, eval(f"player_monster.actions[{player_input}]"))
            opponent.perform_action(player_monster, random.choice(opponent.actions))
            print()
            print(f"your monsters health: {player_monster.get_health()}")
            print(f"opposing monsters health: {opponent.get_health()}")
        except KeyboardInterrupt:
            break
        except ValueError:
            print("ValueError")
    if player_monster.dead:
        print("your monster died")
    elif opponent.dead:
        print("the opposing monster was brutally killed")
        player_monster.health += 20
        player_monster.health_check()
        score += 1


actions = [
    Action("tak dawn", "normal", 15, 70),
    Action("fame throuwer", "fire", 0, 50),
    Action("vine wipp", "grass", 0, 50),
    Action("wa'a goon", "water", 0, 50),
    Action("tunder shouk", "electric", 0, 50),
    Action("photosynthesis", "grass", -40, 0),
]

monsters = [
    Monster("Faiagurasukyanon", "fire", 80, 80, 45, [actions[0], actions[1], actions[4]]), 
    Monster("Gurasutanku", "grass", 150, 40, 100, [actions[2], actions[5]]), 
    Monster("denkitenki", "electric", 100, 65, 65, [actions[0], actions[4]]),
    Monster("kami-sama", "normal", 90, 60, 60, [actions[0]]),
    Monster("sakana", "water", 150, 50, 70, [actions[3], actions[5]])
]


print()
print("This is poket monsters, (please don't sue me)")

score = 0
while True:
    try:
        print()
        print("what monster do you want?")
        counter = 0
        for i in monsters:
            counter += 1
            print(f"{counter}. {i.name}")
        player_input = int(input(": ")) -1

        player_monster = copy.copy(eval(f"monsters[{player_input}]"))
        break
    except KeyboardInterrupt:
        break
    except ValueError:
        print("ValueError")
    

while not player_monster.dead:
    print()
    print("you enconterd a wild monster")
    print("what do you want to do?")
    print("1. fight")
    print("2. run")
    player_input = input(": ")
    print()

    if player_input == "1":
        wild_battle()
    elif player_input == "2":
        print("you ran away from your responsibility as a human being")
        print("but what good did it do?")
    else:
        print("you have to make a proper decision")

print("your score:", score)
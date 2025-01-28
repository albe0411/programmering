#it sucks
#I over compicated things and wanted to add things
#so I ran out of time
#and now it half done
#I have at least commented the biggest problems

class Monster:
    def __init__(self, name : str, health : int, attack_power : int):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def is_alive(self):
        if self.health <= 0:
            return False
        else:
            return True
        #can still have less than 0 hp

    def take_damage(self, damage : int):
        self.health -= damage
        if self.is_alive():
            print(self.name, "take", damage, "damage,", self.health, "remaining.")
        else:
            print(self.name, "take", damage, "damage, and is now dead.")
        #can take negetiv damage for healing (no limit to how much or how little hp a monster can have)

    def __str__(self):
        return f"name: {self.name}, health: {self.health}"

class Dragon(Monster):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)

    def fire_breath(self):
        target = input(": ")
        print(target, "took", self.attack_power, "fire damage")
        #does nothing

    def bite(self):
        target = input(": ")
        print(target, "took", self.attack_power, "physical damage")
        #does nothing

class Vampire(Monster):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
    
    def bite(self):
        target = input(": ")
        self.health += 20
        print(target, "took", self.attack_power, "physical damage and you heald 20 hp")
        #does prity much nothing

vampire1 = Vampire("Jaguar", 300, 70)
dragon1 = Dragon("Martin", 1000, 80)

while True:
    try:
        #it's the best system, I know
        comand = input("/")
        exec(comand)
    except NameError:
        print("NameError")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        break
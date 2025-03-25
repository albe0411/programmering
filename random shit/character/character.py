from nicegui import ui
import random

class Character:
    def __init__(self, f_name : str, l_name : str, race : str, age : int, gender : bool, occupation : str, traits : list, dere_type : str):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        if gender:
            self.gender = "male"
        else:
            self.gender = "female"
        self.race = race
        self.occupation = occupation
        self.traits = traits
        self.dere_type = dere_type

    def __str__(self):
        return [f"Name: {self.f_name} {self.l_name}",
            f"Age: {self.age}", 
            f"Gender: {self.gender}",
            f"Race: {self.race}", 
            f"Occupation: {self.occupation}",
            f"Traits: {self.traits[0]} and {self.traits[1]}",
            f"Dere type: {self.dere_type}"]

def generate_character():
    character = Character(
        random.choice(f_name_list),
        random.choice(l_name_list),
        random.choice(race_list),
        random.randint(0, 500),
        bool(random.getrandbits(1)),
        random.choice(occupation_list),
        random.sample(trait_list, k=2),
        random.choice(dere_type_list)
        )

    name.text = character.__str__()[0]
    age.text = character.__str__()[1]
    gender.text = character.__str__()[2]
    race.text = character.__str__()[3]
    occupation.text = character.__str__()[4]
    traits.text = character.__str__()[5]
    dere_type.text = character.__str__()[6]

f_name_list = [
    "Aelarion", "Thalindra", "Baldric", "Galadriel", "Eldrin", 
    "Isolde", "Caldar", "Vespera", "Fendral", "Zalathar", 
    "Lirael", "Raventhorn", "Sylas", "Mirael", "Oberon", 
    "Elyndor", "Nyx", "Aeloria", "Kethar", "Morrigan", 
    "Thrain", "Astrid", "Kaelen", "Varian", "Firael", 
    "Shandris", "Daerion", "Tyria", "Gareth", "Lorcan", 
    "Nymeria", "Rhaegar", "Talindra", "Jorath", "Valkira",
    "Branwen", "Valloran", "Lyanna", "Drakmar", "Elara",
    "Thalion", "Eldric", "Cynthia", "Dorian", "Faelorn",
    "Virelia", "Mordrin", "Soren", "Kylira", "Fenris",
    "Rowan", "Gorath", "Aeris", "Corvin", "Faelana",
    "Vellinor", "Zariel", "Cylas", "Ariella", "Zephyra",
    "Syllis", "Karael", "Beren", "Orion", "Valandra",
    "Theon", "Althaea", "Kovira", "Draven", "Raelis",
    "Adalyn", "Kelvar", "Talyndra", "Zorath", "Lilith",
    "Vornak", "Ysolde", "Malethar", "Arius", "Galathor",
    "Zarathos", "Selene", "Liraelith", "Draegon", "Arieth",
    "Vaelen", "Merith", "Galenar", "Inara", "Orlith",
    "Serrath", "Tornik", "Rynn", "Daelith", "Valrond",
    "Ravena", "Varden", "Nerith", "Baelros", "Arius", 
    "Raegar", "Brindar", "Drestan", "Vaelor", "Thorin",
    "Selveth", "Galadorn", "Draken", "Mirelith", "Kaldar",
    "Viora", "Kendal", "Valthar", "Lyria", "Xanderis",
    "Aeriseth", "Tanithra", "Valros", "Lareth", "Vornor",
    "Elvandar", "Saphira", "Korran", "Quorath", "Thyra",
    "Ilian", "Gryndal", "Aelix", "Oriana", "Kendrith",
    "Orlanth", "Malrith", "Gorwyn", "Ferlis", "Aethlan"
]

l_name_list = [
    "Stormbringer", "Nightshade", "Ironfoot", "Moonwhisper", "Silverthorn",
    "Darkwater", "Windrider", "Fireblade", "Blackstone", "Shadowfall",
    "Flameheart", "Swiftstrike", "Stonefist", "Wolfsbane", "Dawnbringer",
    "Starcaller", "Thundershield", "Brightmantle", "Earthwarden", "Frostvale",
    "Skyward", "Blacksoul", "Silverbrook", "Grimblade", "Ironclaw",
    "Silverstream", "Greystone", "Dewdrop", "Thornheart", "Frostwind",
    "Moonstone", "Ironbark", "Dreadshadow", "Wolfthorn", "Ashenforge",
    "Redfury", "Firewing", "Stoneflame", "Wyrmscale", "Falconcrest",
    "Stormhammer", "Ironvale", "Dreadfoot", "Sunfire", "Bloodthorn",
    "Darkflame", "Silverstone", "Moonfang", "Sunspear", "Ravenshadow",
    "Falconheart", "Viperclaw", "Thornbloom", "Steelwind", "Shadowthorn",
    "Windspeaker", "Stormwatch", "Blackfang", "Shadowstrike", "Silverclaw",
    "Brimstone", "Fireheart", "Cindermoon", "Darkforge", "Redstone",
    "Ironhold", "Stormspire", "Hawke", "Morningshade", "Ironhelm",
    "Thunderfury", "Grimspire", "Froststone", "Ravenswing", "Ashwalker",
    "Blackthorn", "Dawnblade", "Stormrider", "Redwing", "Moonhunter",
    "Flamestrike", "Steelheart", "Thunderwing", "Nightbloom", "Stonevale",
    "Brackenshield", "Sunthorn", "Frosthammer", "Ravencall", "Earthroot",
    "Blazeheart", "Darkwhisper", "Brightstone", "Gravelight", "Windwalker",
    "Taloncrest", "Sunsworn", "Moonshadow", "Shadowfury", "Dreadbane",
    "Windfury", "Frostfang", "Ironfang", "Darksky", "Stonebloom",
    "Starforge", "Frostwhisper", "Firestorm", "Steelthorn", "Darkraven",
    "Grimsworn", "Ashflame", "Sunbloom", "Bloodsworn", "Icebreaker",
    "Ravenspire", "Dreadfang", "Stormfang", "Silverwind", "Lightshroud",
    "Shadowbrook", "Flamebloom", "Ironthorn", "Nightbloom", "Sunflare"
]

race_list = [
    "human", "Elf", "Dwarf", "Orc", "Troll", "Giant",
    "Dragonborn", "Tiefling", "Gnome", "Halfling", "Vampire",
    "Werewolf", "Fairy", "Nymph", "Centaur", "Merfolk",
    "Minotaur", "Dryad", "Shapeshifter", "Fey", "Angel",
    "Demon", "Djinn", "Kitsune", "Chimera", "Aarakocra",
    "Yeti", "Lich", "Griffin", "Hobgoblin", "Satyr",
    "Valkyrie", "Banshee", "Elder Dragon", "Sphinx"
]

occupation_list = [
    "Dragon Rider", "Potion Master", "Enchanter", "Spellsmith", "Rune Weaver",
    "Necromancer", "Beast Tamer", "Knight of the Eternal Order", "Witch Hunter", "Divination Seer",
    "Elemental Summoner", "Alchemist", "Treasure Hunter", "Guardian of the Sacred Forest", "Elemental Engineer",
    "Illusionist", "Time Traveler", "Skyship Navigator", "Arcane Librarian", "Crystal Shaper",
    "Shape-Shifter", "Fey Messenger", "Rune Scholar", "Arcane Architect", "Astral Cartographer",
    "Shadow Walker", "Celestial Guide", "Soulbinder", "Mystic Falconer", "Dream Weaver",
    "Blacksmith", "Carpenter", "Miller", "Farmer", "Tanner", "Merchant", "Baker", "Herbalist", 
    "Scribe", "Armorer","Barber Surgeon", "Falconer", "Apothecary", "Lumberjack", "Minstrel",
    "Stable Master", "Innkeeper", "Town Crier", "Jester", "Guard Captain",
    "Woodsman", "Court Advisor", "Shipwright", "Cook", "Ranger"
]

trait_list = [
    "Fearlessly Brave", "Exceedingly Cunning", "Incredibly Wise", "Unwaveringly Loyal", "Nobly Honorable",
    "Endlessly Curious", "Deeply Compassionate", "Fiercely Vengeful", "Unyieldingly Patient", "Unfailingly Trustworthy",
    "Magnetically Charming", "Obstinately Stubborn", "Astoundingly Resourceful", "Rashly Hot-headed",
    "Acutely Shrewd", "Overwhelmingly Generous", "Unstoppably Ambitious", "Radically Selfless",
    "Intensely Jealous", "Unflinchingly Fearless", "Unbreakably Strong", "Incredibly Dexterous", "Unyieldingly Tough",
    "Astoundingly Intelligent", "Profoundly Wise", "Charismatically Persuasive", "Exceptionally Lucky",
    "Indestructibly Enduring", "Incredibly Speedy", "Amazingly Agile", "Keenly Perceptive", "Unbelievably Stealthy",
    "Laser-Focused", "Iron-willed and Resolute", "Magically Gifted", "Masterfully Crafted", "Unfailingly Inspirational",
    "Unshakably Iron-willed", "Sharply Accurate", "Incredibly Resilient", "Perpetually Youthful", "Totally Blind",
    "Uncontrollably Furious", "Invisibly Bound at Night", "Eternally Voiceless",
    "Unhealing and Cursed", "Chronically Unlucky", "Terrified of Fire", "Frozen by Touch", "Endlessly Hungry",
    "Cursed to Speak Riddles", "Irreversibly Beastly", "Forever Sleep-bound", "Permanently Shadow-marked",
    "Compelled to Tell the Truth", "Endlessly Falling", "Lost and Wandering Forever", "Unfailingly Unlucky",
    "Unstoppably Laughing", "Haunted by Voices", "Darkly Humorous", "Dryly Witty", "Exceptionally Sarcastic",
    "Absurdly Comedic", "Uncontrollably Slapstick", "Ironically Hilarious", "Pun-obsessed", "Self-deprecatingly Funny",
    "Unpredictably Situational", "Wordplay Genius", "Prankster Extraordinaire", "Sillily Antics", "Banter-filled",
    "Cleverly Retorted", "Teasingly Playful", "Mischievously Witty", "Outrageously Ridiculous", "Dramatically Absurd",
    "Sarcastically Observant", "Playfully Mocking", "Racist", "Sexist", "Elitist", "Narrow-minded", "Bigoted",
    "Arrogant", "Ignorant", "Prejudiced", "Discriminatory", "Self-righteous", "Xenophobic", "Unforgiving",
    "Greedy", "Lazy", "Selfish", "Manipulative", "Hypocritical", "Cowardly", "Dishonest", "Entitled",
    "Inconsiderate", "Pessimistic", "Vindictive", "Intolerant", "Egotistical", "Gullible", "Self-centered",
    "Deceitful", "Cold-hearted", "Shallow", "Judgmental", "Impulsive", "Overbearing"
]

dere_type_list = [
    "Bakadere", "biridere", "Bocchandere", "bokodere", 
    "Butsudere", "Byoukidere", "Dandere", "Darudere", 
    "Deredere", "Dorodere", "Erodere", "Gandere", 
    "Gesudere", "Goudere", "Gundere", "Gurodere", 
    "Hajidere", "Himedere", "Hindere", "Kamidere", 
    "Kanedere", "Kekkondere", "Kichidere", "Kiridere", 
    "Kuudere", "Kuzudere", "M Dere", "Nemuidere", 
    "Nyandere", "Ojoudere", "Onidere", "Osadere", 
    "Oujidere", "Oujodere", "Rindere", "Roshidere", 
    "S Dere", "Sashidere", "Shindere", "Shundere", 
    "Smugdere", "Sunao Cool", "Sunao Heat", "Sunao Surreal", 
    "Teasedere", "Thugdere", "Tsundere", "Tsuyodere", 
    "Undere", "Usodere", "Utsodere", "Wandere", "Yandere", 
    "Yoidere", "Zondere"
]

ui.button("Generate character", on_click=lambda: generate_character())

name = ui.label()
age = ui.label()
gender = ui.label()
race = ui.label()
occupation = ui.label()
traits = ui.label()
dere_type = ui.label()

ui.run(native=True)
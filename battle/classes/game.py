import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#create the character
class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    '''
    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)
    '''

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return self.hp

    #utility classes/ methods
    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp
        
    def reduce_mp(self, cost):
        self.mp -= cost

    '''
    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mpcost(self, i):
        return self.magic[i]["cost"]
    '''

    def choose_action(self):
        print("action")
        i = 1
        for item in self.actions:
            print("    " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        print("magic")
        i = 1
        for spell in self.magic:
            print("    " + str(i) + ":", spell.name, ", cost:", spell.cost)
            i += 1

    def choose_item(self):
        print("items")
        i = 1
        for item in self.items:
            print("    " + str(i) + ".", item["item"].name, ":", item["item"].description, " x", str(item["quantity"]))
            i += 1

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "Target: " + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("    " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input("Choose target:")) - 1
        while choice > (len(enemies) - 1) or choice is None:
            print("Please choose within the list.")
            choice = int(input("Choose target:")) - 1
        return choice

    def get_enemy_stats(self):
        hp_bar = ""
        hp_ticks = (self.hp / self.maxhp) * 100 / 2

        while hp_ticks > 0:
            hp_bar += "█"
            hp_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        # current_hp = str(self.hp) + "/" + str(self.maxhp)

        if len(hp_string) < 11:
            Decreased = 11 - len(hp_string)

            while Decreased > 0:
                current_hp +=  " "
                Decreased -=1

            current_hp += hp_string
        else:
            current_hp = hp_string

        MP_bar = ""
        MP_bar_ticks = (self.mp / self.maxmp) * 100 / 10
        while MP_bar_ticks > 0:
            MP_bar += "█"
            MP_bar_ticks -= 1

        while len(MP_bar) < 10:
            MP_bar += " "

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        # current_mp = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""
        
        if len(mp_string) < 2:
            decreased = 9 - len(mp_string)
            
            while decreased > 0:
                current_mp += " "
                decreased -= 1
                
                current_mp += mp_string
        else:
            current_mp = mp_string

        print(bcolors.BOLD + self.name + ":     " + current_hp + "|" + bcolors.OKGREEN + hp_bar
            + bcolors.ENDC+ "| HP\n            " + bcolors.BOLD + current_mp
            + "  |" + bcolors.OKBLUE + MP_bar + bcolors.ENDC + "| MP")

    #print out the stats
    def get_stats(self):
        HP_bar = ""
        HP_bar_ticks = (self.hp/self.maxhp) * 100 /4
        while HP_bar_ticks > 0:
            HP_bar += "█"
            HP_bar_ticks -= 1

        while len(HP_bar) < 25:
            HP_bar += " "

        MP_bar = ""
        MP_bar_ticks = (self.mp / self.maxmp) * 100 / 10
        while MP_bar_ticks > 0:
            MP_bar += "█"
            MP_bar_ticks -= 1

        while len(MP_bar) < 10:
            MP_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        # current_hp = str(self.hp) + "/" + str(self.maxhp)

        if len(hp_string) < 9:
            Decreased = 9 - len(hp_string)

            while Decreased > 0:
                current_hp +=  " "
                Decreased -=1

            current_hp += hp_string
        else:
            current_hp = hp_string
          
        mp_string = str(self.mp) + "/" + str(self.maxmp)
        # current_mp = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""
        
        if len(mp_string) < 2:
            decreased = 9 - len(mp_string)
            
            while decreased > 0:
                current_mp += " "
                decreased -= 1
                
                current_mp += mp_string
        else:
            current_mp = mp_string
         
        print(bcolors.BOLD + self.name + ":     " + current_hp + "  |" + bcolors.OKGREEN + HP_bar
            + bcolors.ENDC+ "| HP\n            " + bcolors.BOLD + current_mp
            + "  |" + bcolors.OKBLUE + MP_bar + bcolors.ENDC + "| MP")

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        print("magic_choice", magic_choice)
        spell = self.magic[magic_choice]
        print("spell", spell)
        magic_dmg = spell.generate_damage()

        pct = self.hp / self.maxhp * 100

        if self.mp < spell.cost or spell.type == "white" and pct > 50:
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg
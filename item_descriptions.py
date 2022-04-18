import system_methods
import game_mechanics_methods

def fist():
    print('''
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|                                   ___ ___ ___ _____                    |
|                                  | __|_ _/ __|_   _|                   |
|                                  | _| | |\__ \ | |                     |
|                                  |_| |___|___/ |_|                     |
|                                                                        |             
|           ,--.--._                                                     |
|    ------" _, \___)       DESCRIPTION: It's a fist. I mean...          |
|            / _/____)      You punch things with it. You've had         |
|            \//(____)      them all your life.                          |
|    ------\     (__)                                                    |
|            `-----"                                                     |
|                                                                        |
|                           DAMAGE: 1d6                                  |
|                                                                        |
|                                                                        |
|________________________________________________________________________|

|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|   |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|        EQUIP        |   |        BACK         |
|_____________________|   |_____________________|
    ''')

def longsword():
    print('''
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|                 _    ___  _  _  ___ _____      _____  ___ ___          |
|                | |  / _ \| \| |/ __/ __\ \    / / _ \| _ \   \         |
|        o       | |_| (_) | .` | (_ \__ \\\\ \/\/ / (_) |   / |)|         |
|        X       |____\___/|_|\_|\___|___/ \_/\_/ \___/|_|_\___/         |
|        X                                                               |   
|   |===[O]===|                                                          |   
|       |||         DESCRIPTION: You've had this sword since you         |
|       |||         started adventuring. It's rusting a bit and could    |
|       |||         use a good sharpening.                               |   
|       |||                                                              |
|       |||                                                              |
|       |||                                                              | 
|       |||                                                              |
|       |||         DAMAGE: 1d8 + 4                                      |
|       |||                                                              |   
|       |^|                                                              |
|       \ /                                                              |   
|        `                                                               |   
|________________________________________________________________________|

|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|   |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|        EQUIP        |   |        BACK         |
|_____________________|   |_____________________|
''')

def battleaxe():
    print('''
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|                      ___   _ _____ _____ _    ___   _   __  _____      |
|       ,  /\  .      | _ ) /_\_   _|_   _| |  | __| /_\  \ \/ / __|     |  
|      //`-||-'\\\\     | _ \/ _ \| |   | | | |__| _| / _ \  >  <| _|      |
|     (| -=||=- |)    |___/_/ \_\_|   |_| |____|___/_/ \_\/_/\_\___|     |
|      \\\\,-||-.//                                                        |
|       `  ||  '                                                         |
|          ||          DESCRIPTION: A solid axe with a plain wooden      |
|          ||          handle. This was given to you grandfather from    |
|          ||          an old dwarven merchant. Or was it stolen?        |
|          ||                                                            |
|          ||                                                            |
|          ||                                                            |
|          ()          DAMAGE: 1d12 + 2                                  |
|                                                                        |
|                                                                        |
|________________________________________________________________________|

|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|   |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|        EQUIP        |   |        BACK         |
|_____________________|   |_____________________|
''')
def knife():
    print('''
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|            _  _   _   ___ _______   __  _  ___  _ ___ ___ ___          |
|           | \| | /_\ / __|_   _\ \ / / | |/ / \| |_ _| __| __|         |
|    .      | .` |/ _ \\ __ \ | |  \ V /  | ' <| .` || || _|| _|          |
|   / \\     |_|\_/_/ \_\___/ |_|   |_|   |_|\_\_|\_|___|_| |___|         |
|   |.|                                                                  |
|   |.|                                                                  |
|   |:|              DESCRIPTION: A small simple kife covered in         |
|   |:|              some sort of residue or slime. It's pretty          |
|  `-8-'             rusty.                                              |
|    8                                                                   |
|    O               DAMAGE: 1d4+3                                       |
|                                                                        |
|________________________________________________________________________|

|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|   |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|        EQUIP        |   |        BACK         |
|_____________________|   |_____________________|
''')

def five():
    print('''
This is image five
''')


def view_weapons_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions):
    system_methods.clear_console()
    game_mechanics_methods.player_stat_bar(name, player_hp, player_ac, player_race)
    print()
    print()
    print(f'''
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|   SLOT #        ITEM       |
|____________________________|       
 ''')
    game_mechanics_methods.count_list(player_weapons)
    print('______________________________')
    print()
    print('''
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|   |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|      VIEW ITEM      |   |        BACK         |
|_____________________|   |_____________________|
''')
    print()
    print('What do you want to do? ')
    print()
    while True:
        choice = input(str('Choice: '))
        choice = choice.lower()
        if choice == 'back':
            game_mechanics_methods.weapons_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        elif choice == 'view item':
            break
        else:
            input('Invalid input. Press Enter to try again...')
            view_weapons_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)


    ####CHECKING IF NUMBERS ARE WITHING THE RANGE OF ITEMS IN INVENTORY
    #slot_numbers = len(player_weapons)
    #item = game_mechanics_methods.check_number(slot_numbers, 'view')

    #TURN USER INPUT INTO THE WEAPON IN THE CORRESPONDING SLOT
    #l = []
    #l.append(item)

    #item_index = item-1
    #item = player_weapons[item_index]
    while True:
        print()
        choice = input(str('Name of item to view: '))
        choice = choice.lower()
        if choice == 'fist':
            system_methods.clear_console()
            game_mechanics_methods.player_stat_bar(name, player_hp, player_ac, player_race)
            print()
            print()
            fist()
            while True:
                print()
                choice = input(str('Choice: '))
                choice = choice.lower()
                if choice == 'equip':
                    game_mechanics_methods.equip_menu_one(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
                elif choice == 'back':
                    view_weapons_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
                else:
                    print()
                    input('Invalid input. Press Enter to try again...')
        elif choice == 'longsword':
            system_methods.clear_console()
            game_mechanics_methods.player_stat_bar(name, player_hp, player_ac, player_race)
            print()
            print()
            longsword()
            while True:
                print()
                choice = input(str('Choice: '))
                choice = choice.lower()
                if choice == 'equip':
                    game_mechanics_methods.equip_menu_one(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
                elif choice == 'back':
                    view_weapons_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
                else:
                    print()
                    input('Invalid input. Press Enter to try again...')
        elif choice == 'battleaxe':
            system_methods.clear_console()
            game_mechanics_methods.player_stat_bar(name, player_hp, player_ac, player_race)
            print()
            print()
            battleaxe()
            while True:
                print()
                choice = input(str('Choice: '))
                choice = choice.lower()
                if choice == 'equip':
                    game_mechanics_methods.equip_menu_one(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
                elif choice == 'back':
                    view_weapons_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
                else:
                    print()
                    input('Invalid input. Press Enter to try again...')
        elif choice == 'nasty knife':
            system_methods.clear_console()
            knife()
            print()
            while True:
                choice = input(str('Choice: '))
                choice = choice.lower()
                if choice == 'equip':
                    game_mechanics_methods.equip_menu_one(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
                elif choice == 'back':
                    view_weapons_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
                else:
                    print()
                    input('Invalid input. Press Enter to try again...')
        else:
            input('Invalid input. Press Enter to try again...')
            view_weapons_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
 
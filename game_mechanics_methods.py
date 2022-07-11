import time
import textwrap as tw
import inspect
import system_methods
import assets
import main
import item_descriptions
import area_one_combat_methods
import random
import area_one_dialogue
import potion_descriptions

def game_instructions():
    while True:
            user_response = input('Need the instructions? YES or NO: ')
            user_response = user_response.lower()
            if user_response == 'yes':
                print()
                p42 = inspect.cleandoc('''This is a text-based adventure game. Scenarios are delivered in text form and you need use theater of the mind to visualize
                what's going on. Pretty cool! At the end of some statements there will be a few choices in UPPERCASE letters like, RUN or FIGHT. You'll then be asked to
                choose your response. Like this: "Choice: " You don't need to type it in UPPERCASE letters. After you give your response different outcomes can happen.''')
                system_methods.delay_print(tw.fill(p42, width=75))
                print()
                p43 = inspect.cleandoc('''But beware! Anything can happen. If you make the wrong choices, it could be deadly. Good luck!''')
                system_methods.delay_print(tw.fill(p43, width=75))
                print()
                break
            elif user_response =='no':
                print()
                system_methods.delay_print('Good luck then adventurer!')
                print()
                break
            else:
                system_methods.delay_print('Invalid input. Try again.')
                print()
                system_methods.delay_print('Press Enter to try again...')
                input()
                system_methods.clear_console()
    print()
    input('Press Enter to start game.')

def game_start():
    pass

def play_again():
    print()
    play_again_response = input('Play again? YES or NO: ')

    play_again_response = play_again_response.lower()
    while True:
        if play_again_response == 'yes':
            print()
            main.main()
            
        elif play_again_response == 'no':
            print()
            system_methods.delay_print('Thanks for playing!')
            print()
            time.sleep(3)
            exit()
        else:
            print()
            input('Invalid input. Press Enter to try again.')
            play_again()

def you_died(enemy_type): 
    p41 = inspect.cleandoc(f'As the {enemy_type} makes its final attack, you feel a coldness come over your body. You fall to the ground and the room goes black.')
    system_methods.delay_print(tw.fill(p41, width=75))
    print()
    input('Press Enter to continue...')
    
    system_methods.clear_console()
    assets.you_died_image()
    time.sleep(5)
    print()
    print()
    play_again()

def name_check():
    while True:
        player_name = input("What's your name? ")
        player_name= player_name.lower()
        print()
        name_answer = input((f'Your name is, {player_name.capitalize()}. Right? YES or NO: '))
        if name_answer == 'yes':
            god_mode(player_name)
            return player_name
        else:
            print()
            print('Okay, let\'s try again!')
            print()

def god_mode(player_name):
    if player_name == 'saitama':
        system_methods.clear_console()
        assets.saitama_image()
        time.sleep(4)
        system_methods.clear_console()
        system_methods.delay_print('Welcome Master Saitama. Enjoy the adventure.')
        time.sleep(3)
        print()
        print()
        player_race = 'superhuman'
        player_gold = 100
        player_hp, player_ac, player_weapons, player_potions = race_stats(player_race)
        print(f'Name: {player_name.capitalize()} | Race: {player_race.capitalize()} | Hit Points: {player_hp} | Armor Class: {player_ac}')
        print()
        print()
        input("Press Enter to begin...")
        print()
        system_methods.clear_console()
        area_one_dialogue.main_dialogue(player_name, player_race, player_hp, player_ac, player_gold, player_weapons, player_potions)
    else:
        return player_name

def race_stats(race):
    if race == 'halfling':
        hp = 22
        ac = 13
        weapons = ['FIST', 'LONGSWORD', 'BATTLEAXE']
        potions = ['POTION OF HEALTH', 'POTION OF HEALTH', 'POTION OF HEALTH']
        return hp, ac, weapons, potions
    elif race == 'dwarf':
        hp = 33
        ac = 17
        weapons = ['FIST', 'LONGSWORD', 'BATTLEAXE']
        potions = ['POTION OF HEALTH', 'POTION OF HEALTH', 'POTION OF HEALTH']
        return hp, ac, weapons, potions
    elif race == 'elf':
        hp = 30
        ac = 16
        weapons = ['FIST', 'LONGSWORD', 'BATTLEAXE']
        potions = ['POTION OF HEALTH', 'POTION OF HEALTH', 'POTION OF HEALTH']
        return hp, ac, weapons, potions
    elif race == 'superhuman':
        hp = 1000000
        ac = 1000
        weapons = ['FIST', 'FIST']
        potions = []
        return hp, ac, weapons, potions
    else:
        hp = 25
        ac = 16
        weapons = ['FIST', 'LONGSWORD', 'BATTLEAXE']
        potions = ['POTION OF HEALTH', 'POTION OF HEALTH', 'POTION OF HEALTH']
        return hp, ac, weapons, potions 

def race_check():
    while True:
        player_race = input("Are you a HALFLING, DWARF, ELF, or HUMAN? ")
        player_race = player_race.lower()
        if player_race == 'halfling' or player_race == 'dwarf' or player_race == 'elf' or player_race == 'human':
            return player_race
        else:
            print()
            print('Not a valid input. Try again')
            print()

def race_hp_for_health(race):
    if race == 'halfling':
        hp = 22
        return hp
    elif race == 'dwarf':
        hp = 33
        return hp
    elif race == 'elf':
        hp = 30
        return hp
    elif race == 'superhuman':
        hp = 1000000
        return hp
    else:
        hp = 25
        return hp
    
#### HEALTH POTIONS

### HEALTH BAR
def health_bar(player_race, current_health):

    player_max_health = race_hp_for_health(player_race)

    if current_health == player_max_health:
        health_percentage = 100
    else:   
        health_percentage = round(current_health/player_max_health, 2)

    healthbar = ''

    if health_percentage == 100:
        healthbar = '████████████████████'
    elif health_percentage >= .95 and health_percentage < 1:
        healthbar = '███████████████████ '
    elif health_percentage >= .90 and health_percentage <= .95:
        healthbar = '██████████████████  '
    elif health_percentage >= .85 and health_percentage <= .90:
        healthbar = '█████████████████   '
    elif health_percentage >= .80 and health_percentage <= .85:
        healthbar = '████████████████    '
    elif health_percentage >= .75 and health_percentage <= .80:
        healthbar = '███████████████     '
    elif health_percentage >= .70 and health_percentage <= .75:
        healthbar = '██████████████      '
    elif health_percentage >= .65 and health_percentage <= .70:
        healthbar = '█████████████       '
    elif health_percentage >= .60 and health_percentage <= .65:
        healthbar = '████████████        '
    elif health_percentage >= .55 and health_percentage <= .60:
        healthbar = '███████████         '
    elif health_percentage >= .50 and health_percentage <= .55:
        healthbar = '██████████          '
    elif health_percentage >= .45 and health_percentage <= .50:
        healthbar = '█████████           '
    elif health_percentage >= .40 and health_percentage <= .45:
        healthbar = '████████            '
    elif health_percentage >= .35 and health_percentage <= .40:
        healthbar = '███████             '
    elif health_percentage >= .30 and health_percentage <= .35:
        healthbar = '██████              '
    elif health_percentage >= .25 and health_percentage <= .30:
        healthbar = '█████               '
    elif health_percentage >= .20 and health_percentage <= .25:
        healthbar = '████                '
    elif health_percentage >= .15 and health_percentage <= .20:
        healthbar = '███                 '
    elif health_percentage >= .10 and health_percentage <= .15:
        healthbar = '██                  '
    elif health_percentage >= .5 and health_percentage <= .10:
        healthbar = '█                   '
    elif health_percentage > 0 and health_percentage <= .5:
        healthbar = '▄                   '
    else:
        healthbar = '                    '

    filled_health_bar = (f'HEALTH: |{healthbar}| HP: {current_health}')
    return filled_health_bar
############# STAT BAR

def player_stat_bar(name, player_hp, player_ac, player_race):
    healthbar = health_bar(player_race, player_hp)
    print(f'### Name: {name.capitalize()} | Armor Class: {player_ac} | {healthbar} ###')


############# OPTION BAR
'''
underneath player stats before PUNCH or SWORD prompt.
'''
def option_bar(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions):
    system_methods.clear_console()
    player_stat_bar(name, player_hp, player_ac, player_race)
    print()
    print()
    print('''
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|   |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|   |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|        FIGHT        |   |      INVENTORY      |   |         RUN         |
|_____________________|   |_____________________|   |_____________________|
''')
    print()
    print('                           What do you want to do?')
    print()
    print()
    choice = input('Choice: ') 
    choice = choice.lower()
    while True:
        if choice == 'fight':
            area_one_combat_methods.player_fight_troll(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        elif choice == 'inventory':
            inventory(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        elif choice == 'run':
            run_away(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        else:
            input('Invalid option. Press Enter to try again...')
            option_bar(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)

#FIGHT will take you to the normal screen but the PUNCH or SWORD are customizeable from what's "equipped" in inventory.
#essentially it will be print(f'Do you use your {weapon_inventory[0]} or {weapon_inventory[1]}')

#INVENTORY will trigger the inventory method 

############# RUN METHOD
def run_away(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions):
    system_methods.clear_console()
    player_stat_bar(name, player_hp, player_ac, player_race)
    print()
    print()
    print('You try to run away...')
    run_chance = random.randint(1,4)
    time.sleep(2)
    if run_chance == 1:
        print()
        print('You got away!')
        time.sleep(2)
        area_one_dialogue.run_end()
    else:
        print()
        print('You\'re unable to run away!')
        time.sleep(2)
        option_bar(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)


############# INVENTORY METHOD
    '''
    This only works for one area right now. Need to figure out how to get it to tie into other combat scenarios.
    You could have each battle have a certain parameter associate and fill that in.
    '''

def inventory(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions):
    system_methods.clear_console()
    player_stat_bar(name, player_hp, player_ac, player_race)
    print()
    print('''
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|         Inventory         |
|___________________________|

|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|          WEAPONS          |
|                           |
|          POTIONS          |
|___________________________|

|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|            BACK           |
|___________________________|
''')

    print('   What do you want to do?')
    
    print()
    print()
    choice = input('Choice: ') 
    choice = choice.lower()
    while True:
        if choice == 'weapons':
            weapons_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        elif choice == 'potions':
            potions_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        elif choice == 'back':
            option_bar(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        else:
            input('Invalid option. Press Enter to try again...')
            inventory(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)


########## WEAPONS METHOD

def weapons_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions):
    system_methods.clear_console()
    player_stat_bar(name, player_hp, player_ac, player_race)
    print()
    print()
    print(f'''
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|   SLOT #        ITEM       |
 ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
''')
    count_list(player_weapons)
    print('______________________________')
    print('''
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|   |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|   |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|        EQUIP        |   |        VIEW         |   |        BACK         |
|_____________________|   |_____________________|   |_____________________|
''')
    print()
    print(f'Currently equipped: {player_weapons[0].upper()} and {player_weapons[1].upper()}')
    print()
    print('                           What do you want to do?')
    print()
    print()
    choice = input('Choice: ') 
    choice = choice.lower()
    while True:
        if choice == 'equip':
            equip_menu_one(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        elif choice == 'view':
            item_descriptions.view_weapons_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        elif choice == 'back':
            inventory(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        else:
            input('Invalid option. Press Enter to try again...')
            weapons_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)

############# EQUIP METHOD

###SCREEN 1
def check_number(slot_numbers, equip_or_view):
    print()
    try:
        item = int(input(f"Slot # of item to {equip_or_view}: "))
        if item >= 1 and item <= slot_numbers:
            return item
        else:
            print()
            print(f'That\'s not an item slot. They can be any slot from 1 to {slot_numbers}.')
            print()
            input('Press enter to try again...')
            return check_number(slot_numbers, equip_or_view)
    except ValueError:
            print()
            print(f'That\'s not an item slot. They can be any slot from 1 to {slot_numbers}.')
            print()
            input('Press enter to try again...')
            return check_number(slot_numbers, equip_or_view)

def equip_menu_one(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions):
    system_methods.clear_console()
    player_stat_bar(name, player_hp, player_ac, player_race)
    print()
    print()
    print(f'''
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|   SLOT #        ITEM       |
 ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
''')
    count_list(player_weapons)
    print('______________________________')

    print()
    print(f'Currently equipped: {player_weapons[0].upper()} and {player_weapons[1].upper()}')
    print()
    choice = input(f'Do you want to keep the {player_weapons[0]} in slot# 1? YES or NO: ')
    choice = choice.lower()
    
    if choice == 'yes':
        equip_menu_two(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
    elif choice == 'no':
        pass
    else:
        input('Invalid input. Press Enter to try again...')
        equip_menu_one(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)

    ####CHECKING IF NUMBERS ARE WITHING THE RANGE OF ITEMS IN INVENTORY
    slot_numbers = len(player_weapons)
    item = check_number(slot_numbers, 'equip')
    
    #TURN USER INPUT INTO THE WEAPON IN THE CORRESPONDING SLOT
    item_index = item-1
    item = player_weapons[item_index]
    

    if item == player_weapons[0]:
        print()
        print(f'{item.upper()} already equipped as item 1.')
        print()
        input('Press Enter to try again...')
        equip_menu_one(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
 
    elif item != player_weapons[0] and item == player_weapons[1]:
        print()
        print(f'{player_weapons[1]} already equipped as item 2.')
        print()
        print(f'Do you want to replace {player_weapons[0]} with {item}?')   
        print()
        item_swap_answer = input('YES or NO: ')
        item_swap_answer = item_swap_answer.lower()
        system_methods.clear_console()
        if item_swap_answer == 'yes':
            player_weapons.insert(0, player_weapons.pop(1))
            print()
            print(f'{player_weapons[0].upper()} swapped with {player_weapons[1]}!')
            time.sleep(2)
            print()
            equip_menu_two(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)

        elif item_swap_answer == "no":
            equip_menu_one(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        else:
            print()
            input('Invalid input. Press Enter to try again...')
            equip_menu_one(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
 
    elif item != player_weapons[0] and item != player_weapons[1]:
        player_weapons.insert(0, player_weapons.pop(item_index))
        player_weapons.insert(1, player_weapons.pop(2))
        print()
        print(f'{item.upper()} equipped in slot 1!')
        print()
        input('Press Enter to continue...')
        equip_menu_two(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
 
    else:
        input('Invalid input. Press Enter to try again...')
        equip_menu_one(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)

############## EQUIP MENU 2
def equip_menu_two(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions):
    system_methods.clear_console()
    player_stat_bar(name, player_hp, player_ac, player_race)
    print()
    print()
    print(f'''
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|   SLOT #        ITEM       |
 ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
 ''')
    count_list(player_weapons)
    print('______________________________')


    print()
    print(f'Currently equipped: {player_weapons[0].upper()} and {player_weapons[1].upper()}')
    print()
    choice = input(f'Do you want to keep the {player_weapons[1]} in slot# 2? YES or NO: ')
    choice = choice.lower()
    
    if choice == 'yes':
        weapons_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
    elif choice == 'no':
        pass
    else:
        input('Invalid input. Press Enter to try again...')
        equip_menu_two(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)

    ####CHECKING IF NUMBERS ARE WITHING THE RANGE OF ITEMS IN INVENTORY
    slot_numbers = len(player_weapons)
    item = check_number(slot_numbers, 'equip')
    
    #TURN USER INPUT INTO THE WEAPON IN THE CORRESPONDING SLOT
    item_index = item-1
    item = player_weapons[item_index]
    

    if item == player_weapons[1]:
        print()
        print(f'{item.upper()} already equipped as item 2.')
        print()
        input('Press Enter to try again...')
        equip_menu_one(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
 
    elif item != player_weapons[1] and item == player_weapons[0]:
        print()
        print(f'{player_weapons[0]} already equipped as item 1.')
        print()
        print(f'Do you want to replace {player_weapons[1]} with {item}?')   
        print()
        item_swap_answer = input('YES or NO: ')
        item_swap_answer = item_swap_answer.lower()
        system_methods.clear_console()
        if item_swap_answer == 'yes':
            player_weapons.insert(1, player_weapons.pop(0))
            print()
            print(f'{player_weapons[1].upper()} swapped with {player_weapons[0]}!')
            time.sleep(2)
            print()
            weapons_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)

        elif item_swap_answer == "no":
            equip_menu_two(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        else:
            print()
            input('Invalid input. Press Enter to try again...')
            equip_menu_two(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
 
    elif item != player_weapons[0] and item != player_weapons[1]:
        player_weapons.insert(1, player_weapons.pop(item_index))
        #player_weapons.insert(1, player_weapons.pop(item_index))
        print()
        print(f'{item.upper()} equipped in slot 2!')
        print()
        input('Press Enter to continue...')
        weapons_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
 
    else:
        input('Invalid input. Press Enter to try again...')
        equip_menu_two(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)


############# view METHOD

######## COUNT LIST
def count_list(player_list):
    count = 0
    for item_index in range(len(player_list)):
        print(f'      {count+1}        {player_list[item_index].upper()}')
        print()
        count += 1

###### POTIONS LIST

def potions_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions):
    system_methods.clear_console()
    player_stat_bar(name, player_hp, player_ac, player_race)
    print()
    print()
    print(f'''
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|   SLOT #        ITEM       |
 ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
 ''')
    count_list(player_potions)
    print('______________________________')
    print('''
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|   |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|   |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|         USE         |   |        VIEW         |   |        BACK         |
|_____________________|   |_____________________|   |_____________________|
''')
    print()
    print('                           What do you want to do?')
    print()
    print()
    choice = input('Choice: ') 
    choice = choice.lower()
    while True:
        if choice == 'use':
            print()
            potion_choice = input(str('What potion do you want to use: '))
            potion_choice = potion_choice.lower()
            use_potions(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions, potion_choice)
        elif choice == 'view':
            potion_descriptions.view_potions_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        elif choice == 'back':
            inventory(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        else:
            input('Invalid option. Press Enter to try again...')
            potions_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)

def use_potions(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions, potion_choice):
    player_max_health = race_hp_for_health(player_race)
    
    if potion_choice == 'potion of health':
        if 'POTION OF HEALTH' not in player_potions:
            system_methods.clear_console()
            print('You dont have any potions of health in your inventory.')
            time.sleep(3)
            potions_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        else: 
            pass

        if player_hp == player_max_health:
            system_methods.clear_console()
            print('You\'re already at full health!')
            time.sleep(2)
            potions_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        else:
            player_hp += 10

        if player_hp > player_max_health:
            player_hp = player_max_health
            print()
            print('You feel invigorated as the potion touches your lips!')
            player_potions.remove('POTION OF HEALTH')
            time.sleep(2)
            potions_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        else:       
            print()
            print('You feel invigorated as the potion touches your lips!')
            player_potions.remove('POTION OF HEALTH')
            time.sleep(2)
            potions_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
    else:
        system_methods.clear_console()
        print('That\'s not a potion you have in inventory.')
        print()
        input('Press Enter to go back...')
        potions_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)

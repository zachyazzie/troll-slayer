'''
This is a file containing the images and descriptions for each potion
'''
import system_methods
import game_mechanics_methods

'''
      _____
     `.___,'
      (___)
      <   >
       ) (
      /`-.\\
     /     \\
    / _    _\\
   :,' `-.' `:
   |         |
   :         ;
    \       /
     `.___.' 

'''

def health():
    print('''
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|                                                                        |
|                                _  _ ___   _   _  _____ _  _            |
|                               | || | __| /_\ | ||_   _| || |           |
|         _____                 | __ | _| / _ \| |__| | | __ |           |
|        `.___,'                |_||_|___/_/ \_\____|_| |_||_|           |
|         (___)                                                          |
|         <   >                                                          |
|          ) (             DESCRIPTION: A small bottle with an           |
|         /`-.\\            encouraging red liquid inside. The smell      |
|        /     \\           of the liquid alone feels invigorating.       |
|       / _    _\\                                                        |
|      :,' `-.' `:         USE: Heal up to 10hp                          |
|      |         |                                                       |
|      :         ;                                                       |
|       \       /                                                        |
|        `.___.'                                                         |
|                                                                        |
|________________________________________________________________________|

|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|   |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|         USE         |   |        BACK         |
|_____________________|   |_____________________|
''')

def view_potions_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions):
    system_methods.clear_console()
    game_mechanics_methods.player_stat_bar(name, player_hp, player_ac, player_race)
    print()
    print()
    print(f'''
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|   SLOT #        ITEM       |
|____________________________|       
 ''')
    game_mechanics_methods.count_list(player_potions)
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
            game_mechanics_methods.potions_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        elif choice == 'view item':
            break
        else:
            input('Invalid input. Press Enter to try again...')
            view_potions_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)

    while True:
        print()
        choice = input(str('Name of item to view: '))
        choice = choice.lower()
        if choice == 'potion of health':
            system_methods.clear_console()
            game_mechanics_methods.player_stat_bar(name, player_hp, player_ac, player_race)
            print()
            print()
            health()
            while True:
                print()
                choice = input(str('Choice: '))
                choice = choice.lower()
                if choice == 'use':
                    potion_choice = 'potion of health'
                    game_mechanics_methods.use_potions(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions, potion_choice)
                elif choice == 'back':
                    view_potions_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
                else:
                    print()
                    input('Invalid input. Press Enter to try again...')
        
        else:
            input('Invalid input. Press Enter to try again...')
            view_potions_menu(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
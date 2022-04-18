'''
This file controls the combat in area one
'''
import time
import textwrap as tw
import inspect
import random
import attack_methods
import system_methods
import game_mechanics_methods
import area_one_dialogue

def troll_fight(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions):
    #Troll has 44hp | AC 15 | Attack(claw) roll 2d6+2 | Attack(bite) 1d6+4
    #This fight will go until the troll has 1/2 health or the player dies. Once the troll has half health, Durnan will come out of the back and use the sword over the bar to finish the job.
    system_methods.clear_console()
    system_methods.delay_print('The troll gives out a hideous roar and begins to lumber toward you!')
    print()
    print()
    input('Press Enter to continue...')
    player_fight_troll_options(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)  
            
def troll_fight_player(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions):
    while True:
       
        if troll_hp >= 22:  
            system_methods.clear_console()
            game_mechanics_methods.player_stat_bar(name, player_hp, player_ac, player_race)
            print()
            print()
            system_methods.delay_print('The troll gets ready for another attack!')
            time.sleep(2)
            print()
            print()
            troll_choice = random.randint(1,2)
            if troll_choice == 1:
                attack_methods.creature_claw_options('troll')
                attack_attempt = attack_methods.attack(6, player_ac)
                if attack_attempt:
                    p44 = inspect.cleandoc("The troll's claws sink into your skin and you feel terrible burning from the probably infected claws!")
                    system_methods.delay_print(tw.fill(p44, width=75))
                    print()
                    print()
                    damage = attack_methods.weapon_damage(12, 5)
                    system_methods.delay_print(f'You take {damage} points of damage!')
                    player_hp -= damage
                    print()
                    print()
                    input('Press Enter to continue...')
                    player_fight_troll_options(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
                else:
                    system_methods.delay_print('You narrowly dodge the large troll\'s hand and ready yourself!')
                    print()
                    print()
                    input('Press Enter to continue...')
                    player_fight_troll_options(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
    
            elif troll_choice == 2:
                attack_methods.creature_bite_options('troll')
                attack_attempt = attack_methods.attack(4, player_ac)
                if attack_attempt:
                    system_methods.delay_print('The terrible teeth rip into your flesh and you let out a large yell in pain!')
                    print()
                    print()
                    damage = attack_methods.weapon_damage(8, 3) 
                    system_methods.delay_print(f'You take {damage} points of damage!')
                    player_hp -= damage
                    print()
                    print()
                    input('Press Enter to continue...')
                    player_fight_troll_options(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
                else:
                    system_methods.delay_print('You slip past the trolls jaws and back away, ready to go again!')
                    print()
                    print()
                    input('Press Enter to continue...')
                    player_fight_troll_options(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        else:
            area_one_dialogue.end_area_one_boss(player_hp, player_race)
    

def player_fight_troll(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions): 
    system_methods.clear_console()
    if name == 'saitama':
        healthbar = game_mechanics_methods.health_bar(player_race, player_hp)
        print(f'### Name: {name.capitalize()} | Armor Class: {player_ac} | {healthbar} ###')
        print()
        print() 
        print(f'Do you use your {player_weapons[0]} or {player_weapons[1]}?')
        print()
        user_attack = input('Choice: ')
        user_attack = user_attack.lower()
        print()
        if user_attack == 'fist': 
            system_methods.delay_print('You cock your fist and land one solid punch in the middle of the Troll\'s gut')
            print() 
            print()
            system_methods.delay_print(f'You dealt 1,000,000 points of damage!')
            print()
            print()
            input('Press Enter to continue...')
            area_one_dialogue.saitama_troll_end(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        else:
                system_methods.clear_console()
                print(f'### Name: {name.capitalize()} | Hit Points: {player_hp} | Armor Class: {player_ac} ###')
                print()
                print()
                print('Invalid input. Try again.')
                print()
                input('Press Enter to try again...')    

    else:
        healthbar = game_mechanics_methods.health_bar(player_race, player_hp)
        print(f'### Name: {name.capitalize()} | Armor Class: {player_ac} | {healthbar} ###')
        print()
        print() 
        print(f'Do you use your {player_weapons[0]} or {player_weapons[1]}?')
        print()
        user_attack = input('Choice: ')
        user_attack = user_attack.lower()
        print()
        if user_attack == 'fist':
            attack_methods.player_creature_punch_options('troll')
            attack_attempt = attack_methods.attack(4, troll_ac) 
            if attack_attempt:
                system_methods.delay_print('You land the hit and troll recoils with a loud yell!')
                print()
                print()
                damage = attack_methods.weapon_damage(6, 0)
                system_methods.delay_print(f'You dealt {damage} points of damage!')
                troll_hp -= damage
                print()
                print()
                input('Press Enter to continue...')
                troll_fight_player(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
            else:
                system_methods.delay_print('The troll dodges the attack and you\'re right up next to it!')
                print()
                print()
                input('Press Enter to continue...')
                troll_fight_player(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
    
        elif user_attack == 'longsword':
            attack_methods.player_creature_sword_options('troll')
            attack_attempt = attack_methods.attack(8, troll_ac)
            if attack_attempt:
                p45 = inspect.cleandoc('You land the hit and troll howls in pain as the sword opens up a black oozy wound!')
                system_methods.delay_print(tw.fill(p45, width=75))
                print()
                print()
                damage = attack_methods.weapon_damage(8, 4)
                system_methods.delay_print(f'You dealt {damage} points of damage!')
                troll_hp -= damage
                print()
                print()
                input('Press Enter to continue...')
                troll_fight_player(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
            else:
                system_methods.delay_print('The troll dodges the attack and you\'re right up next to it!')
                print()
                print()
                input('Press Enter to continue...')
                troll_fight_player(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)

        elif user_attack == 'battleaxe':
            attack_methods.player_creature_battleaxe_options('troll')
            attack_attempt = attack_methods.attack(8, troll_ac)
            if attack_attempt:
                p45 = inspect.cleandoc('The troll recoils and roars in pain as the axe rips into its flesh!')
                system_methods.delay_print(tw.fill(p45, width=75))
                print()
                print()
                damage = attack_methods.weapon_damage(12, 2)
                system_methods.delay_print(f'You dealt {damage} points of damage!')
                troll_hp -= damage
                print()
                print()
                input('Press Enter to continue...')
                troll_fight_player(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
            else:
                system_methods.delay_print('The troll dodges the attack and you\'re right up next to it!')
                print()
                print()
                input('Press Enter to continue...')
                troll_fight_player(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        elif user_attack == 'nasty knife':
            attack_methods.player_creature_knife_options('troll')
            attack_attempt = attack_methods.attack(6, troll_ac)
            if attack_attempt:
                p45 = inspect.cleandoc('The troll recoils and roars in pain as the knife slices into its flesh!')
                system_methods.delay_print(tw.fill(p45, width=75))
                print()
                print()
                damage = attack_methods.weapon_damage(4, 2)
                system_methods.delay_print(f'You dealt {damage} points of damage!')
                troll_hp -= damage
                print()
                print()
                input('Press Enter to continue...')
                troll_fight_player(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
            else:
                system_methods.delay_print('The troll dodges the attack and you\'re right up next to it!')
                print()
                print()
                input('Press Enter to continue...')
                troll_fight_player(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
        else:
            system_methods.clear_console()
            print(f'### Name: {name.capitalize()} | Hit Points: {player_hp} | Armor Class: {player_ac} ###')
            print()
            print()
            print('Invalid input. Try again.')
            print()
            input('Press Enter to try again...')     

def player_fight_troll_options(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions):
    while True:   
        if player_hp <=0:
            system_methods.clear_console()
            game_mechanics_methods.you_died('Troll')
        else:
            system_methods.clear_console()
            healthbar = game_mechanics_methods.health_bar(player_race, player_hp)
            print(f'### Name: {name.capitalize()} | Armor Class: {player_ac} | {healthbar} ###')
            print()
            print()
            game_mechanics_methods.option_bar(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions)
            
  
    


"""
This file contains all the methods for attacks
"""
import random
import time

######### ATTACK OPTIONS

def player_creature_sword_options(enemy_type):
    user_sword = [f'You swipe at the {enemy_type} with your sword across the chest!',f'You try to get behind the {enemy_type} and stab it in the back!',
    f'You swing at the {enemy_type}\'s arms trying to cut anything you can touch!']
    attack_option_number = random.randint(0,2)
    print(user_sword[attack_option_number])
    time.sleep(2)
    print()

def player_creature_punch_options(enemy_type):
    user_punch = [f'You run behind the {enemy_type} and take a swing with your fist!',f'You run headfirst at the {enemy_type} and try to gut punch it!',
    f'You jump toward the {enemy_type} and try to elbow the creature!']
    attack_option_number = random.randint(0,2)
    print(user_punch[attack_option_number])
    time.sleep(2)
    print()

def player_creature_battleaxe_options(enemy_type):
    user_punch = [f'You run behind the {enemy_type} and take a swing with your might axe!',f'You let out a battlecry and run headfirst at the {enemy_type} with your axe!',
    f'You jump toward the {enemy_type} with your axe overhead and swing down!']
    attack_option_number = random.randint(0,2)
    print(user_punch[attack_option_number])
    time.sleep(2)
    print()

def player_creature_knife_options(enemy_type):
    user_punch = [f'You run behind the {enemy_type} and try to stab it in the back!',f'You hide in the shadows and jump out at the {enemy_type} with the knife in hand!',
    f'You jump toward the {enemy_type} with the knife and swipe frantically at it.']
    attack_option_number = random.randint(0,2)
    print(user_punch[attack_option_number])
    time.sleep(2)
    print()

def creature_claw_options(enemy_type):
    creature_claw = [f'The {enemy_type} take a swipe at you with its long figers!',f'The {enemy_type} grabs at you with their claws!',
    f'The {enemy_type} uses both hands and tries to grab you!']
    attack_option_number = random.randint(0,2)
    print(creature_claw[attack_option_number])
    time.sleep(2)
    print()

def creature_bite_options(enemy_type):
    creature_bite = [f'The {enemy_type} lunges at you with its jaws to take a bite!',f'The {enemy_type} ducks to your level and attempts to grab and take a bite out of you!',
    f'The {enemy_type} opens up its large mouth and runs toward you!']
    attack_option_number = random.randint(0,2)
    print(creature_bite[attack_option_number])
    time.sleep(2)
    print()

######### DAMAGE OUTCOMES
def attack(roll_modifier, target_ac):
    '''
    Pulls in the weapon roll modifier. 1d4, 1d6, 1d8, 1d10, 1d12, etc. and the armor class of the enemy.
    '''
    d20_roll = random.randint(1,20) + roll_modifier
    if d20_roll >= target_ac:
        return True
    else:
        return False

def weapon_damage(weapon_dice, weapon_plus):
    '''
    Pulls in the weapon. 1d4, 1d6, 1d8, 1d10, 1d12, etc and then adds the modifier.
    '''
    return random.randint(1, weapon_dice) + weapon_plus


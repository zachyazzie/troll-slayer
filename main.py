import system_methods
import assets
import game_mechanics_methods
import area_one_dialogue

##################################################### MAIN
def main():
    assets.title_image()
    print()

    game_mechanics_methods.game_instructions()
    system_methods.clear_console()
    player_name = game_mechanics_methods.name_check()
    print()
    player_race = game_mechanics_methods.race_check()
    player_hp, player_ac, player_weapons, player_potions = game_mechanics_methods.race_stats(player_race)
    player_gold = 25
    print()
    print(f'### Name: {player_name.capitalize()} | Race: {player_race.capitalize()} | Hit Points: {player_hp} | Armor Class: {player_ac} ###')
    print()
    print()
    system_methods.delay_print("Press Enter to begin...")
    input()
    print()
    system_methods.clear_console()
    area_one_dialogue.main_dialogue(player_name, player_race, player_hp, player_ac, player_gold, player_weapons, player_potions)
if __name__ == "__main__":
    main()


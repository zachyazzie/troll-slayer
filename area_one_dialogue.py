'''
This contains all dialog scenarios contained in functions
'''
import time
import textwrap as tw
import inspect
import system_methods
import assets
import game_mechanics_methods
import area_one_combat_methods

def main_dialogue(player_name, player_race, player_hp, player_ac, player_gold, player_weapons, player_potions):
    p1 = inspect.cleandoc("""You find yourself sitting at a lone table in the corner of your favorite tavern, The Yawning Portal. The smell of ale and a warm meal are in the air. The 
    tavern is full of people from all the surrounding area, this is the hub of adventure after all. The open area is three stories tall with tables filled all 
    the way to the top. There is singing, chatting, music, and secrecy in every corner. And on the bottom floor, in the middle of the room lies a large dark 
    pit. The real Yawning Portal. Adventurers have been know to go down from time to time in search of treasure. Few return. And most that do return with madness in their eyes. 
    No one truly knows what lies beneath the ground here.""")
    system_methods.delay_print(tw.fill(p1, width=75))
    print()
    print()
    p2 = inspect.cleandoc(f"""You hear the barkeep, Durnan, yell at a table of halflings who seem to be getting a bit too excited, "Hey! You lot! Get off that table or I'm throwin' you out!" 
    Durnan is a burly man with an unmatched mustache. It's been said he fought off a wyrmling dragon all on his own with his fabled sword Storm-Weaver, which now 
    hangs over the bar as more of a decoration than anything. He carries four pints in each hand to a long table of dwarves next to you and then turns to you and 
    asks, "What will it be {player_race}? ...Quickly now!""")
    system_methods.delay_print(tw.fill(p2, width=75))
    print()
    print()
    
    while True:
        system_methods.delay_print('FOOD, DRINK, BOTH, or NOTHING?')
        print()
        print()
        food_response = input("Choice: ")
        food_response = food_response.lower()   ##food is 5, drink is 2, both is 7.
        system_methods.clear_console()
        if food_response == 'food' or food_response == 'drink' or food_response == 'both':
            system_methods.delay_print("Durnan nods and says, 'Very well. Back in a minute.'")
            print()
            print()
            break
                ###store in a variable True if food was ordered
        elif food_response == "nothing":
            p3 = inspect.cleandoc("""Durnan says gruffly, "If you're not going to order anything, you're wasting good space in my tavern. Keep your business quick and get out." He turns back 
            and heads toward the kitchen no longer paying any attention to you.""")
            system_methods.delay_print(tw.fill(p3, width=75))
            print()
            print()
            break
                ###store in a variable False if food wasn't ordered
        else:
            print("Not a valid input. Try again")
            print()
            input('Press Enter to try again...')
            system_methods.clear_console()
            
    p4 = inspect.cleandoc(f"""While you sit at your table, you hear an angry voice call at you from across the room. "You! You filthy {player_race} trash!" A large half-orc woman is storming toward 
    you! She is wearing heavy leather armor and has a hand-axe at her side. One of the sharp lower teeth shooting out above her lip is cracked. She has white war 
    paint across her face in a menacing pattern. She grabs you and lifts you by the collar to stand up. Standing at about 6'7" she's a pretty good height taller than 
    you. She snarls and says, "You still owe me 100 gold from that job you botched and left us to take the fall! I still have two guys locked up!""")
    system_methods.delay_print(tw.fill(p4, width=75))
    print()
    print()

    
    while True:
        system_methods.delay_print('Do you TALK or FIGHT?')
        print()
        print()
        yagra_response_1 = input("Choice: ")
        yagra_response_1 = yagra_response_1.lower()
        print()
        system_methods.clear_console()
        if yagra_response_1 == 'talk':
            p5 = inspect.cleandoc("""You say, Woah Yagra! The job that I botched?! You and your heavy-footed thugs are the ones that tripped that alarm! I was just smart enough to leave before anything 
            too dicey went down! It's not my fault that you all don't know the meaning of stealth. You smirk a bit and push yourself out of her grasp.""")
            system_methods.delay_print(tw.fill(p5, width=75))
            print()
            print()
            p6 = inspect.cleandoc("""Yeah? Yagra replies. Then how come the guards just so happened to be on that block at the right time? It's almost like they knew something was going down in the 
            area so that you could sneak away at the last minute and let us take the fall! You've always been a snake! Now give me the 100 gold and I'll only rough you up a bit.""")
            system_methods.delay_print(tw.fill(p6, width=75))
            print()
            print()
            
            while True:
                system_methods.delay_print('Do you GIVE the gold or REFUSE?')
                print()
                print()
                yagra_response_2 = input("Choice: ")
                yagra_response_2 = yagra_response_2.lower()
                system_methods.clear_console()

                if yagra_response_2 == 'give':
                    p7 = inspect.cleandoc("""You say, Alright alright! Here you go. You take a hefty pouch out of your jacket pocket and had it to Yagra. She opens it, smirks, then says, "Smart choice. Don't 
                    let it happen again.: At that moment, you feel a glass break across the back of your head. Your vision goes dizzy for a moment and you fall to the ground. You hear deep chuckling and footseps walking around you. 
                    As you gain your composure and vision you see one of Yagra's orc thugs walking off with her.""")          
                    player_hp -= 1
                    system_methods.delay_print(tw.fill(p7, width=75))
                    print()
                    print()

                    while True:
                        system_methods.delay_print('Do you get up and FIGHT or SIT back down?')
                        print()
                        print()
                        yagra_response_3 = input("Choice: ")
                        yagra_response_3 = yagra_response_3.lower()
                        system_methods.clear_console()
                        
                        if yagra_response_3 == "fight":
                            p18 = inspect.cleandoc("""You get up off the floor and say, \"That's it Yagra!! I've had it up to here with you!\" You run up to her thug on her right and punch him across the face. He loses his balance 
                            and tumbles down the pit in the middle of the room. The music and chatter in the room come to a halt and audible gasps can be heard for a moment.""")
                            system_methods.delay_print(tw.fill(p18, width=75))
                            print()
                            print()
                            input('Press Enter to continue...')
                            troll_fight_choice(player_name, player_hp, player_ac, player_race, player_weapons, player_potions)
                           
                        elif yagra_response_3 == "sit":
                            p9 = inspect.cleandoc("""You get off the floor, brush the glass pieces off your head and sit back in your chair. After a few minutes Durnan comes back out and comes over to you. 
                            "Geez kid!" He says. "Looks like you could use that ale now. Should I run and grab you one?""")
                            system_methods.delay_print(tw.fill(p9, width=75))
                            print()
                            print()

                            durnan_post_orc_fight(player_gold)

                        else:
                            print('Invalid input. Try again.')
                            print()
                            input('Press Enter to try again...')
                            system_methods.clear_console()            
                elif yagra_response_2 == 'refuse':
                    if player_name == 'saitama':
                        p51 = inspect.cleandoc(f'''"You know... I really don't want to do that." You say. Yagra replies, "I don't care what you want!" She then winds up for another punch and just before
                        she can connect, with lightning speed you hit her across the face and she launches up in the air and falls down into the pit. "Man... these bad guys need to get tougher..." You think to yourself, almost bored.
                        You turn around and see one of Yagra's thugs look at you terrified. He runs away through the crowd out of the tavern and the place erupts in cheers!''')
                        system_methods.delay_print(tw.fill(p51, width=75))
                        print()
                        print()
                        input('Press Enter to continue...')
                        troll_fight_choice(player_name, player_hp, player_ac, player_race, player_weapons, player_potions)
                    else:
                        p17 = inspect.cleandoc(f"""\"You know, Yagra..\" You say cockily. \"I don't think I will.\" You shove her off of you and she lets go of your coat. She gives a nod to someone behind you and before 
                        you can see who it is you feel a glass shatter across your head. Your vision goes dizzy for a moment and you hear deep chuckling as you fall to the ground. You feel 
                        someone going through your pockets and then you hear it. The jingling of your pouch of coins being lifted from your pocket. \"Thanks again, {player_name.capitalize()}. Don't call us for 
                        help next time.\" Out of the corner of your eye you see Yagra walking away with one of her orc thugs.""")
                        system_methods.delay_print(tw.fill(p17, width=75))
                        player_hp -= 1 #subtract 1hp
                        print()
                        print()

                    while True:
                        system_methods.delay_print('Do you get up and FIGHT or SIT back down?')
                        print()
                        yagra_response_4 = input("Choice: ")
                        yagra_response_4 = yagra_response_4.lower()
                        system_methods.clear_console()
            
                        if yagra_response_4 == "fight":
                            p18 = inspect.cleandoc("""You get up off the floor and say, \"That's it Yagra!! I've had it up to here with you!\" You run up to her thug on her right and punch him across the face. He loses his balance 
                            and tumbles down the pit in the middle of the room. The music and chatter in the room come to a halt and audible gasps can be heard for a moment.""")
                            system_methods.delay_print(tw.fill(p18, width=75))
                            print()
                            print()
                            input('Press Enter to continue...')
                            pick_up_knife(player_name, player_hp, player_ac, player_race, player_weapons, player_potions)
                            #move down to the fight
                        elif yagra_response_4 == 'sit':
                            p19 = inspect.cleandoc("""You get off the floor, brush the glass pieces off your head and sit back in your chair. After a few minutes Durnan comes back out and comes over to you.""")
                            system_methods.delay_print(tw.fill(p19, width=75))
                            print()
                            print()
                            p20 = inspect.cleandoc("""\"Geez kid!\" He says. \"Looks like you could use that ale now.\"""")
                            system_methods.delay_print(tw.fill(p20, width=75))
                            print()
                            print()

                            durnan_post_orc_fight(player_gold)

                        else:
                            print('Invalid input. Try again.')
                            print()
                            input('Press Enter to try again...')
                            system_methods.clear_console()
                else:
                    print('Invalid input. Try again.')
                    print()
                    input('Press Enter to try again...')
                    system_methods.clear_console()
            break
        elif yagra_response_1 =='fight':
            if player_name == 'saitama':
                p52 = inspect.cleandoc("""You push Yagra off of you with ease and she snarls with anger. She rushes at you and then winds up for another punch. Just before
                        she can connect, with lightning speed you hit her across the face and she launches up in the air and falls down into the pit. "Man... these bad guys need to get tougher..." You think to yourself, almost bored.
                        You turn around and see one of Yagra's thugs look at you terrified. He runs away through the crowd out of the tavern and the place erupts in cheers!""")
                system_methods.delay_print(tw.fill(p52, width=75))
                print()
                print()
                input('Press Enter to continue...')
                troll_fight_choice(player_name, player_hp, player_ac, player_race, player_weapons, player_potions)
            else:
                p27 = inspect.cleandoc("""You immediately shove Yagra off of you and punch her across the face. She snarls and looks over your shoulder and nods. A large orc thug lunges at you and you begin to trade 
                blows. The area clears and people begin cheering for the fight! Yagra backs off to watch her backup take you on. \"Get him Goregutt! Make him pay!\" Yagra yells.""")
                system_methods.delay_print(tw.fill(p27, width=75))
                print()
                print()
                p28 = inspect.cleandoc("""After a few equal hits, the fight gets uncomfortably close the the pit in the middle of the room. With one final left hook across the orcs jaw, you launch him into the pit 
                where he falls into the darkness.""")
                system_methods.delay_print(tw.fill(p28, width=75))
                print()
                print()
                input("Press Enter to continue...")
                system_methods.clear_console()
                print("CRASH!")
                print()
                p29 = inspect.cleandoc("""The orc's body slams to the ground at the bottom of the dark pit and then silence in the tavern.""")
                system_methods.delay_print(tw.fill(p29, width=75))
                print()
                print()
                p30 = inspect.cleandoc("""The place erupts with applause and cheering after being so entertained by the brawl. """)
                system_methods.delay_print(tw.fill(p30, width=75))
                print()
                print()
                ##Move to FIGHT TIME
                input("Press Enter to continue...")
                pick_up_knife(player_name, player_hp, player_ac, player_race, player_weapons, player_potions)
                
        else:
            print('Invalid input. Try again.')
            print()
            input('Press Enter to try again...')
            system_methods.clear_console()

########## CHOOSE TO FIGHT TROLL OR NOT
def troll_fight_choice(name, player_hp, player_ac, player_race, player_weapons, player_potions):
    system_methods.clear_console()
    system_methods.delay_print("Suddenly, you hear a faint 'Thud... Thud... Thud...'")
    ##wait 2 seconds
    time.sleep(2)
    system_methods.clear_console()
    system_methods.delay_print("You hear another louder 'Thud... Thud... Thud...'")
    ##wait 2 seconds
    time.sleep(2)
    system_methods.clear_console()
    system_methods.delay_print("Finally, there comes an even louder and closer 'Thud! Thud!")
    time.sleep(2)
    system_methods.clear_console()
    system_methods.delay_print("And then... silence.")
    print()
    print()
    input('Press Enter to continue...')
    system_methods.clear_console()
    assets.troll_image()
    p31 = inspect.cleandoc("""A large scaly grey hand grabs the edge of the floor from inside the pit and begins to pull up a large hulking body. Shouts of alarm suddenly ring out as a hulking creature 
    climbs up out of the shaft in the middle of the taproom — a monster with warty green skin, a tangled nest of wiry black hair, a long, carrot-shaped nose, and bloodshot eyes. 
    As it bares its yellow teeth and howls, you recoil from the foul stench of his breath. Everyone in the tavern reacts in fear except for the barkeep, Durnan, who shouts, \"Troll!\"""")
    system_methods.delay_print(tw.fill(p31, width=75))
    print()
    print()
    system_methods.delay_print("Being that you're the closest he uses his large hand to take a swipe at you!")
    print()
    print()
    input("Press Enter to continue...")
    system_methods.clear_console()
    ##wait 2 seconds

    while True:
        system_methods.delay_print("You narrowly dodge the swipe! Do you RUN away or FIGHT the troll?")
        print()
        print()
        troll_response_1 = input("Choice: ")
        troll_response_1 = troll_response_1.lower()
        system_methods.clear_console()
        if troll_response_1 == 'run':
            p32 = inspect.cleandoc("""You run out of the tavern having forgotten the business that you previously had there. You can hear the screams of the individuals inside the tavern followed by large blasts 
            and clanking metal you assume are spells and swords flying around the room.""")
            system_methods.delay_print(tw.fill(p32, width=75))
            print()
            print()
            time.sleep(2)
            p33 = inspect.cleandoc("""Anyhow, that's no longer your concern. You gain your composure and look up at the noonday sky in 
            the city of Waterdeep. The smell of salty sea air sitting in your nostrils calms you down and you head toward the docks, ready to leave this trouble behind.""")
            system_methods.delay_print(tw.fill(p33, width=75))
            print()
            print()
            print('To be continued...')
            time.sleep(3)
            game_mechanics_methods.play_again()
            #end
        elif troll_response_1 == 'fight':
            area_one_combat_methods.troll_fight(name, player_hp, player_ac, 15, 44, player_race, player_weapons, player_potions)
        else:
            print('Invalid input. Try again.')
            print()
            input('Press Enter to try again...')
            system_methods.clear_console()

############### DURNAN POST-FIGHT WITH YAGRA
def durnan_post_orc_fight(player_gold):
    while True:
        system_methods.delay_print('Do you ACCEPT or DECLINE?')
        print()
        print()
        durnan_response_2 = input("Choice: ")
        durnan_response_2 = durnan_response_2.lower()
        system_methods.clear_console()

        if durnan_response_2 == 'accept':
            p21 = inspect.cleandoc("""You say, \"Sounds good. Thanks.\" You close your eyes, sit back and listen to the sound of the irreverent tavern as your rub the goose-egg on the back of your head. You hear laughing and 
            mugs clanking all around you.""")
            system_methods.delay_print(tw.fill(p21, width=75))
            print()
            print()
            p22 = inspect.cleandoc("""An old man in a grey cloak at a nearby table comes over to you and says, \"You showed real restraint back there. If I were a younger man I 
            would have given her a real fight. We need more people like you.\"""")
            system_methods.delay_print(tw.fill(p22, width=75))
            print() 
            print()
            p23 = inspect.cleandoc("""\"Thanks.\" You say gruffly. And return to closing your eyes trying to ignore the man.""")
            system_methods.delay_print(tw.fill(p23, width=75))
            print()
            print()
            p24 = inspect.cleandoc("""\"You know...\" He says. \"I'm needing someone of your temperment to help me with a que- I mean job. Would you be interested? The pay is more than 
            you've probably had before.\"""")
            system_methods.delay_print(tw.fill(p24, width=75))
            print()
            print()
            old_man_request(player_gold) 
            break
        elif durnan_response_2 == 'decline':
            p39 = inspect.cleandoc("""Durnan says, \"Fine. It's time you be leaving my tavern now. You're taking up valuable seating. On top of that I hear you're bringing in trouble into 
            my establisment\" He escorts you to the door and gives you a little push out the door. \"Come back when you're ready to pay for some service.\"""")
            system_methods.delay_print(tw.fill(p39, width=75))
            print()
            print()
            p40 = inspect.cleandoc("""The warm sun in the city of Waterdeep outside feels great and you have the smell of the salty sea nearby in your nostrils. Although a little peeved, 
            you head toward your home at the docks to plan your next adventure.""")
            system_methods.delay_print(tw.fill(p40, width=75))
            game_mechanics_methods.play_again()             
        else:
            print('Invalid input. Try again.')
            print()
            input('Press Enter to try again...')
            system_methods.clear_console()

########## OLD MAN ASKING FOR HELP
def old_man_request(player_gold):
    while True:
        system_methods.delay_print('Do you ACCEPT or DECLINE?')
        print()
        print()
        old_man_response = input("Choice: ")
        old_man_response = old_man_response.lower()
        system_methods.clear_console()

        if old_man_response == 'accept':
            system_methods.delay_print("\"How much profit are we talking?\" You say.")
            print()
            print()
            system_methods.delay_print("\"A large cut of 10,000 gold.\" The man replies.")
            print()
            print()
            system_methods.delay_print("You think about it for a moment..")
            print()
            print()
            time.sleep(2)    ##wait 5 seconds
            system_methods.delay_print("\"Alright.\" You say confidently.")
            print()
            print()
            time.sleep(1)        ##wait 2 seconds
            system_methods.delay_print("I'm in.")
            print()
            print()
            system_methods.delay_print('To be continued...')
            time.sleep(3)
            print()
            game_mechanics_methods.play_again()
            #end
        elif old_man_response == "decline":
            p13 = inspect.cleandoc("""You say, \"Get out of my face old man. All I want is my drink and to get out of here.\" You wave off the man and he returns to his table dismayed. Durnan 
            returns a few minutes later with your drink and requests 2 gold. You hand over the gold and take the drink.""")
            player_gold -= 2       #subtract two gold
            system_methods.delay_print(tw.fill(p13, width=75))
            print()
            print()
            p14 = inspect.cleandoc("""After you finish the drink, you take a deep breath, get up and leave the tavern. The warm sun in the city of Waterdeep outside feels great and you have the 
            smell of the salty sea nearby in your nostrils. You head toward your home at the docks to plan your next adventure.""")
            system_methods.delay_print(tw.fill(p14, width=75))
            print()
            print()
            system_methods.delay_print('To be continued...')
            time.sleep(3)
            print()
            print()
            game_mechanics_methods.play_again()
            #end
        else:
            print('Invalid input. Try again.')
            print()
            input('Press Enter to try again...')
            system_methods.clear_console()

def end_area_one_boss(current_health, player_race):

    player_max_health = game_mechanics_methods.race_hp_for_health(player_race)

    if current_health == player_max_health:
        ## FILLER
        player_gold = 25
        system_methods.clear_console()
        p34 = inspect.cleandoc("""Suddenly! Durnan rips Storm-Weaver from off the bar and 
        yells, \"Come here you filthy creature!\" And he lunges at the beast and begins to contend with it! It's apparent 
        this isn't his first brawl with the monsters of the deep. You fall to your knees exhausted and watch in amazement as Durnan makes light work of the troll. With 
        one final blow, the troll goes stiff on the end of Durnan's sword and slowly collapses over itself and falls sideways back into the pit.""")
        system_methods.delay_print(tw.fill(p34, width=75))
        print()
        print()
        input("Press Enter to continue...")
        system_methods.clear_console()
        system_methods.delay_print("THUD! The troll's body crashes to bottom of the dark pit.")
        print()
        print()
        p35 = inspect.cleandoc("""Durnan spits in the pit and yells, \"And stay out you beasts of the abyss!\" He comes to you and picks you up. \"Come on! Let's get you a drink!\" He sits you at the bar 
        and gives you a mug of ale. \"On the house, adventurer.\" He says warmly and returns to his other duties, carrying on as if nothing had happened.""")
        system_methods.delay_print(tw.fill(p35, width=75))
        print()
        print()
        input('Press Enter to continue...')
        system_methods.clear_console()
        p36 = inspect.cleandoc("""After about ten minutes you feel a tap on your shoulder and you turn to see an old man in a cloak staring at you with large eyes behind spectacles. \"Greeting brave adventurer!\" He says. \"I saw your display 
        of bravery and I have a proposition for you! I'm in need of help for a que- I mean job. A big one. One that'll pay more than you can fathom. What say you?\"""")
        system_methods.delay_print(tw.fill(p36, width=75))
        print()
        print()
        old_man_request(player_gold)

    else:
        ## FILLER
        player_gold = 25
        system_methods.clear_console()
        p34 = inspect.cleandoc("""Suddenly! As your wounds bleed more profusely and the pain becomes almost unbearable... Durnan rips Storm-Weaver from off the bar and 
        yells, \"Come here you filthy creature!\" And he lunges at the beast and begins to contend with it! It's apparent 
        this isn't his first brawl with the monsters of the deep. You fall to your knees exhausted and watch in amazement as Durnan makes light work of the troll. With 
        one final blow, the troll goes stiff on the end of Durnan's sword and slowly collapses over itself and falls sideways back into the pit.""")
        system_methods.delay_print(tw.fill(p34, width=75))
        print()
        print()
        input("Press Enter to continue...")
        system_methods.clear_console()
        system_methods.delay_print("THUD! The troll's body crashes to bottom of the dark pit.")
        print()
        print()
        p35 = inspect.cleandoc("""Durnan spits in the pit and yells, \"And stay out you beasts of the abyss!\" He comes to you and picks you up. \"Come on! Let's get you a drink!\" He sits you at the bar 
        and gives you a mug of ale. \"On the house, adventurer.\" He says warmly and returns to his other duties, carrying on as if nothing had happened.""")
        system_methods.delay_print(tw.fill(p35, width=75))
        print()
        print()
        input('Press Enter to continue...')
        system_methods.clear_console()
        p36 = inspect.cleandoc("""After about ten minutes you feel a tap on your shoulder and you turn to see an old man in a cloak staring at you with large eyes behind spectacles. \"Greeting brave adventurer!\" He says. \"I saw your display 
        of bravery and I have a proposition for you! I'm in need of help for a que- I mean job. A big one. One that'll pay more than you can fathom. What say you?\"""")
        system_methods.delay_print(tw.fill(p36, width=75))
        print()
        print()
        old_man_request(player_gold)

def run_end():
    system_methods.clear_console()
    p32 = inspect.cleandoc("""You run out of the tavern having forgotten the business that you previously had there. You can hear the screams of the individuals inside the tavern followed by large blasts 
    and clanking metal you assume are spells and swords flying around the room.""")
    system_methods.delay_print(tw.fill(p32, width=75))
    print()
    print()
    time.sleep(2)
    p33 = inspect.cleandoc("""Anyhow, that's no longer your concern. You gain your composure and look up at the noonday sky in 
    the city of Waterdeep. The smell of salty sea air sitting in your nostrils calms you down and you head toward the docks, ready to leave this trouble behind.""")
    system_methods.delay_print(tw.fill(p33, width=75))
    print()
    print()
    system_methods.delay_print('To be continued...')
    time.sleep(2)
    print()
    game_mechanics_methods.play_again()

def saitama_troll_end(name, player_hp, player_ac, troll_ac, troll_hp, player_race, player_weapons, player_potions):
    system_methods.clear_console()
    assets.saitama_punch()
    time.sleep(4)
    system_methods.clear_console()
    p53 = inspect.cleandoc(""" The troll explodes from the impact of the punch leaving the crowd covered in a guts and slime.
    \"One punch again?! I thought this was going to be a real fight!\" You are incredulous and disappointed in the ease of the battle. As you stand there the crowd
    erupts once again in thunderous applause. You shrug it off and walk out of the tavern, a bit disappointed the fight wasn't more challenging.""")
    system_methods.delay_print(tw.fill(p53, width=75))
    print()
    print()
    time.sleep(2)
    game_mechanics_methods.play_again()

def pick_up_knife(player_name, player_hp, player_ac, player_race, player_weapons, player_potions):
    system_methods.clear_console()
    p50 = inspect.cleandoc("""As you look down you see that the orc thug must have had a knife drop out of their pocket just before falling into the pit. It looks pretty gross.""")
    system_methods.delay_print(tw.fill(p50, width=75))
    print()
    print()
    while True:
        print("Do you PICK UP or LEAVE the nasty knife?")
        print()
        choice = input("Choice: ")
        choice = choice.lower()
        system_methods.clear_console()
        if choice == 'pick up':
            system_methods.delay_print("You pick up the nasty knife and add it to your inventory.")
            player_weapons.append('NASTY KNIFE')
            print()
            print()
            input('Press Enter to continue...')
            troll_fight_choice(player_name, player_hp, player_ac, player_race, player_weapons, player_potions)
        elif choice == "leave":
            system_methods.delay_print("You leave the knife on the ground.")
            print()
            print()
            input('Press Enter to continue...')
            troll_fight_choice(player_name, player_hp, player_ac, player_race, player_weapons, player_potions)
            break
        else:
            print("Not a valid input. Try again")
            print()
            input('Press Enter to try again...')
            system_methods.clear_console()

from os import name
import random
import time, sys

def start_game():

    left = ["Left", "left", "L", "l"]
    right = ["Right", "right", "R", "r"] 
    straight = ["Straight", "straight", "S", "s"]
    yes = ["Yes", "yes", "Y", "y"]
    no  = ["No", "no", "N", "n"]
    ans = input
    choice = input
    riddle_ans = ["fire","a candle","the future","an echo","darkness"] 
    riddles = ["Give me food i will live, give me water and i will die what am I?",             
        "I'm tall when I'm young, and short when I'm old. What am I?",                         
        "What's always in front of you but can't be seen?",
        "What can't talk but will reply when spoken to?",
        "It can't be seen, can't be felt, can't be heard, and can't be smelt. It lies behind stars and under hills, And empty holes it fills. It comes first and follows after, Ends life, and kills laughter. What is it?"]

    def print(str):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.0005)


    def intro():

        print("\x1b[1;37;40m")
        print("                    𝕎𝔼𝕃ℂ𝕆𝕄𝔼 𝕋𝕆.....\n")

        print("              ╔╗╔═╦══╦══╗╔╦═╦╗╔══╦╦╦═╗╔═╦╗╔═╦══╗\n")
        print("              ║╚╣║╠╗╚╬╗╔╝║║║║║╚╗╔╣═║╦╣║╩║╚╣╔╬╗╚╣\n")
        print("              ╚═╩═╩══╝╚╝ ╚╩╩═╝ ╚╝╚╩╩═╝╚╩╩═╩╝╚══╝\n")

        
        print("    .                  .-.    .  _   *     _   .\n")
        print("           *          /   \     ((       _/ \       *    .\n")
        print("         _    .   .--'\/\_ \     `      /    \  *    ___\n")
        print("     *  / \_    _/ ^      \/\'__        /\/\  /\  __/   \ *\n")
        print("       /    \  /    .'   _/  /  \  *' /    \/  \/ .`'\_/\   .\n")
        print("  .   /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _\n")
        print("\x1b[1;30;40m")
        print("    /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \ \n")
        print("   /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \ \n")
        print("  /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.\n")
        print(" /        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-  \ \n\n")

        
        time.sleep(0.0005)
        
        print("\x1b[1;36;40m")     
        print("You wake up dazed, not knowing where you are. You find yourself lost in the Alp Mountain's.\n")

        global name
        name = input("What's Your Name Mate?\n")

        print(f"Whats appenin, {name} . Let's get you home!!!\n\n")

        print("\x1b[1;30;40m")

        print("░▀█▀░█░█░█▀▀░░░█▀█░█▀▄░█░█░█▀▀░█▀█░▀█▀░█░█░█▀▄░█▀▀░░░█▀▄░█▀▀░█▀▀░▀█▀░█▀█░█▀▀░░░░░░░░░░░\n")     
        print("░░█░░█▀█░█▀▀░░░█▀█░█░█░▀▄▀░█▀▀░█░█░░█░░█░█░█▀▄░█▀▀░░░█▀▄░█▀▀░█░█░░█░░█░█░▀▀█░░░░░░░░░░░\n")
        print("░░▀░░▀░▀░▀▀▀░░░▀░▀░▀▀░░░▀░░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀░░░▀▀░░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░░▀░░▀░░▀░ \n\n")

        time.sleep(0.5)

        print("\x1b[1;36;40m")

        print("You gather yourself together and start walking, after sometime you stumble across a fork\n") 
        levelone()

    def levelone():

        print("\x1b[1;36;40m")
        print("in the beaten track there lies in front of you three paths\n")

        print("To your left the road enters a snow capped forest.\nTo your right the path winds between deep drifts of snow.\nStraight ahead the path disappears into the mist.\n")  

        print("What route would you like to take?\nChoose carefully, " + name + ", for ahead there be both adventure......  and DANGER!\n") 

        choice = input("Do you choose the left, right or straight ahead?\n")
    
        if choice in left:
            print("You have taken the path to the left,\n")
            print("\x1b[1;31;40m")
            print("It's starting to look a bit sketchy!!!!\nYou lose your bearing's and fall over a rock.....\nYou get up and stumble around in a panic. The fog is too thick to see where you are going...\n  NO... STOP!!! \nThe next thing you know you're falling through the crisp mountain air to your doom. \nIn your haste you blundered off the edge of a cliff!!!!!!! \nFor now, your adventuring days are over.\n")
            game_over()
    
        elif choice in right:

            print("You take the winding path to the right, past the steep drifts of snow to your left and right.\nAfter some time you come out into a snow blanketed clearing. Ahead of you is a hut in the distance.\n\n")


            print("\x1b[1;37;40m")
            print("                      (   ) \n")
            print("                       (    )\n")
            print("                         (    )\n")
            print("                          (    )\n")
            print("                            )  )\n")
            print("                           (  (                  /\ \n")
            print("                            (_)                 /  \  /\ \n")
            print("                    ________[_]________      /\/    \/  \ \n")
            print("           /\      /\        ______    \    /   /\/\  /\/\ \n")
            print("          /  \    //_\       \    /\    \  /\/\/    \/    \ \n")
            print("   /\    / /\/\  //___\       \__/  \    \/\n")
            print("  /  \  /\/    \//_____\       \ |[]|     \ \n")
            print(" /\/\/\/       //_______\       \|__|      \ \n")
            print("/      \      /XXXXXXXXXX\                  \ \n")
            print("        \    /_I_II  I__I_\__________________\ \n")
            print("\x1b[1;30;40m ")
            print("              I_I|  I__I_____[]_|_[]_____I\n")
            print("               I_II  I__I_____[]_|_[]_____I\n")
            print("               I II__I  I     XXXXXXX     I\n")
            print("            ~~~~~_____~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

            time.sleep(0.0005)


            print("\x1b[1;36;40m")
            print("Do you head for the hut?????\n")
            leveltwo()

        elif choice in straight:
            print("You take the path straight ahead of you. As the wind picks up the snow thickens, making it difficult to see the path. One particularly strong gust blows you off the path and into a deep drift of snow. You panic, stumbling around, searching for the trail you was following... A sigh of relief escapes you as you find your way back to the path, and  countinue your journey. After struggling through the veil of snow for what seems like hours, the wind dies down and the snowfall lightens to a gentle sprinkling. At last, you can see the path before you clearly. Just ahead of you the path splits to the left and right. \n")
            levelthree()     
        else:
            print("Thats not an option pal, try again\n\n")
            levelone()

    def leveltwo():

        ans = input ("")
    
        if ans in yes:
            print("\x1b[1;36;40m")
            print("You make it to the hut just as night falls. \nOnce you enter the hut you seee, to your wonder, a neatly made bed and some dried meat hanging from a hook. \nYou sit on the surprisingly soft and dry bed and take in your surroundings. \nThe bed seems to be calling to you, and your tired limbs ache in response. The only question on your mind is: \n Do you spend the night?\n")  
            levelfive()

        elif ans in no:
            print("You take what you can carry from the hut and countiune on your way\n")        
            levelseven()
            
        else:
            print("Thats not an option, try again!\n\n")
            leveltwo()
    
    def levelthree():
        
        print("Before you lies a well-worn path to the left, leading off into the distance. A faint, barely used path leads to the right.\n")
        
        print("Which route would you like to take, left or right?\n")
        
        choice = input("")
    
        if choice in left:
            print("\x1b[1;37;40m")
            print("You follow the beaten track. With every step you take the wind seems to get stronger. Sleet plasters you from head to toe, the cold, like knives, pierces your every joint. \nWithout warning, the blustering winds die down, the sleet turns to soft snowfall...\nYou look around, confused but glad to out of the blizzard, and then it suddenly hits you:\nYou've ended up right back where you started!!!....\n")
            levelone() 
            # loops back to the start

        elif choice in right:
            print("\x1b[1;36;40m")
            print("You carefully follow the faint path in the snow, hoping the trail doesn't disappear completely. \nAfter 15 minutes, you come across a snow mobile parked just off the beaten track.\nWhat luck! The keys are in the ignition. You look around for the owner but there's nobody in sight and no footprints in the snow either coming or going from the vehicle.\nAfter calling out for the owner, with no response, you stare longingly at what may well be the answer to your prayers.\nDo you take the snow mobile??\n")
            levelfour()
        
        else:
            print("Thats not an option I'm afraid\n\n")
            print("Try again\n\n")
            levelthree()
        

    def levelfour():
       
        choice = input("")

        if choice in yes :
            print("You turn the key.... NOTHING!  After moment of turning the air blue with some particularly salty language a sailor would be proud of, you try the key again. \n'VROOOMM'. The engine roars into life. You yell out in triumph, turn the throttle to full, and tear off down the mountainside.\n'Whats that!?'. You turn your head and see, crashing behind you an avalanche. Your shouts of joy must've caused the loose snow to start sliding, picking up momentum and more snow as it chases you down the mountain.\nYou curse softly under your breath and duck low into the freezing wind, hoping against hope to outrun the crashing wall of winter death which follows behind.\nYou risk a quick peek behind... Relief washes over you like sunshine as you see the avalanche has used up it's pent up energy and is settling down, waiting silently for it's next victim.\nEasing off the throttle, you head towards the now visible village at the base of the mountain. To safety. To warmth. To Beer!\n")

            time.sleep(0.00000005)

            print("\x1b[1;33;40m")
            print("     |    ||     |                  (\ /)     | ||  o | . |     |	\n")
            print("     | o  ||  _  |                 .--==--.   | ||    |   |     |	\n")
            print("     |    ||     |               .'//|/)(|)\  | ||    |   |   o |	\n")
            print(" >   |    ||     |              /)/|(/|\||||\ | ||    |   |     |	\n")
            print("     |  . ||   o |            .'/))/'(|)' ||  \ | o   |   |     |	\n")
            print("     |    ||     |          .')/|/))`  __  /\)| ||    |   |     |	\n")
            print("     |    ||     |         /)(|\|(/'.`.__.'(\)| ||    | ______  |	\n")
            print("     |  o ||     |         )/(|\)-. -` - '-.--. || o  ||   .::| |	\n")
            print(" o   |    ||     | ______ (|.'    /`.''. .''`  `.'    ||   '::| |	\n")
            print("     |    ||  .  ||::.   | (/| /\ | \   /\    \/\)  < ||   '::| |	\n")
            print("     |    ||  |  ||::'   |  `.\)(/. |   | |   |.'\   .'\   '::/ |	\n")
            print("     |  \ ||     ||::'   |    `-' '.'`-' : `-.`   \.'  '`.__.'  |	\n")
            print("     |    ||o    '\::'   /-.._/   /\_   _    | \  `   /   |     |	\n")
            print("     |    ||     | `.__.'_    `  / / `-/ \--/   \    /|   |     |	\n")
            print("   o |    ||     |        `-.._.'.'/`--\_/--|    `..' |   | o   |	\n")
            print("     |    ||     |             .' '        \ \  ||  < |   |     |	\n")
            print(" /   |    ||     |            /  /          `.\ ||    |   |     |	\n")
            print("     | o  || _   |           /   `.           \`.|    |   |  .  |	\n")
            print("     |    ||    o|          | `.   `._      .'  _\ -  |  -|     |	\n")
            print("     |    ||     |          `. .`-._  `-._.'_.-'.`    |   |     |	\n")
            print("o    |    ||     |            `|    `-.__.-'  :' |    |   |   o |	\n")
            print("     |  - ||     |              \         :   | || o  |   [     |	\n")
            print("     |    ||     |               `        |   | ||    |   |     |	\n")
            print("     |    ||o    |                \       |   | ||    | | |     |	\n")
            print("     |    ||   < |                 \      |   / ||    | . |     |	\n")
            print("     |   o||     |                  |     |   : ||    |   | o   |	\n")
            print("   o |    ||     |                 .:     :  /  ||   o|   |     |	\n")
            print("     |    ||     |               .'      /  | | ||    |   |     |	\n")
            print("     |    ||     |              /\_     '-._' | ||    |   |  |  |	\n")
            print("  \  |  . ||     |             /_  `-._:-.__| | || <  |o  |     |	\n")
            print("     |  | ||    o|            |  `-.__/     | | ||    |   |  _  |	\n")
            print("-    |  | ||     |            )      /\     | | ||    |   |     |	\n")
            print("     |    ||     |            |     ' |     | | ||o   |   | o   |	\n")
            print("     |    ||     |           /     /  |     | | ||    |   |     |	\n")
            print("     |    ||   . |           |   .'   `     | | ||    |   |     |	\n")
            print("     |   .||o    |          /   /      \    | | ||    |   |    o|	\n")
            print(" o   |    ||     |         )    \       |   | | ||    | > |     |	\n")
            print("_____|____||     |        '     / ..--'` )  | '.||____|___|_____|	\n")
            print("      LGB `|_____| ..--'`/    .'        /   (   __...'         ___	\n")
            print("    _            '      /_  .'  ___,.. (     `. ___....----'''		\n")
            print(" '  _ _..`.  ___`-  --'`\_.'   ___ ..   `-._   `.           ____`...	\n\n")

            time.sleep(0.5)

            
        elif choice in no :
            print("Thinking the owner must be just out of earshot, you sigh, gather up your belongings, and begin to trudge steadily down the mountain. \nYou turn, cup your hands around your mouth and give one last shout for the owner of the snowmobile... 'HELLOOOO!'.")
            print("\x1b[1;31;40m\n")
            print("A crashing sound thunders in reply, getting louder and louder. Your shouts have started the relentless cascade of an Avalanche!!! \nYou turn away from the horrific sight, running as fast as you can through the knee deep snow. The crashing is getting louder... nearer...\nIn your desparation you fall headlong into the snow, tumbling faster and faster down the steep gradient. The snapping of bones and tendons causes you to scream in agony as you hurtle downhill, \nyour cries drowning out the sound of swiftly approaching death. \nAs you lay, crushed beneath a solid wall of densely packed snow, struggling to breath and with fire coursing through your nerves, you think again of the abandoned snowmobile. \nThen darkness takes away your pain and you let out a soft gasp as you slip into death's sweet embrace. \nRest easy now, traveller. Your adventures here have reached their end.\n")
            game_over()
            
        else:
            print("Incorrect input dude, sort yourself out!")
            levelfour()
            
    def levelfive():
        
        choice = input("")

        if choice in yes:
            print("\x1b[1;36;40m")
            print("You awake with a start...  You've been woken up by a large, hungry polar bear prowling around the hut. \nHe stops , sniffing through the small gap at the bottom of the door, and starts scratching at the wooden door. \n'CRASH!'. The door bursts inward and you are left face to face with an angry bear. \nHe pads towards you, stops, and raises his snout, sniffing the air. \nYou grab for the dried meat before the bear manages to snap it up. He turns towards you and lets out a mighty roar. \nHis fetid breath assaults your senses and you reel back in fear and disgust. The polar bear approaches you, drool hanging from his maw. \n Do you fight the polar bear for the meat?\n") 
            levelsix()
        elif choice in no :
            print("You take what you can carry from the hut and countinue on your way.\n")
            levelseven()
        else:
            print("Jesus Christ! Thats DEFINITELY not an option\n\n")
            levelfive()

    def levelsix():
        
        choice = input("")

        if choice in yes:
            print("\x1b[1;31;40m")
            print("The bear snaps his teeth at the hand clutching the dried meat. You pull your hand back and kick out at the bear's face. \nBad mistake! The polar bear rears up on his hind legs, lifts his enourmous forelegs with his claws extended, and slams down onto you. \nThe crunch of breaking ribs fills your ears and the sudden agony drowns out all thoughts of fighting. You struggle to take a breath, but your shattered ribs have lacerated your lungs. \nBlood runs in crimson rivulets from the corners of your mouth and your life ebbs away. Again the bear rears up, all interest in dried meat forgotten. He now has fresh meat! \nJust as the bear begins his second lunge at you, the world turns to darkness and the pain and fear dissipate into the void. \nYour adventure has come to a sorry end.\n")
            game_over()
        elif choice in no :
            print("\x1b[1;36;40m")
            print("Do you share the dried meat with him?\n")
            leveleight()
        
        else:
            print("I'm getting tired of your shenanigans!!\n")
            print("Last chance\n")
            levelsix()

    def levelseven():
        
        print("You continue past the hut what seems like a life time when.....\n you see someone in the distance..\n")
        print("\x1b[1;30;40m")
        print("""             
                              ___,
                           __)____)__
                              -)- )))
                    ,         \=_/ \__
                 __/).          )_/=\ 
                /6)   \      __((_\_/\ 
               /   __/ \    /_/-\o____)
              / ,_/|    \   \/  ))\\\\\ 
              \_)o_'     _.-'  ,/:_/_\\  ___
                 '---`' \>__/   /\\---.,/_  \ 
                  (      / /   /\\        \)  \ 
                  |        ('  \\\        (   /
             _____/         )__\\ /       /\ (
            / _______/,_____| |_,(       /  ) )
           / (_     \  |   _/ o)  \     /_  |/
           \_ /     ( '| (___/     `.__  /  '
                     \ |        / _/ / _/
                      \(       / /  / /
                       )\     / (  ( <
                    ,./_(,, ,/_|    \_/,, \n\n""")
        
        time.sleep(0.0005)
                
        print("Do you approach the mysterious person??\n")

        choice = input("")

        if choice in yes:
            print("\x1b[1;36;40m")
            print("The villager gives you a look of mistrust.. takes a breath.. and says...\n")
            levelnine()
        elif choice in no :
            print("\x1b[1;32;40m")
            print("You countinue on your way, you lose your bearings and end up lost!!!!!")
            levelone()
            # loops back to the start
        else:
            print("Seriously?")
            levelseven()

    def leveleight():
        time.sleep(0.05)
        choice = input ("")

        if choice in yes:
            print("Mustering all of your courage, you take a handful of the dried meat and extend your arm towards the polar bear. \nImmediately, the bear's countenance changes. It sniffs your hand and gently takes the offered morsel. \nAfter accepting the meat the bear turns around, looks back at you, and makes it's way to the door. Once there he waits and once again glances back at you before sitting down. \n'Does he want me to follow him?', you think. You get up and walk towards the bear. He gets up and makes his way out of the door, looking back at you every now and again. Amazingly, when you stop, so does he, patiently waiting for you to follow. It seems that you have gained the polar bears trust. \nAfter walking for what seems like hours, stopping only once to share a little of the remaining dried meat, you emerge from a copse of fir trees and see the village a short distance away at the base of the mountain. \nThe polar bear then turns around and walks up to you slowly. He lowers his head and allows you to ruffle the fur on his head, then he simply turns and walks back towards the clump of trees and back up the mountain. \n'Farewell, my friend.' you mutter under your breath, before turning to face the last few hundred yards of your trek before safety. \nCongratulations, adventurer. You have made it home in one piece.\n\n")

            print("\x1b[1;37;40m")
            print("                   _         _\n")
            print('  .-""-.          ( )-"```"-( )          .-""-.\n')
            print(' / O O  \          /         \          /  O O \ \n')
            print(' |O .-.  \        /   0 _ 0   \        /  .-. O|\n')
            print(" \ (   )  '.    _|     (_)     |     .'  (   ) / \n")
            print("   .`-'     '-./ |             |`\.-'     '-'.'\n")
            print('    \         |  \   \     /   /  |         /\n')
            print("     \        \   '.  '._.'  .'   /        /\n")
            print("       \        '.   `'-----'`   .'        /\n")
            print("         \   .'    '-._        .-'\   '.   / \n")
            print("            /`          `'''''')    )    `\|\n")
            print("           /                  (    (      ,\ \n")
            print("          ;                    \    '-..-'/ ;\n")
            print("          |                     '.       /  |\n")
            print("          |                       `'---'`   |\n")
            print("          ;                                 ;\n")
            print("           \                               /\n")
            print("            `.                           .'\n")
            print("               '-._                   _.-'\n")
            print("                 __/`"  '  - - -  ' "`` \__\n")
            print("              /`            /^\           `\ \n")
            print("              \(          .'   '.         )/\n")
            print("                '.(__(__.-'       '.__)__).'\n")

            time.sleep(0.00000000001
)


        elif choice in no :
            print("\x1b[1;31;40m")
            print("The bear snaps his teeth at the hand clutching the dried meat. You pull your hand back and kick out at the bear's face. \nBad mistake! The polar bear rears up on his hind legs, lifts his enourmous forelegs with his claws extended, and slams down onto you. \nThe crunch of breaking ribs fills your ears and the sudden agony drowns out all thoughts of fighting. You struggle to take a breath, but your shattered ribs have lacerated your lungs. \nBlood runs in crimson rivulets from the corners of your mouth and your life ebbs away. Again the bear rears up, all interest in dried meat forgotten. He now has fresh meat! \nJust as the bear begins his second lunge at you, the world turns to darkness and the pain and fear dissipate into the void. \nYour adventure has come to a sorry end.")
            game_over()
        else:
            print("Last warning, if you do that again I'll have to punish you")
            leveleight()
    def levelnine():
            
        print("If you can answer my three riddles correctly, I will give you the help you need, \n would you like to try an solve my riddles????\n")

        choice = input ("")

        if choice in yes:
            print("\x1b[1;36;40m")
            print("Riddle me this....\n")
            levelten()
        elif choice in no:
            print("You countinue on your way. As the darkness of night falls you stumble around, all but blind in the encompassing blackness. As the snowfall thickens you can hardly see your hand in front of your face, and as for following the path, there's no chance. \nYou are feeling dispirited, cold and hungry, and on top of it all you realise you are completely lost. After blundering around for ages you emerge from a frost rimed thicket. Meanwhile, the snowfall has lightened and you are able to make out your surroundings.\n Amazingly, you are back where you started!!")
            levelone()
        else:
            print("THATS IT!!!!!!!")
            print("Don't say I didn't warn you")
            game_over()

    def levelten():
        print(random.choice(riddles))

        r_ans1 = input("\n") 

        if r_ans1 in riddle_ans:
            print ("You have answered correctly.\nYour second riddle is:\n")
            print(random.choice(riddles))
            r_ans2 = input("\n")
            if r_ans2 in riddle_ans:
                print ("You have answered correctly.\nYour third and final riddle is:\n")
                print(random.choice(riddles))
                r_ans3 = input("\n")
                if r_ans3 in riddle_ans:
                    print("You have answered correctly.\nI will escort you along the path.\n")
                    print("The villager escorts you to the bottom of the mountain and to safety")
                    restart()
                else: 
                    print("'You have answered incorrectly.', booms the voice of the mysterious stranger.\n")
                    print("Without another word, the stranger turns and rides off into the thickening mist,\nleaving you lost and alone on the frozen path.\n")
                    print("\x1b[1;31;40m")   
                    print("As you stumble around blindly, the cold creeps into your body....\nYou stumble and cry out, but alas, your adventuring days are over!\n") 
                    game_over()
            else: 
                print("\x1b[1;36;40m")
                print("'You have answered incorrectly.', booms the voice of the mysterious stranger.\n")
                print("Without another word, the stranger turns and rides off into the thickening mist,\nleaving you lost and alone on the frozen path.\n")
                print("\x1b[1;31;40m")
                print("As you stumble around blindly, the cold creeps into your body....\nYou stumble and cry out, but alas, your adventuring days are over!\n") 
                game_over()
        else: 
            print("\x1b[1;36;40m")
            print("'You have answered incorrectly.', booms the voice of the mysterious stranger.\n")
            print("Without another word, the stranger turns and rides off into the thickening mist,\nleaving you lost and alone on the frozen path.\n")
            print("\x1b[1;31;40m")
            print("As you stumble around blindly, the cold creeps into your body....\nYou stumble and cry out, but alas, your adventuring days are over!\n")  
            game_over()
           

                    
    def game_over():
        print("The sweet kiss of death")
        print(""""
                                    .... NO! ...                  ... MNO! ...
                                ..... MNO!! ...................... MNNOO! ...
                                ..... MMNO! ......................... MNNOO!!
                                .... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
                                ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
                                    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
                                ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....!
                                ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...
                                    ....... MMMMM..    OPPMMP    .,OMI! ....
                                    ...... MMMM::   o.,OPMP,.o   ::I!! ...
                                        .... NNM:::.,,OOPM!P,.::::!! ....
                                        .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
                                        ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
                                        .. MMMMMNNOOMMNNIIIPPPOO!! ......
                                        ...... MMMONNMMNNNIIIOO!..........
                                        ....... MN MOMMMNNNIIIIIO! OO ..........
                                    ......... MNO! IiiiiiiiiiiiI OOOO ........... 
                                ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
                                .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
                                ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
                                        ...... OO! ................. ON! .......
                                    ................................ 
                  
                   _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______      
                 /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \     
                |  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |    
                |  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /     
                |  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.
                 \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|
                  
                  \nWould you like to play again???""")
        restart()

    def restart():

        choice = input("")

        if choice in yes:
            print("Lets hope you make it this time")
            levelone()
        elif choice in no:
            print(f"Thankyou {name} for playing come back again adventurer and hopefully you have better luck next time, ")

    intro()

start_game()

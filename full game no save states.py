from time import sleep
from graphics import *
import winsound
import random

NAME=input('NAME please \n')

#welcome
def check(T):
    if T.upper()=='HELP':
        print('prepare for fun in the most STRANGE game yet.')
        sleep (1.0)
        print('\t')
        title()

    elif T.upper()=='EXIT':
        exit()

    elif T.upper()=='START':
        story1()

    elif T.upper() == 'YES':
        story2()

    elif T.upper()=='NO':
        story0()

    else:
        print('no')
        title()

def title():
    print('|        TXT Rerun        |')
    print('|     make thy choice     |')
    print('| type start exit or help |')
    print('| dont say no             |')
    TOOL=input('  ')
    check(TOOL)


#falling!
def story1():
    print('chapter 1, a new begining!?\n')
    sleep (2.0)
    print('You wake up in a long dark hallway with a line of people in front of you.\n')
    sleep (2.0)
    print('At the front theres a being that you can\'t recognize with a lantern.\n')
    sleep (2.0)
    print('The being seems to be friendly but fair, with 3 doors behind them. one white with gold tint, one black with red tint and a door thats old and rusty on the ground like a trapdoor.\n')
    sleep (2.0)
    print('At that point you know where you are, purgatory or at best some other space between hell and heaven.\n')
    sleep (2.0)
    print('The being starts to look confused when you get to them and then walks over to the white door with gold tint and peaks in and said something that you could not hear clearly.\n')
    sleep (2.0)
    print('You think that something\'s of and then 3 perfect copys of the being are in front of the line, 2 take care of the line and the third that you recognize as the first one you saw.\n')
    sleep (2.0)
    print('\"My name is Azazel and it seems you died by gods unfair will\" at this point you were confused and shaken, \"don\'t worry i can bring you back to life by sending you to onnel a world with magic But do you want to?\n')
    sleep (2.0)
    put=input ('choose(yes or no): \n')
    check(put)
    
#dead?
def story0():
    print('\"then please enter the white door with gold tint.\"\n')
    sleep (2.0)
    print('congradulations you got the bad ending')

#fun!
def story2():
    print('\"ok please come with me\" they said. guiding you away from the three doors toward the wall of the hall and starts to go in a wall.\n')
    sleep (2.0)
    print('You follow Azazel through the wall and see a dark hole.\'thats the entrance to the new world\'\n')
    sleep (2.0)
    print('You jump in without hesitation and starts falling for a while.\n')
    sleep (2.0)
    print('To be continued\n')
    sleep (2.0)
    print('.',end='')
    sleep (1.5)
    print('.',end='')
    sleep (1.5)
    print('.',end='')
    sleep (1.5)
    print('?',end='')
    sleep (1.5)
    story3()



#the end of chapter!
def story3():
    print('chapter 2, A new start?\n')
    sleep (2.0)
    print ('after falling for what felt like 30 min you black out and open your eyes in the middle of the sky, falling to the ground fast.\n')
    sleep (2.0)
    input ('you need to think fast if you want to live and not end up as a fine RED paste on the ground. what do you do?(call status or check body): \n')
    sleep (2.0)
    print ('\"this is Azazel speaking you might of got dropped off at the wrong place but don\'t worry you will be invincible for the first hit in the world.\" you breath out with glee and sit back to wait for the landing.\n')
    sleep (2.0)
    print ('at this moment you think of calling your status screen\n')
    sleep (2.0)
    print ('___stats___')
    print ('HEALTH POINTS: 10')
    print ('MANA : 10')
    print ('ATTACK: 10')
    print ('DEFENCE: 10')
    print ('LUCK: 10\n')
    print ('SKILLS: appraisal:LV 1, fire LV 1')
    sleep (2.0)


    print ('while falling you see A Village and A FOREST\n.')
    meta=input('where do you go(forest or village):')
    if meta.upper() == 'FOREST':
        GOD()
    
    elif meta.upper() == 'VILLAGE':
        village()

    elif meta.upper() != 'FOREST' or 'VILLAGE':
        print('try once more')
        story3()

#YOU CAN'T RUN
def GOD():    
    print('as soon as you land you head to the forest that all of a sudden seems a lot more red then you remember.\n')
    sleep (2.0)
    print('the ground is a sickly red and there are dead monsters that look gutted for some reason\n')
    sleep (2.0)
    GOD=input('there\'s a strangely lanky humonoid creature (talk)\n')
    if GOD.upper() == 'TALK':
        print('you go up to the man to talk and when you see his face your scared out of your mind\n')
        sleep (2.0)
        print('his face was completely ripped to sheds and you die with an arm from the back pirceing you gut from something\n')
        sleep (2.0)
        print('very')
        sleep (2.0)
        print('Very')
        sleep (2.0)
        print('BAD')
        sleep (2.0)
        print ('nice try' ,NAME,'!')
        
        winsound.PlaySound('sonic_1',winsound.SND_FILENAME)

        maxHeight=600
        maxWidth=1000

        win=GraphWin("HAHAHAHAHAHAHAHAHAHAHA",maxWidth,maxHeight);
        bkgnd=Image(Point(500,300),'I AM GOD!.png')
        bkgnd.draw(win);

    elif GOD.upper() != 'TALK':
        print('DO IT')
        GOD()

#excuse me?
def village():
    print ('after the fall of your life you end up walking to the village that you saw when you were up in the sky.\n')
    sleep (2.0)
    print ('when you get to the village you notice that its full of life but at the same time eerily quiet.\n')
    sleep (2.0)
    print ('when you enter the village people come out and ask you a question.\"are you here to slay the beast?\"\n')
    sleep (2.0)
    print ('you say no but ask what the beast is because you come from a remote mountan village(a good back story that you made on the way here.)\n')
    sleep (2.0)
    print ('\"no one knows what the beast is actually, But it came and started killing off the adventures that enter the forest of crimson trees.\"\n')
    sleep (2.0)
    print ('they said that they sent someone to the capital to get help in killing it but the army said that\" its no use\" and \"its for the greater good\".\n')
    sleep (2.0)
    choice=input ('do you help them:(yes or yes(you have no choice))\n')
    sleep (2.0)
    
    if choice.upper() == 'YES':
        print('\"thank you kind sir we will give you a weapon to fight said beast.\"\n')
        sleep (2.0)
        print('you got a sword?\n')
        sleep (2.0)
        print('\"we have a foke lore that everyone here knows but no one can give the same story.\"\n')
        sleep (2.0)
        print('\"there are tales of a creature of pitchblack\" \"DARK RED!\" \"SHUT UP DAVE! anyways where was I?\"\n')
        sleep (2.0)
        print('\"oh right A pitchblack creature lived in theses woods back when we were kids.\"\n')
        sleep (2.0)
        print('\"It was stronger then anything that lived there and was never the same creature everytime we saw them, A bear, A goblin, An Orc, it was not known what it truly was.\"\n')
        sleep (2.0)
        print('\"anyone that was an adventurer died when entering the forest with ill intent and when the army when to slay the creature that they thought was the reincarnation of the maou(demon king) well you can guess what happend next.\"\n')
        sleep (2.0)
        print('\"well good luck random man\"\n')
        FOREST2()

    elif choice.upper() != 'YES':
        print('try once more')
        village()


def FOREST2():
    print('you reach the edge of the forest with nothing but a sword on your back and your brains.\n')
    sleep (2.0)
    RUN=input('what do you do (run or stealth): \n')
    if RUN.upper() == 'RUN':
        print('you run in with gusto and start to look for the beast but you can\'t find it\n')
        sleep (2.0)
        print('at that point you notice that something feels odd... like something is watching you.\n')
        sleep (2.0)
        print('\"Ready for Round Two?\"',NAME,'\n')
        sleep (2.0)
        winsound.PlaySound('sonic_1',winsound.SND_FILENAME)

        maxHeight=600
        maxWidth=1000

        win=GraphWin("HAHAHAHAHAHAHAHAHAHAHA",maxWidth,maxHeight);
        bkgnd=Image(Point(500,300),'I AM GOD!.png')
        bkgnd.draw(win);

    elif RUN.upper() == 'STEALTH':
        print('you enter slowly and quietly trying to find the beast.\n')
        sleep (2.0)
        print('you begin to find a short dark blue hedgehog standing in the middle of the carnage completely ignorant to you.\n')
        sleep (2.0)
        fight=input('what do you do(fight or run): \n')
        sleep (2.0)

        if fight.upper() == 'FIGHT':
          BATTLE()

        elif  fight.upper() == 'RUN':
            print('you start to sneak away to run when you notice that while you were still in the same spot you started in with the beast getting closer every time.\n')
            sleep (2.0)
            winsound.PlaySound('sonic_1',winsound.SND_FILENAME)

            maxHeight=600
            maxWidth=1000

            win=GraphWin("HAHAHAHAHAHAHAHAHAHAHA",maxWidth,maxHeight);
            bkgnd=Image(Point(500,300),'I AM GOD!.png')
            bkgnd.draw(win);

        elif RUN.upper() != 'FIGHT' or 'RUN':
            print('try once more')
            FOREST2()

    elif RUN.upper() != 'STEALTH' or 'RUN':
        print('try once more')
        FOREST2()


def BATTLE():
    duo=20

    player=10

    MP=10

    HPpotions=5

    MPpotions=5
    
    while duo > 0:
         CC=input('what do you do:(fight, magic, item or guard)')

         if CC.upper() == 'ITEM':
              print('HPpotions =',HPpotions)
              print('MPpotions =',MPpotions)
              PC=input('use what item?')
              if PC.upper() == 'MPPOTIONS':
                   MP+=10
                   MPpotions-=1
              elif PC.upper() == 'HPPOTIONS':
                   HP+=10
                   HPpotions-=1
              
                

         elif CC.upper() == 'FIGHT':
              letters=['1','2','3','4','5','6','7','8','9','10']
              random_index=random.randint(0,len(letters)-1)
              print('you dealt',letters[random_index],'\n')
              duo-=int(letters[random_index])

         elif CC.upper() == 'MAGIC':
             DDD=input('what magic do you use.(fire)')
             if DDD.upper() == 'FIRE':
                 if MP > 3:
                     letters=['10','11','12','13','14','15','16','17','18','19','20']
                     random_index=random.randint(0,len(letters)-1)
                     print('you dealt',letters[random_index],'\n')
                     duo-=int(letters[random_index])
         
                              
         letters=['1','2','3','4','5','6','7',]
         random_index=random.randint(0,len(letters)-1)

         if CC.upper() == 'GUARD':
               letters=['1','2','3','4']
               random_index=random.randint(0,len(letters)-1)

         else:
             print('too bad')

         print('??? dealt',letters[random_index],'\n')
         player-=int(letters[random_index])
         
         
    story31()



def story31():
    print('you win!\n')
    sleep (2.0)
    print('\"wait a second!\" the monster said in a hurry\n')
    sleep (2.0)
    print('\"you got the wrong monster\"\n')
    sleep (2.0)
    print('you ask what that means?\n')
    sleep (2.0)
    print('\"It means that I did not kill anyone only defend myself\"\n')
    sleep (2.0)
    print('the monster starts to change in to a small blue blob on the ground\n')
    sleep (2.0)
    print('\"people use to come and kill us for no reason and I was born with ilusion magic\"\n')
    sleep (2.0)
    print('at that point you relized something the blue blob made ilusions of adventures to deter people from entering and scared away an army\n')
    sleep (2.0)
    print('you ask if the blob wants to come with you with you telling the villagers that all monsters were killed.\n')
    sleep (2.0)
    print('\"sure why not I\'ve been wanted to leave here eventualy, do you have a name?\"\n')
    sleep (2.0)
    print('\"your name is',NAME,'? well my name is artemis!"')
    sleep(2.0)
    print('    __________________  ')
    print('   /                  \\  ')
    print('  /                    \\  ')
    print(' /                      \\  ')
    print('|     ---       ---      |')
    print('|                        |')
    print('|    __          __      |')
    print('\\    |          |       /') 
    print(' \\    \\        /       /')
    print('  \\    --------       /')
    print('   \\_________________/') 
    storyC()


#meeting with knight
def storyC():
    print('After leaving the forest with Artemis you to start your journey to the capital of onnel. fettatoni\n')
    sleep (2.0)
    print('You start your journey full of hope for a fun and full filling second life and then your being chased by 20 absurdly large bandits with shovels.\n')
    sleep(2.0)
    print('\"This is great!\" said Artemis with glee on her see though face, yea when you arn\'t running for your life!\n')
    sleep(2.0)
    print('What do you do? (do you..\n')
    print('\" IM HERE TO HELP\" someone yelled from behind all the bandits\n')
    sleep(2.0)
    print('At that exact moment the bandits started flying left and right past you with them screaming in fear\n')
    sleep(2.0)
    print('\"Grab a hold!\" said the voice as a hand flys by to fast for you to grab\n')
    sleep(2.0)
    print('You eventualy grab a hold of said hand and say thanks to the stanger\n')
    sleep(2.0)
    print('\"No problem thats what knights are for!\" you ask if you could be shown the direction of the capital?\n')
    sleep(2.0)
    print('\"No need i\'ll take you there!\"\n')
    sleep(2.0)
    print('After a full day on a horse on performance enhancement drugs (You think thats the case.) You reach the capital barfing\n')
    sleep(2.0)
    print('As soon as you finished barfing you thank the knight and go in the the capital fettatoni.\n')
    sleep(2.0)
    CC=input ('Where do you go from here?(guild or shop):\n')
    sleep(2.0)
    if CC.upper() == 'GUILD':
        GUILD()


    else:
        SHOP()

#Lamp oil, rope, bombs. You want it? It's yours my friend, as long as you have enough gold. Sorry pal, I can't give credit. Come back when you're a little, MMMMMMMMMMM richer. from (https://copypastatext.com/morshu/) changed to fit
def SHOP():
    print('With Artemis still hidden in your bag you head to the nearest shop\n')
    sleep(2.0)
    print('\"Welcome to jacks weapons shop what do ya want\"\n')
    sleep(2.0)
    print('before you say anything you relise that you have no money and should probably go to the guild first\n')
    GUILD()
    
#classic "ya look like a bag o bones"
def GUILD():
    print('With Artemis still hidden in your bag you head to the guild.\n')
    sleep(2.0)
    print('\"Welcome to the guild do you have a request?\"\n')
    sleep(2.0)
    print('You say no and ask if you could become an adventurer.\n')
    sleep(2.0)
    print('The guild member skoffs. \"Sure you can try. Head left.\"\n')
    sleep(2.0)
    print('\"she does not seem nice\" Artemis said quietly to you. at that point you notice that you physicaly did not change after death so you look weak.\n')
    sleep(2.0)
    print('After heading left you enter a arena filled with people fighting two people.\n')
    sleep(2.0)
    print('Ones a small girl with a staff bigger then her and you guess that she is a mage.\n')
    sleep(2.0)
    print('The other is a big grissly bear looking man holding a claymore.\n')
    sleep(2.0)
    print('After about 10 min of waiting you get to go fight what you think are the examiners\n')
    sleep(2.0)
    print('\"Nice to meet\'cha!\" said the grissly. the girl just looked bored and did not say anything\n')
    sleep(2.0)
    print('\"We are the examiners for all you test\'en\"he said \"so lets get started!\" he said as he came at you!\n')
    BATTLE2()

#DUEL https://www.youtube.com/watch?v=xMgawMBPaiw
def BATTLE2():
    duo=40
    
    player=15

    MP=10

    HPpotions=5

    MPpotions=5

    while duo > 0:
         CC=input('what do you do:(fight, magic, item or guard)')

         if CC.upper() == 'ITEM':
              print('HPpotions =',HPpotions)
              print('MPpotions =',MPpotions)
              PC=input('use what item?')
              if PC.upper() == 'MPPOTIONS':
                   MP+=10
                   MPpotions-=1
              elif PC.upper() == 'HPPOTIONS':
                   HP+=10
                   HPpotions-=1
            
                

         elif CC.upper() == 'FIGHT':
              letters=['1','2','3','4','5','6','7','8','9','10']
              random_index=random.randint(0,len(letters)-1)
              print('you dealt',letters[random_index],'\n')
              duo-=int(letters[random_index])

         elif CC.upper() == 'MAGIC':
             DDD=input('what magic do you use.(fire)')
             if DDD.upper() == 'FIRE':
                 if MP > 3:
                     letters=['10','11','12','13','14','15','16','17','18','19','20']
                     random_index=random.randint(0,len(letters)-1)
                     print('you dealt',letters[random_index],'\n')
                     duo-=int(letters[random_index])
           

                   
         letters=['1','2','3','4','5','6','7']
         random_index=random.randint(0,len(letters)-1)

         if CC.upper() == 'GUARD':
               letters=['1','2','3','4']
               random_index=random.randint(0,len(letters)-1)


         print('the duo dealt',letters[random_index],'\n')
         player-=int(letters[random_index])

         if duo == 0:
             break
            
         elif player == 0:
             print ('you lose')
             exit()
             break
    STORYG()

def STORYG():
    print ('\"You did great!\"He said with a boom. the girl looked shocked that he lost\n')
    sleep(2.0)
    print ('after talking with them for a little you know their names and that people can be tamers\n')
    sleep(2.0)
    print('\"You should go back to the front desk with Mary\"griz said\n')
    sleep(2.0)
    print('\"What kind people.\" Artemis said still hidden in your bag, you agree while Mary glares a hole in you\n')
    sleep(2.0)
    print('You ask if somethings wrong to Mary and she said\n')
    sleep(2.0)
    print('\"You have the talent for powerful magic and you choose to go the path of the sword. Why?\"\n')
    sleep(2.0)
    input('type what you think about magic:\n')
    sleep(2.0)
    print('\"Thats\"\n')
    sleep(1.5)
    print('.',end='')
    sleep(1.5)
    print('.',end='')
    sleep(1.5)
    print('.',end='')
    sleep(1.0)
    print('Deep\n')
    sleep(2.0)
    print('and so after getting your adventures badge you live the rest of your life hunting,gathering and haveing fun with Artemis\n')
    sleep(2.0)
    print('TTTTTTTTTTTTTTTTTTTTTTTHHHHHHHHH     HHHHHHHHHEEEEEEEEEEEEEEEEEEEEEE     EEEEEEEEEEEEEEEEEEEEEENNNNNNNN        NNNNNNNNDDDDDDDDDDDDD     ')   
    print('T:::::::::::::::::::::TH:::::::H     H:::::::HE::::::::::::::::::::E     E::::::::::::::::::::EN:::::::N       N::::::ND::::::::::::DDD   ')  
    print('T:::::::::::::::::::::TH:::::::H     H:::::::HE::::::::::::::::::::E     E::::::::::::::::::::EN::::::::N      N::::::ND:::::::::::::::DD   ')
    print('T:::::TT:::::::TT:::::THH::::::H     H::::::HHEE::::::EEEEEEEEE::::E     EE::::::EEEEEEEEE::::EN:::::::::N     N::::::NDDD:::::DDDDD:::::D  ')
    print('TTTTTT  T:::::T  TTTTTT  H:::::H     H:::::H    E:::::E       EEEEEE       E:::::E       EEEEEEN::::::::::N    N::::::N  D:::::D    D:::::D ')
    print('        T:::::T          H:::::H     H:::::H    E:::::E                    E:::::E             N:::::::::::N   N::::::N  D:::::D     D:::::D')
    print('        T:::::T          H::::::HHHHH::::::H    E::::::EEEEEEEEEE          E::::::EEEEEEEEEE   N:::::::N::::N  N::::::N  D:::::D     D:::::D')
    print('        T:::::T          H:::::::::::::::::H    E:::::::::::::::E          E:::::::::::::::E   N::::::N N::::N N::::::N  D:::::D     D:::::D')
    print('        T:::::T          H:::::::::::::::::H    E:::::::::::::::E          E:::::::::::::::E   N::::::N  N::::N:::::::N  D:::::D     D:::::D')
    print('        T:::::T          H::::::HHHHH::::::H    E::::::EEEEEEEEEE          E::::::EEEEEEEEEE   N::::::N   N:::::::::::N  D:::::D     D:::::D')
    print('        T:::::T          H:::::H     H:::::H    E:::::E                    E:::::E             N::::::N    N::::::::::N  D:::::D     D:::::D')
    print('        T:::::T          H:::::H     H:::::H    E:::::E       EEEEEE       E:::::E       EEEEEEN::::::N     N:::::::::N  D:::::D    D:::::D ')
    print('      TT:::::::TT      HH::::::H     H::::::HHEE::::::EEEEEEEE:::::E     EE::::::EEEEEEEE:::::EN::::::N      N::::::::NDDD:::::DDDDD:::::D  ')
    print('      T:::::::::T      H:::::::H     H:::::::HE::::::::::::::::::::E     E::::::::::::::::::::EN::::::N       N:::::::ND:::::::::::::::DD   ')
    print('      T:::::::::T      H:::::::H     H:::::::HE::::::::::::::::::::E     E::::::::::::::::::::EN::::::N        N::::::ND::::::::::::DDD     ')
    print('      TTTTTTTTTTT      HHHHHHHHH     HHHHHHHHHEEEEEEEEEEEEEEEEEEEEEE     EEEEEEEEEEEEEEEEEEEEEENNNNNNNN         NNNNNNNDDDDDDDDDDDDD        ')

title() 

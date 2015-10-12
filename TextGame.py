import random
import time

#mario's events
def dinosaur():
    print("You are facing a ginormous T-Rex! And he's hungry as hell!")
    print("He is ready to charge at you!")
    print("Quick! What do you want to do?")
    print("A: Run away like a baby.")
    print("B: Fight like a man.")
    print("C: Crap in your pants and hope T-Rex gets disgusted.")
    inp = vinput()
    if inp == "a":
        print("Congratulations! You are oficially a baby! And you barely got out of this. It's a god thing T-Rex got hit by lorry.")
        timetaken = 20
    elif inp == "b":
        print("You certainly are crazy. Fighting a T-Rex is a mighty feat that only the main characters of Jurassic Park have ever done. Talk about being in danger...")
        timetaken == 13
    elif inp == "c":
        print("You are such a scardy cat. Oddly enough, that worked! And in a matter of minutes.")
        timetaken == 5
    print("")
    return timetaken
#reece events
def NickiMinaj():
    print("Nicki Minaj walks passed you")
    print("She's walking quite slow, what do you do?")
    print("A: Think about your students waiting in lecture and ignore Nicki Minaj")
    print("B: Speak to Nicki Minaj, get an autograph & be late to lecture")
    print("C: Follow Nicki Minaj, take her somewhere to eat.")
    inp=vinput()
    if inp == "a":
        print("Congratulations! You put your job first")
        timetaken = 0
    elif inp == "b":
        print("You just couldn't help yourself!")
        timetaken == 5
    elif inp == "c":
        timetaken == 40
    print("Tut tut Michael! Your students are all going to complain")
    return timetaken

def AppleStore():
    print("You witness a riot in the AppleStore")
    print("You see people taking IPads, IPhones and Macbooks, what do you do?")
    print("A: Call the police.")
    print("B: Follow the riot and see what Apple products you can get.")
    print("C: Carry on walking to Coventry University..")
    inp=vinput()
    if inp == "a":
        print("You will see this crime on crime watch")
        timetaken = 2
    elif inp == "b":
        print("You will see yourself on crime watch")
        timetaken == 10
    elif inp == "c":
        timetaken == 0
    print("Well Done! You won't be late for work!")
    return timetaken

#jiminy'a shizz
def attack(inv):
    print("You're driving in your car when suddenly")
    for count in range(0,3):
        time.sleep(1)
        print(".")
    time.sleep(1)
    print("OPTIMUS PRIME RIDING A WHALE EMERGES FROM THE EARTH")
    time.sleep(1)
    print("You have little time to react, you must get these Pi's to the")
    time.sleep(1)
    print("electronically starved students, but you have no time, you must fight!")
    time.sleep(1)
    print("You realise you have 3 options (pattern here ain't there wink emoticon)")
    print()
    time.sleep(2)
    
    print("You can A:")
    print("Run down the street like a little girl screaming, throwing babies at")
    print("the monster trying to get rid of it")
    print()
    
    time.sleep(2)
    print("You can B:")
    print("Using your mega rasberry pi abilites you can create a giant mecha robot")
    print("of doom and do battle with Optimus Whale Lord which will look super cool")
    print()
    
    time.sleep(2)
    print("You can C:")
    print("Scowl angrily at your new robot/whale overlord and attempt to drive past")
    print()
    
    time.sleep(3)
    print("What are you going to do? ")
    inp=vinput()

    if inp=="a":
        print("As you flee down the street like a little schoolgirl late for class Optimus Whale")
        time.sleep(1)
        print("turns round and let's out a mighty whimper, you feel his fishy, mechanical breath")
        time.sleep(1)
        print("hot on your ankles, what do you do?")
        
        time.sleep(2)
        print("You can A:")
        print("keep running down the street and hide in the disabled orphan kids hospital")
        print("and hope it accepts your offering of sacrifice")
        print()
        
        time.sleep(2)
        print("You can B:")
        print("grow a backbone and turn and kick the giant mechamammel in its titanium balls")
        print()
        
        time.sleep(2)
        print("You can C:")
        print("Give up and give in to the sweet relief only death can bring")
        print()
        
        inp2=vinput()

        if inp =="a":
            print("you are the worst kind of person, however the giant fish robot thing accepts")
            time.sleep(2)
            print("your offering of helpless children, you wipe the sweat off your brow and continue")
            time.sleep(2)
            print("on your way to university, with a guilt free mind, you horrible person")
            timetaken=5
                
        elif inp=="b":
            print("you turn round to face the beast, you are immediately stood on and")
            time.sleep(2)
            print("smeared along the pavement, thankfully, the robophibian thing has ")
            time.sleep(2)
            print("the ability to bring you back to life for some reason and then it just ")
            time.sleep(2)
            print("leaves and walks off for some reason, its best if you dont think about it")
            time.sleep(2)
            print("it takes ten minutes for you to come back to life because it does ok")
            timetaken=10
            
        elif inp=="c":
            print("You give in to CyborgWhaleManThing but as you wait for your fate to arrive")
            time.sleep(2)
            print("Jackie Chan turns up and kicks you so hard you fly into the sky Team Rocket")
            time.sleep(2)
            print("You land it what appears to be an identical alternate universe where everything")
            time.sleep(2)
            print("is identical except for the giant whale robot thing thats fading from your memory")
            time.sleep(2)
            print("you shake your head and you have no recollection of the last event, so you just keep")
            time.sleep(2)
            print("walking in a really convinient way, wondering where the last 7 minutes went...")
            timetaken=7
        else:
            print("You've broken the universe good job")
            timetaken=0
            
    elif inp=="b":
        print("You engage in a mighty battle with the RoboWhale and it looks super sweet,")
        time.sleep(2)
        print("like, imagine a michael bay film mixed with avatar and some other cool visual shit")
        time.sleep(2)
        print("it looks super sweet, I've never seen anything so cool in my life, i'm just going ")
        time.sleep(2)
        print("to stop talking so I can watch this amazing, epic, once in a lifetime moment")
        time.sleep(3)
        print("Oooo")
        time.sleep(5)
        print("AhhhH")
        time.sleep(2)
        print("Woaahhh")
        time.sleep(9)
        print("Wow didn't that look amazing, that was a great fight, I guess you can continue on with")
        time.sleep(2)
        print("your day, authough you might be around 14 minutes late now..")
        timetaken=14
        
    elif inp=="c":
        print("surprisingly you drive past really easy and continue, you don't lose any time")
        time.sleep(2)
        print("That took like no time, but that was really boring that could of been something epic...")
        timetaken=0
    else:
        print("You've broke the game good job")
        timetaken=0
    
    return timetaken

def hobo(inv):
    timetaken=2
    return timetaken

def flop(inv):
    timetaken=5
    return timetaken

# V's events
def river():
    print("There is a huge long river infron of you")
    print("You are not able to cross")
    print("What do you want to do?")
    print("A: Swim across the river.")
    print("B: Build a bridge to cross.")
    print("C: Walk around to see if you can find a boat.")
    inp=vinput()
    if inp == "a":
        print("Congratulations! You have the strength for this, very brave!")
        timetaken = 6
    elif inp == "b":
        print("You have wasted a lot of time for this!")
        timetaken == 15
    elif inp == "c":
        timetaken == 8
    print("")
    return timetaken
    
def unicorn():
    print("A unicorn is walking behind you on the way")
    print("She is injured and hungry")
    print("What would you like to do with the unicorn?")
    print("A: Heal the unicorn and feed it with the food in your bag.")
    print("B: Try to run away and hide.")
    print("C: Play with the unicorn and don't bother about arriving late.")
    inp=vinput()
    if inp == "a":
        print("You are very kind, but unfortunately you will have no lunch.")
        timetaken = 9
    elif inp == "b":
        print("You are mean! but you will get to uni faster")
        timetaken == 2
    elif inp == "c":
        print("You are irresponsible!")
        timetaken == 10
    print("")
    return timetaken

def prisoner():
    print("On the way, you have met with 3 prisoners who escaped from jail, they look very scary")
    print("They are trying to steal your stuff and hurt you")
    print("Oh no! What are you going to do?")
    print("A: Take out your phone, call the police and run!!!")
    print("B: Give them all your stuff and run away.")
    print("C: Use your boxing skills and and fight for your life.")
    inp=vinput()
    if inp == "a":
        print("The police are on their way!")
        timetaken = 5
    elif inp == "b":
        print("Oh no!")
        timetaken == 7
    elif inp == "c":
        print("Wow! You are very brave, are all dead but the police are coming after you hahaha!")
        timetaken == 10
    print("")
    return timetaken

def vinput():
    while True:
        try:
            inp=input("Please enter your choice! ").lower()
            if inp in ["a","b","c"]:
                break
            else:
                print("That's not a valid input")
        except:
            print("That's not anything!")
    return inp

def gamerun():
    totaltime=0
    timetaken=0
    count=0
    inv=[]
    used=[]
    print("It's 8.45, you've been up until 3am playing the Battlefront Beta")
    time.sleep(4)
    print("Your girlfriend kicks you out of bed and forces you downstairs")
    time.sleep(4)
    print("you must get to college on time, lets hope nothing slows you down...")
    time.sleep(4)
    for count in range(0,100):
        used.append(count)
    count=0
    while count < 10:
        count+=1
        choice=random.randint(0,99)
        if used[choice]!=101:
            print(used[choice])
            used[choice]=101
            if choice==1:
                timetaken=attack(inv)
            elif choice==2:
                timetaken=river(inv)
            elif choice==3:
                timetaken=unicorn(inv)
            elif choice==4:
                timetaken=prisoner(inv)
            elif choice==5:
                timetaken=dinosaur(inv)
            elif choice==6:
                timetaken=NickiMinaj(inv)
            elif choice==7:
                timetaken=AppleStore(inv)
            else:
                userpl=False
                count-=1
        if userpl:
            input=("Press enter to continue... ")
            
        else:
            used[choice]=101
            timetaken=0
            count-=1
        userpl=True 
        totaltime=totaltime+timetaken
        
    print("You've finally made it to university, and you were only {0} minutes late!".format(totaltime))
    time.sleep(2)
    
def main():
    print("---Welcome to Michaels Excuses Game!---")
    print()
    print("The game where you try to get in on time to your lessons!")
    print()
    print("Would you Like to play?")
    play=input("y/n? ").lower()
    if play =="y":
        print("Lets go!")
        time.sleep(2)
    else:
        print("{0}? Who cares of course you want to play!".format(play))
    quits=False
    while not quits:
        gamerun()
        again=input("That was great wasn't it? would you like to play again(y/n)? ").lower()
        if again=="y":
            print("Let's go again!")
            time.sleep(2)
        elif again=="n":
            quits=True
            print("Thanks for playing!")
            time.sleep(2)
        else:
            print("That's not really a good input is it?")


if __name__=="__main__":
    main()
    

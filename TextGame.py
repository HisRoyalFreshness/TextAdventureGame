import random
import time

#Мario's events
def dinosaur():
    print("You are facing a ginormous T-Rex! And he's hungry as hell!")
    print("He is ready to charge at you!")
    print("Quick! What do you want to do?")
    print("A: Run away like a baby.")
    print("B: Fight like a man.")
    print("C: Crap in your pants and hope T-Rex gets disgusted.")
    inp = vinput()
    if inp == "a":
        print("Congratulations! You are oficially a baby!")
        print("And you barely got out of this.")
        print("It's a god thing T-Rex got hit by lorry.")
        print("Now weren't those some fun 20 minutes?")
        timetaken = 20
    elif inp == "b":
        print("You certainly are crazy. Fighting a T-Rex is a mighty feat that only")
        print("the main characters of Jurassic Park have ever done.")
        print("Talk about being in danger...")
        print("Add 13 minutes to your time, Mr. Norris.")
        timetaken = 13
    elif inp == "c":
        print("You are such a scardy cat. Oddly enough, that worked! And in just 5 minutes.")
        timetaken = 5
    print("")
    return timetaken
def kidnapping():
    print("Run, Michael, run!")
    time.sleep(1)
    print("Oh, wait. Why is that black van stopping right in front of you?")
    time.sleep(2)
    print("What the...")
    time.sleep(2)
    print("STOP!")
    time.sleep(1)
    print("Don't hit--")
    for count in range(0,3):
        time.sleep(1)
        print(".")
    print("Rise and shine! And welcome to today episode of 'Where the hell am I?' starring...")
    time.sleep(1)
    print("YOU")
    print("So, what do you think happened?")
    print("A: You got kidnapped.")
    print("B: You got kidnapped.")
    print("C: You got kidnapped.")
    inp = vinput()
    print("Wow! Now wasn't that hard to figure out!")
    print("Looks like you have nothing to do about it, too...")
    time.sleep(2)
    print("Might as well feel forlorn, because--")
    time.sleep(2)
    print("WHAM!")
    print("'Here's your friendly neighbourhood Spider-Man to the rescue!'")
    print("And just in the nick of time! It only took him 3 days to find you.")
    print("Better late than never!")
    time.sleep(1)
    print("Let's keep going!")
    timetaken = 4320

#George
def Money():
    print("You are walking to university - nervous because no one did the worksheet again!")
    print("Then, outta nowhere, big bag with around 1 bil. CASH! No ID, nothing.")
    print("Now it's your chance. What you gonna do?")
    print("A: Take the money. Save them somewhere until you uni is over for today. And rock on!")
    print("B: Wait for a while in case someone decides to come for his money.Don't forget you have got lectures.")
    print("C: Take them to the police. ")
    inp = vinput()
    if inp == "A":
        print("Honestly, who wouldn't do that!:D")
        timetaken = 12
    elif inp == "B":
        print("A guy came and got the money. You are both late for lectures and not a billionaire.")
        timetaken = 20
    elif inp == "C":
        print("You did the right thing. Nice. You were late for lectures but became a hero.")
        timetaken = 15
    print("")
    return timetaken

def Shoplifting():
    print("While walking to uni you decide to enter a shop to get a snack")
    print("You see one of your student there.")
    print("OMG. What is he doing. He just put one xbox live card and one PSN Plus card into his pocket!")
    print("Oh, no. What you gonna do? You are late for your lectures already.")
    print("A: Tell the staff about that.")
    print("B: Do not tell the staff but have a conversation with the student when you get out of the shop.")
    print("C: Just ignore everything and wait for your turn at the cash register.")
    inp = vinput()
    if inp == "A":
        print("You and your student should go to the police. You have missed the all day at uni. They will cut your wage because you were late. They don't care where have you been.")
        timetaken = 20
    elif inp == "B":
        print("After you got out of the shop you spoke with the student. You are very angry and late for your lecture.")
        timetaken = 11
    elif inp == "C":
        print("This is bad. You are breaking the law. At least you have plenty of before the lecture starts.")
        timetaken = 7
    print("")
    return timetaken

def Lostman():
    print("While walking to uni a man stops you and asks you for directions. He is obviously lost.")
    print("You know where he should go and he asks you if you could help him get there.")
    print("You tell him to get a cab but he has no money and he can't speak English.")
    print("So now what? Don't forget you have a lecture in 15 minutes!")
    print("A: You walk all the way with him to the destination.")
    print("B: You decide to find him a cab which would take him to the wanted destination and give him money for the cab")
    print("C: You just leave him.")
    inp = vinput()
    if inp == "A":
        print("You are a nice person. But you are also so late.")
        timetaken = 20
    elif inp == "B":
        print("There are no cab today huh? You waited 10 minutes for a cab to show up. BTW you are a good person")
        timetaken = 9
    elif inp == "C":
        print("This is bad. You know that, right? At least you were in time.")
        timetaken = 5
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
        timetaken = 5
    elif inp == "c":
        timetaken = 40
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
        timetaken = 10
    elif inp == "c":
        timetaken = 0
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

        if inp2 =="a":
            print("you are the worst kind of person, however the giant fish robot thing accepts")
            time.sleep(2)
            print("your offering of helpless children, you wipe the sweat off your brow and continue")
            time.sleep(2)
            print("on your way to university, with a guilt free mind, you horrible person")
            timetaken=5
                
        elif inp2=="b":
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
            
        elif inp2=="c":
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
    print("As you make your way down a man with a scraggle beard walks by, he")
    time.sleep(2)
    print("puts his hand in the middle of your chest and stop's you in your")
    time.sleep(2)
    print("tracks, he gives you a hard stare, what do you say?")
    time.sleep(2)

    print("Do you A:")
    time.sleep(1)
    print('"Dont touch me! I AM A TEACHER MOTHERFLIPPER"')
    time.sleep(1)
    print("Do you B:")
    time.sleep(1)
    print('"Im so sorry sir please dont take my smart watch pls"')
    time.sleep(1)
    print('"Look here gutterbum, i will pwn you, I have a level 80 paladin n00b"')
    time.sleep(1)
    print()
    inp=vinput()
    
    if inp=="a":
        print("That filthy hobo suddenly falls to the floor and kisses your shoes")
        time.sleep(2)
        print("you think to yourself *finally, the respect I deserve*")
        time.sleep(2)
        print("Once the hobo is done, you continue on your way")
        time.sleep(2)
        print("you walk off, shoes shiny, wallet stolen and happy")
        time.sleep(2)
        print("that was a good shoe shine for 4 minutes")
        
    elif inp=="b":
        print("The hobo roars like a man-lepoard, he then gives you a fish")
        time.sleep(2)
        print("You take the fish and wonder what to do with it")
        time.sleep(2)
        print("You shrug and take a bite out of the fish")
        time.sleep(2)
        print("You think, 'Man that was not worth 3 minute'")
        timetaken=3
              
    elif inp=="c":
        print("Your nerdy prowess swamps his Level 3 Healer")
        time.sleep(2)
        print("You pwn that sucka and move on, authough it took like")
        time.sleep(2)
        print("To find a set of pc's to battle on, like, 30 minutes")
        time.sleep(2)
        timetaken=30
    
    else:
        print("You've broken reality")
        timetaken=0
            
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
        time.sleep(2)
        timetaken =6
    elif inp == "b":
        print("You have wasted a lot of time for this!")
        time.sleep(2)
        timetaken =15
    elif inp == "c":
        print("Hurray! You managed to find a boat and cross the river!")
        time.sleep(2)
        timetaken =8  

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
        time.sleep(1)
        timetaken =9
    elif inp == "b":
        print("You are mean! but you will get to uni faster")
        time.sleep(1)
        timetaken =2
    elif inp == "c":
        print("You are irresponsible!")
        time.sleep(1)
        timetaken =10
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
        time.sleep(2)
        timetaken =5
    elif inp == "b":
        print("Oh no!")
        time.sleep(2)
        timetaken =7
    elif inp == "c":
        print("Wow! You are very brave, are all dead but the police are coming after you hahaha!")
        time.sleep(2)
        timetaken =10
    return timetaken

def vinput():
    #validates inputs so it can't crash and the choice can only be a, b or c
    while True:
        try:
            inp=input("Please enter your choice! ").lower()
            if inp in ["a","b","c"]:
                break
            else:
                print("That's not a valid input")
        except:
            #not strictly needed but in case something could happen
            #this is there as a fall back just in case, slightly unnecesary
            print("That's not anything!")
    return inp

def gamerun():
    #set initial values for variables
    totaltime=0
    timetaken=0
    count=0
    inv=[]
    used=[]
    print("It's 8.45, you've been up until 3am playing the Battlefront Beta")
    #makes the program wait before printing the next line
    time.sleep(4)
    print("Your girlfriend kicks you out of bed and forces you downstairs")
    time.sleep(4)
    print("you must get to college on time, lets hope nothing slows you down...")
    time.sleep(4)
    print()
    #repeats 100 times just for expansions sake
    #compiles a list to cover each of the 100 potential slots
    for count in range(0,100):
        used.append(count)
    count=0
    #repeats 3 times so 3 events happen every game
    while count < 3:
        count+=1
        choice=random.randint(0,99)
        #if number has already been generated then it will not run it and will change
        #that value to 101 which is my value for its not a valid choice
        if used[choice]!=101:
            used[choice]=101
            userpl=True
            #crude way of running all the functions but i dont know
            #a better way of doing it 
            if choice==1:
                timetaken=attack(inv)
            elif choice==2:
                timetaken=river()
            elif choice==3:
                timetaken=unicorn()
            elif choice==4:
                timetaken=prisoner()
            elif choice==5:
                timetaken=dinosaur()
            elif choice==6:
                timetaken=NickiMinaj()
            elif choice==7:
                timetaken=AppleStore()
            elif choice==8:
                timetaken==kidnapping()
            else:
                userpl=False
                count-=1
            #when an event is run then the user must hit enter to continue
            if userpl:
                print()
                a=input("Press enter to continue... ")
                print()
            
        else:
            #will not count that as one of the 3 options
            used[choice]=101
            timetaken=0
            count-=1
        #sets the user played value to true which only gets changed
        #when the user has a go 
        userpl=True 
        totaltime=totaltime+timetaken
        
    print("You've finally made it to university, and you were only {0} minutes late!".format(totaltime))
    time.sleep(2)
    
def main():
    #display main menu
    print("---Welcome to Michaels Excuses Game!---")
    print()
    print("The game where you try to get in on time to your lessons!")
    print()
    print("Would you Like to play?")
    #no matter what input you choose you can play whatever you want
    play=input("y/n? ").lower()
    if play =="y":
        print("Lets go!")
        time.sleep(2)
    else:
        print("{0}? Who cares of course you want to play!".format(play))
    while True:
        #calls the gamerun function
        gamerun()
        again=input("That was great wasn't it? would you like to play again(y/n)? ").lower()
        if again=="y":
            print("Let's go again!")
            time.sleep(2)
        elif again=="n":
            break
            print("Thanks for playing!")
            time.sleep(2)
        else:
            print("That's not really a good input is it?")

#if this is the program you click on then it will run this function

if __name__=="__main__":
    main()

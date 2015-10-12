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
    inp=vinput()
    if inp == "a":
        print("Congratulations! You are oficially a baby! And you barely got out of this. It's a god thing T-Rex got hit by lorry.")
        timetaken = 13
    elif inp == "b":
        print("You certainly are crazy.")
        timetaken == 4
    elif inp == "c":
        timetaken == 10
    print("")
    return timetaken

def attack(inv):
    timetaken=6
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
        print("You are irresponsible!)
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
    while count < 10:
        count+=1
        choice=random.randint(0,100)
        if choice==1:
            timetaken=dinosaur()
        else:
            timetaken=0
            count-=1
        totaltime=totaltime+timetaken
    print("You've finally made it to university, and you were only {0} minutes late!".format(totaltime))
    time.sleep(2)      
def main():
    print("---Welcome to Michaels Excuses Game!---")
    print()
    print("The game where you try to get in on time to your lessons!")
    print()
    print("Would you Like to play?")
    play=input("y/n?").lower()
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
    

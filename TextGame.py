import random

#mario test

def attack(inv):
    time=0
    return inv,time

def hobo(inv):
    time=0
    return inv,time

def flop(inv):
    time=5
    return inv,time


def vinput():
    while True:
        try:
            inp=input("Please enter your choice! ")
            if inp in ["a","b","c"]:
                break
            else:
                print("That's not a valid input")
        except:
            print("That's not anything!")
    return inp


def main():
    print("Welcome to the game")
    totaltime=0
    count=0
    inv=[]
    while count < 10:
        count+=1
        choice=random.randint(0,100)
        if choice==1:
            time=attack(inv)
        elif choice==2:
            time=hobo(inv)
        elif choice==3:
            time=flop(inv)
        else:
            time=0
            count-=1
        totaltime+=time
            
    


if __name__=="__main__":
    main()
    

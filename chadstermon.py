from time import sleep
import random
delay1 = 1
delay2 = 2
delay3 = 3

balls = str(input("Start Game ? Enter Yes/No "))
if balls == "no" :
    sleep(delay2)
    print ("Imagine quitting this awesome game.")
    sleep(delay2)
    print("Okay whatever. Bye")
    exit()



print("Welcome to CTRL ALT DEFEAT laborataries. Please state your name")
sleep(delay2)
a = str(input("Your name : "))
sleep(delay2)
print (a,"? Oh, you're the new guy. Welcome")
sleep(delay2)
print("Alright. Your task has come in.")
sleep(delay2)
print("Your job is to defeat pollution, the plague of this world.")
sleep(delay2)
print("Use your chadstermons to defeat it.")
sleep(delay2)
print("Good luck, you're going to need it.")

sleep(delay3)

# Variables
Reduce=10
Reduse=40
Recycle=30
basehp=250
PollutionHP=500
hit=True
PollutionHit=True
healvalue=50
potioncounter=2




print(" ")
print("A wild Pollution appeared")
print(" ")
sleep(delay2)
print("Available chadstermons : x2 chadizard")
print(" ")
print(" ")
print("You send out a chadizard")
print("Your available Attacks :")
print("   Reduce - 10 damage")
print("   Reuse - 40 damage")
print("   Recycle - 30 damage")
print(" ")
sleep(delay2)
print("Pollution HP is", PollutionHP)

for x in range(0,100):
    A=int(input("Do something. Press 1 to choose Reduce, 2 to choose Reuse and 3 to choose Recycle and press 4 to use healing potion."))
    print("Pollution HP is at",PollutionHP)
    PollutionDamage= random.randint(25,100)
    if PollutionDamage>60:
        PollutionDamage = random.randint(25, 100)
    if PollutionDamage>65:
        PollutionDamage=random.randint(25,100)
    if PollutionDamage>70:
        PollutionDamage=random.randint(25,100)
    if PollutionDamage>75:
        PollutionDamage=random.randint(25,100)
    B= random.randint(0,10)
    if B%2==0 or B==3 or B==5:
        hit=True
    if A==4 and potioncounter<=2:
        if basehp+healvalue>100:
            basehp=100
        else:
            basehp=basehp+healvalue
        print("Your hp is now", basehp)
        potioncounter=potioncounter+1
    elif potioncounter>=2 and A==4:
        print("out of potions. You missed a turn")
    if hit:
        if A==1:
            PollutionHP=PollutionHP-10
            print("hit!,Pollution hp is now",PollutionHP)
            print("your hp is", basehp)
        elif A==2:
            if B%2!=0:
                basehp=basehp-75
                PollutionHP = PollutionHP - 50
                print("hit!,Pollution hp is now", PollutionHP)
                print("you took 75 damage")
                print("your hp is",basehp)
            else:
                PollutionHP = PollutionHP - 50
                print("hit!,Pollution hp is now", PollutionHP)
                print("your hp is", basehp)
        elif A==3:
            PollutionHP=PollutionHP-20
            print("hit!,Pollution hp is now", PollutionHP)
            print("your hp is", basehp)
    if B==8 or B%2!=0:
        PollutionHit=True
    else:
        PollutionHit=False
    if PollutionHit:
        basehp=basehp-PollutionDamage
        print("you got hit")
        print("Pollution did", PollutionDamage, "damage")
        print("your hp is now",basehp)
    else:
        print("Pollution missed")
    if basehp<=0:
        print("you died")
        R=int(input("would you like to run or send out another chadizard? 1=run,0=send another chadizard"))
        if R==1:
            runchance=random.randint(0,10)
            if runchance==5 or runchance==7 or runchance%2==0:
                print("You escaped safely")
                break
            else:
                print("You tripped while running and were unable to escape.")
                R=0
        else:
            print("you sent out another chadizard")
            chadizardhp = 100
            print("chadizard's hp is", chadizardhp)
            print("Pollution used a max healing potion")
            PollutionHP2 = 100
            print("PollutionHP is", PollutionHP2)
            print("chadizard can use moves which follow:")
            print("Attack1: Forest fire:45dmg,10dmg burn(press1),Attack2=Flextape:heals 40hp(press2),Attack3:50% damage decrease")

            for chadizard in range(1,69420):
                PollutionDamage = random.randint(25, 100)
                if PollutionDamage > 60:
                    PollutionDamage = random.randint(25, 100)
                if PollutionDamage > 65:
                    PollutionDamage = random.randint(25, 100)
                if PollutionDamage > 70:
                    PollutionDamage = random.randint(25, 100)
                if PollutionDamage > 75:
                    PollutionDamage = random.randint(25, 100)
                B = random.randint(0, 10)
                if B % 2 == 0 or B == 3 or B == 5:
                    hit = True
                P = int(input("pick an attack!"))
                if P == 1:
                    PollutionHP2 = PollutionHP2 - 45
                    print("Hit! Pollution hp is", PollutionHP)
                    burn = True
                    burnprob = random.randint(0, 10)
                    if burnprob % 2 == 0 or burnprob == 5:
                        burn = False
                    if burn:
                        for y in range(1, 2):
                            print("NotPokemon was burned")
                            PollutionHP2 = PollutionHP2 - 10
                            print("Pollution hp is", PollutionHP2)
                    chadizardhp=chadizardhp-PollutionDamage
                    print("chadizard's hp is",chadizardhp)
                elif P==2:
                    if chadizardhp+40<=100:
                        chadizardhp = chadizardhp + 40
                    else:
                        chadizardhp = 100
                    print("chadizard's hp is,",chadizardhp)
                    chadizardhp = chadizardhp - PollutionDamage
                    print("chadizard's hp is,", chadizardhp)
                elif P==3:
                    for x in range(1,3):
                      print("Pollution damage was",PollutionDamage)
                      PollutionDamage=PollutionDamage*0.5
                      print("it's now",PollutionHP)
                      chadizardhp=chadizardhp-PollutionDamage
                      print("chadizard's hp is,", chadizardhp)

    elif PollutionHP<=0:
        print("Wow grape, what a chadizard")
        print("Pollution fainted.")
        print("Big W, you won.")
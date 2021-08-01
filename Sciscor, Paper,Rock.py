import random
from random import randint
t=["Rock","Paper","Scissor"]
# we have to set our Computer Player
computer=random.choice(t)
# first we have to set our player at false/True
player=True

while player==True:
    player=input('Rock,Scissor,Paper?')
    if player==computer:
        print("Tied!")
    elif player=="Rock":
        if computer == "Scissor":
            print("You win!",player,"will make unsharped",computer)
        else:
            print("You lose",computer,"cut ",player)

    elif player=="Scissor":
        if computer=="Paper":
            print("You win",player,"will cut ",computer)
        else:
            print("You lose!",player,"will break",computer)


    elif player=="Paper":
        if computer=="Rock":
            print("You win",player,"Will grabed",computer)
        else:
            print("you lose",computer,"will break",player)

    else:
        print("You have entered wrong Spelling\n Please check your Spelling")
    player=True
    computer=random.choice(t)






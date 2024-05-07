import random as rm

score = [0,0]
player = None
choices = ("rock","paper","scissors")
computer = rm.choice(choices)
while player not in choices:
    player = input("Rock,Paper or Scissors?: ").lower()
    
if player == computer:
    print("Computer: ",computer)
    print("Player: ",player)
    print("Tie!")
elif player == choices[0]:
    if computer == choices[1]:
        print("Computer: ",computer)
        print("Player: ",player)
        print("You Lose!")
    elif computer == choices[2]:
        print("Computer: ",computer)
        print("Player: ",player)
        print("You Win!")
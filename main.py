import random as rm

score = [0,1]
player = None
choices = ("rock","paper","scissors")
computer = rm.choice(choices)
while player not in choices:
    player = input("Rock,Paper or Scissors?: ").lower()
    
if player == computer:
    print("Computer: ",computer)
    print("Player: ",player)
    print("Tie!")

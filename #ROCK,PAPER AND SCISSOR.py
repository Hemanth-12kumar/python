#ROCK,PAPER AND SCISSOR

import random
Options=("rock","paper","scissor")
Player=input("Enter the choice rock,paper,scissor:  ").lower()
computer=random.choice(Options)
print(f"your choice:{Player}")
print(f"Computer choice:{computer}")
if Player==computer:
  print("Its TIE")
elif (Player=="rock"and computer=="scissor"): 
   print("you win")
elif (Player=="scissor" and computer=="paper"):
    print("you win")
elif (Player=="paper" and computer=="rock"):
   print("you win")

else:
   print("You lose")

#Name: Leon Chen
#Date: May 10
#This program allows you to play rock paper scissors against a computer which generates a random move

import random
#input data
move=int(input("Enter your move (1=rock, 2=paper, 3=scissors):"))
compMove=random.randint(1, 3)

#process data
if move>3 or move<1:
    print("\nPlease give a valid move.")
elif move==1 and compMove==1:
    print("\nPlayer throws rock")
    print("Computer throws rock")
    print("Tie.")
elif move==1 and compMove==2:
    print("\nPlayer throws rock")
    print("Computer throws paper")
    print("Computer wins!")
elif move==1 and compMove==3:
    print("\nPlayer throws rock")
    print("Computer throws scissors")
    print("Player wins!")
elif move==2 and compMove==1:
    print("\nPlayer throws paper")
    print("Computer throws rock")
    print("Player wins!")
elif move==2 and compMove==2:
    print("\nPlayer throws paper")
    print("Computer throws paper")
    print("Tie.")
elif move==2 and compMove==3:
    print("\nPlayer throws paper")
    print("Computer throws scissors")
    print("Computer wins!")
elif move==3 and compMove==1:
    print("\nPlayer throws scissors")
    print("Computer throws rock")
    print("Computer wins!")
elif move==3 and compMove==2:
    print("\nPlayer throws scissors")
    print("Computer throws paper")
    print("Player wins!")
else:
    print("\nPlayer throws scissors")
    print("Computer throws scissors")
    print("Tie.")

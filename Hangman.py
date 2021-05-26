import random
import re
player2_char=[]
wrong=[]
word=random.choice(["rush","history","contacts","Silicone","Painting","service"])

for i in range(10):
    p2=input("Guess an alhpabet")
    if len(p2)==1:
        p2 = p2.lower()
        if p2 in word and p2 not in player2_char:
            player2_char.append(p2)
            if len(player2_char)==len(word):
                print("You Have won\n the right word is",word)
                break


        else:
            wrong.append(p2)
            print("This alphbet is not in word")


    else:
        print("Please enter right input")


if len(player2_char) != len(word):
    print("The right word is",word)
    print("You Have lost the Game\n Try next time")








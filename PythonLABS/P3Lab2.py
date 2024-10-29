#CTI 110
#P3Lab2 - Grades and Gaming
#BurnsA
#10/29/24
import random

def main():
    print("Craps Game")
    print("Roll from 1 to 6")
    #die1=int(input("First Die: "))
    #die2=int(input("Second Die: "))
    #random rolls
    die1=random.randint(1,6)
    die2=random.randint(1,6)

    total=die1+die2
    print("Roll:", die1, "+", die2, "is", total)

#win or loose?
#7 or 11 --> win, 2 or 12 --> lose. Rest to be continued
    if total==7:
        print("You Win!")
    elif total==11:
        print("You Win!")
    elif total==2:
        print("LOSER")
    elif total==12:
        print("LOSER")
    else:
        print("Point was", total)
        print("To be continued -->")
        

#start program
main()

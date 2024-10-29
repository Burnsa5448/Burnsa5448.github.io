# CTI 110
# P3LAB1 - Choose your adventure
# BurnsA
# 10/22/24

def main():
    print("Choose your adventure")
    go_home()
#the "go home safe route"
def go_home():
    print("Oh, okay. I guess you can go home. Never thought of that.")
    print("Maybe you could get some food?")
    print("1. Get chinese")
    print("2 Order pizza")
    choice=int(input())
    if choice==1:
        get_chinese()
    elif choice==2:
        get_pizza()

def get_chinese():
    print("The chinese food gets delivered, it's perfectl fine. Except maybe it's a bit cold")
def get_pizza():
    print("There is a knock at the door, must be the pizza you ordered.") #italics
    print("When you answer the door all you see is pizza at the door step.")
    print("Do you decide to tip?")
    #if you tip you stay alive and eat pizza
    #say no and you die, ALWAYS TIP!
#start program
#main()

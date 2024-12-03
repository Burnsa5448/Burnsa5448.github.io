#CTI 110
#P3LAb1
#BurnsA

def main():
    print("Choose Your Own Adventure. Do you go home or to the movies?")
    print("Choose 1, 2, or 3")
    print("1. Go home")
    print("2. Go to the movies")
    print("3. Find something else to do")
    choice = input()
    if choice == "1":
        go_home()
        print("You DIED")
    elif choice == "2":
        go_movies()
        print("You SURVIVE")
    else:
        print("You end up getting gas station pizza... you live... but are you happy? MEH end.")


def go_home():
    print("You go home...")
    
def go_movies():
    print("Do you go to the movies?... ")
    print("What movie do you want to see?")
    print("You can pick 'Phantom of the Opera, 1925' or... whatever other movie. 1 or 3?")
    choice = input()
    if choice == "1":
        print("That's a great one! Good choice, and enjoy!")
    elif choice == "3":
        print("Ugh, fine I guess. You're the loser, not me")
#start    
main()

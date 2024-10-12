# CTI 110
# P2LAB1
# BurnsA
# 10/10/24

#This program adds up sales

#the variables
num_tickets=0
num_candy=0
num_drink=0
num_popcorn=0

ticket_cost=4.99
candy_cost=2.99
drink_cost=1.99
popcorn_cost=2.00

#tickets
print(input("Welcome to the theaters. What movie have you come to see tonight? "))
num_tickets=int(input("Oh... I heard that one is haunted. Anyways, how many tickets? "))
print("Alright, that's", num_tickets, ". Did you want any snacks?")

#candy
print(input("What kind of candy do you want? "))
num_candy=int(input("Uhm, sure. I guess you can get that kind. How many did you want? "))
print("Okay so that's", num_candy, ". Did you want any drinks to wash that down?" )

#drinks
print(input("What drink did you want? "))
num_drink=int(input("Oh thank god, you're a little normal. Alright, how many did you want? "))
print("So thats", num_drink, ". Any popcorn? It is a movie classic snack.")

#popcorn
num_popcorn=int(input("How many buckets of popcorn? "))
print("So you want", num_popcorn, ". Let me get that total.")

#total
print("-"*40)
ticket_total=num_tickets*ticket_cost
candy_total=num_candy*candy_cost
drink_total=num_drink*drink_cost
popcorn_total=num_popcorn*popcorn_cost
movie_total=ticket_total+candy_total+drink_total+popcorn_total

print(num_tickets, "Tickets\t$", format(ticket_total, ".2f"))
print(num_candy, "Candy\t\t$", format(candy_total, ".2f"))
print(num_drink, "Drinks\t$", format(drink_total, ".2f"))
print(num_popcorn, "Popcorn\t$", format(popcorn_total, ".2f"))
print("Total\t\t$", format(movie_total, ".2f"))

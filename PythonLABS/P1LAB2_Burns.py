# CTI 110
# P1LAB2 - Receipt
# BurnsA
# 10/01/24

print("P1LAB2")
#a resturant that sells burgers and fries - end goal make a receipt

#DECLARE the variables
num_burgers=0
num_fries=0
burger_cost=4.99
fry_cost=1.99

#start
print("Can I take your order?")

#burgers
num_burgers=int(input("How many burgers? "))

print("You ordered", num_burgers, "burgers.")

#fries
print("-"*30)
print("Do you wanna pair that with some fries today?")

num_fries=int(input("How many baskets of fries? "))

print("You ordered", num_fries, "of the fry baskets.")
print("-"*40)

#prices
burger_total=num_burgers*burger_cost
fry_total=num_fries*fry_cost
meal_total=burger_total+fry_total
print("-"*40)
print(num_burgers, "Burgers\t$", burger_total)
print(num_fries, "Basket of Fries\t$", fry_total)
print("Total\t\t$", meal_total)

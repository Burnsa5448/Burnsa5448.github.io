# CTI 110
# P1HW2
# A Burns
# 10/08/24

# This is a travel budget program
""""
3. Ask user to enter budget
4. Ask destination
5. Amount they spend on gas or tickets
6. Amount on accomadtion 
7. Amount on food
8. Add Expenses
9. Subtract expenses from budget
10. Display results
"""
print("🛫 Trip Calculator 🛬")
# Ask  user their budget 
budget=float(input("What is your travel budget? $"))
# Where is it
destination=input("Where are you going? ")
#travel cost ie gas or tickets
travel=input("How much will gas or tickets be? $")
# how much for a hotel or airbnb or whatever
hotel=input("How much are you spendingon a hotel or airbnb? $")
# food costs
food=input("How much do you plan to spend on food? $")
print("-"*40)
# add all the expenses together

total_exp=travel+hotel+food


print("Your budget: $", format(budget, ".2f"))
# subtract it from the budget


#displat the results
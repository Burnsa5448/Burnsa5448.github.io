#CTI 110
#P2LAB2 - Lists
#BurnsA
#10/17/24

#example list
numbers=[1, 2, 3, 4]
print(numbers)

#ask user to enter four numbers
print("Please enter four numbers (enter after each)")
num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())

my_numbers=[num1, num2, num3, num4]
print("You entered these numbers;", my_numbers)

print("There are", len(my_numbers), "numbers.")
print("Smallest: ", min(my_numbers))
print("Largest: ", max(my_numbers))
print("The total is: ", sum(my_numbers))
average=sum(my_numbers) / len(my_numbers)
print=("The average: ", average)


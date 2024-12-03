#test - BurnsA
"""
print("test program")
count=1
while count <= 5:
    print("count is", count)
    count=count+1
print("done")
"""
#test 2
"""
print("Program test")
for number in range(1,6):
    print(number)
print("done")
"""
#test 3
"""
#input validation
num=int(input("Type a number from 1 to 3.  "))
while num < 1 or num > 3:
    print("Please try again.")
    num=int(input("Type a number from 1 to 3.  "))
print("You entered", num)
"""
#end of test

#____________________________________________

#CTI 110
#P4LAB2 - Times Tables
#BurnsA

#ask for a number tha's 0 or higher
#display times tables for that number
#from times tables 1 to 12
#finally, repeat

def times_table():
    num=int(input("Enter a number: "))
    while (num < 0):
            print("No negative numbers, none.")
            num=int(input("Enter a number: "))
    print("You entered", num)

#times table time
    for num2 in range(0,13):
        answer=num*num2
        print(num,"*", num2, "=", answer)
            
def main():
    times_table()
    again=input("Do you want to run it again? ")
    while(again=="Yes" or again=="yes" or again=="YES"):
        times_table()
        again=input("Do you want to run again? ")
        print("Goodbye")

#start program
main()

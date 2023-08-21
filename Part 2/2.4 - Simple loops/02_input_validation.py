from math import sqrt
# Write your solution here
number = 1
while number != 0:
    number = int(input("Please type in a number:"))
    if number > 0:
        print(f"{sqrt(number)}")
    elif number < 0:
        print("Invalid number") 
    if number == 0:
        print("Exiting...")
        break 




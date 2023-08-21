# Write your solution here
count = 0
numbersum = 0
pos = 0
neg = 0

print("Please type in integer numbers. Type in 0 to finish.")
number = int(input())

while number != 0:

    count += 1
    numbersum += number
    if number > 0:
        pos += 1
    elif number < 0:
        neg += 1
    number = int(input("Number:"))


else:
    print(f"Numbers typed in {count}")
    print(f"The sum of the numbers is {numbersum}")
    print(f"The mean of the numbers is {numbersum/count}")
    print(f"Positive numbers {pos}")
    print(f"Negative numbers {neg}")
 

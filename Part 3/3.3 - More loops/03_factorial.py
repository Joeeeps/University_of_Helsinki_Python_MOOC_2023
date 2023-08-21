# Write your solution here
number = int(input("Please type in a number:"))
i = 1
factorial = 1  
 
while True:
    if number < 1:
        print("Thanks and bye!")
        break
    while number >= 1:
        while i <= number:
            factorial *= i 
            i += 1  
        print(f"The factorial of the number {number} is {factorial} ")
        number = int(input("Please type in a number:")) 
        factorial = 1
        i = 1 
        continue

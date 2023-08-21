# Write your solution here
number1 = int(input("Give me a number"))
number2 = int(input("GIve me a second number"))
operation = (input("add, multiply or subtract?"))

if operation == "add":
    print(f"{number1} + {number2} = {number1 + number2}") 
    
if operation == "multiply":
    print(f"{number1} * {number2} = {number1 * number2}") 

if operation == "subtract":
    print(f"{number1} - {number2} = {number1 - number2}") 

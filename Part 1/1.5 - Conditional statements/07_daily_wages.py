# Write your solution here

wage = float(input("What's your hourly wage?"))
hours = float(input("How many hours worked?"))
day = input("What day is it?")

if day == "Sunday":
    print(f"Daily wages: {(wage*hours)*2} euros")

if day != ("Sunday"):
    print(f"Daily wages: {wage*hours} euros")

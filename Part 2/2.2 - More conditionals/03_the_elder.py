# Write your solution here
name1 = input("What is the first persons name?")
age1 = int(input("What is the first persons age?"))
name2 = input("What is the second persons name?")
age2 = int(input("What is the second persons age?"))

if age1 > age2:
    print(f"The elder is {name1}") 
elif age1 < age2: 
    print(f"The elder is {name2}")
else: 
    print(f"{name1} and {name2} are the same age")

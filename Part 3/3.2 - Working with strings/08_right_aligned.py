# Write your solution here
string = input("Please type in a string: ")
length = 1 
star = "*"

while len(string) + length < 20:
    star += "*"
    length += 1 
print(f"{star}{string}")
 

